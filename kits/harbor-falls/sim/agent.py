"""Hero run: real Claude (headless, isolated from my hooks/CLAUDE.md) audits each site and writes the outreach email.
Usage: python3 agent.py [N]   (N = first N businesses; default all). Results cached in runs/hero/<id>.json."""
import json, subprocess, sys, pathlib, re, time, os, tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKET = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "market.json")
SITES = ROOT / (sys.argv[4] if len(sys.argv) > 4 else "sites")
OUT = ROOT / "runs" / (sys.argv[3] if len(sys.argv) > 3 else "hero")
OUT.mkdir(parents=True, exist_ok=True)
MODEL = "sonnet"
CLEAN = tempfile.mkdtemp()  # run Claude in an empty folder, so no project settings leak in
FLAGS = {
    "no_mobile": "the page is not set up for phones (no viewport meta tag)",
    "no_booking": "visitors cannot book or schedule online (no booking link or form; text that merely says to book does not count)",
    "no_click_to_call": "the phone number is not a tappable tel: link",
    "heavy_images": "photos are huge, unoptimised originals (very large pixel widths, 'original' MB file names, no lazy loading)",
    "no_reviews": "no customer reviews or testimonials on the page",
    "stale_footer": "the footer copyright year is old (before 2026)",
    "no_hours": "no opening hours are shown",
    "weak_title": "the page title is generic and there is no meta description (hurts Google visibility)",
}


def ask(prompt, system):
    r = subprocess.run(
        ["claude", "-p", "--model", MODEL, "--setting-sources", "", "--strict-mcp-config", "--disable-slash-commands", "--system-prompt", system],
        input=prompt, capture_output=True, text=True, timeout=240, cwd=CLEAN)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    return json.loads(m.group(0))


def audit(b, html):
    defs = "\n".join(f"- {k}: {v}" for k, v in FLAGS.items())
    p = f"""Audit this local business website. For each check below say whether the PROBLEM is present (true) or absent (false), and give a verbatim quote from the HTML as evidence (for a missing feature, quote the closest line you looked at, or NONE).
Checks:
{defs}

Reply with JSON only: {{"flags": {{<check>: true|false}}, "evidence": {{<check>: "<verbatim quote or NONE>"}}}}

HTML:
{html}"""
    return ask(p, "You are a careful, literal website auditor. You only claim what the HTML shows.")


def email(b, aud, html=None):
    found = [k for k, v in aud["flags"].items() if v]
    p = f"""You run Northlight Web, a one-person agency that fixes local business websites for a flat fee. Write a short cold email (under 110 words, plain text, no hype, no emoji) to {b['owner'].split()[0]}, owner of {b['name']} ({b['trade']}, Harbor Falls).
Use ONLY these problems found on their site: {', '.join(found) or 'none found'}. Mention the one or two that cost them the most customers, concretely. Offer a free 10-minute walkthrough. Sign off as Alex.
{("Their page, for context:" + chr(10) + html) if html else ""}

Reply with JSON only: {{"subject": "...", "body": "...", "flaws_mentioned": [<check ids from the list you used>]}}"""
    return ask(p, "You write short, honest, specific cold emails for a small agency. No fake claims.")


def one(b):
    f = OUT / f"{b['id']}.json"
    if f.exists():
        return
    html = (SITES / f"{b['id']}.html").read_text()
    for attempt in range(2):
        try:
            t = time.time()
            a = audit(b, html)
            assert set(FLAGS) <= set(a['flags']) and set(FLAGS) <= set(a['evidence']), 'audit keys'
            e = email(b, a, html if os.environ.get("EMAIL_SEES_HTML") == "1" else None)
            assert isinstance(e.get('flaws_mentioned'), list) and e.get('body') and e.get('subject'), 'email keys'
            f.write_text(json.dumps({"id": b["id"], "audit": a, "email": e, "secs": round(time.time() - t, 1)}, indent=1))
            print(f"{b['id']}  {b['name']:<30} audited + email written  {time.time() - t:4.1f}s", flush=True)
            return
        except Exception as ex:
            err = repr(ex)
    (OUT / f"{b['id']}.err").write_text(err)


if __name__ == "__main__":
    market = json.loads(MARKET.read_text())
    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(market)
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(one, market[:n]))
    print(len(list(OUT.glob("*.json"))), "done,", len(list(OUT.glob("*.err"))), "errors")
