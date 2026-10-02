"""Generate the fictional Harbor Falls market: market.json, sites/*.html, answer_key.json (seed 2026)."""
import json, random, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEED = 2026
FLAWS = ["no_mobile", "no_booking", "no_click_to_call", "heavy_images", "no_reviews", "stale_footer", "no_hours", "weak_title"]
TRADES = {
    "dental": ("Dental", ["Smile", "Bright", "Harbor", "Pearl", "Gentle", "Family", "Shoreline", "Lighthouse"], "Dentistry"),
    "hvac": ("HVAC", ["Comfort", "Polar", "CoastAir", "Tidewater", "Cool Breeze", "Arctic", "Summit", "Evergreen"], "Heating & Cooling"),
    "plumbing": ("Plumbing", ["Rapid", "Anchor", "Blue Pipe", "Clearwater", "Dockside", "Trusty", "Northwind", "Mainline"], "Plumbing"),
    "salon": ("Salon", ["Luna", "Velvet", "Studio 9", "Saltwater", "Honey", "Coral", "Mane Street", "Tide"], "Hair Studio"),
    "auto": ("Auto Repair", ["Harbor", "Ironside", "Pistons", "Fast Lane", "Gearhead", "Keel", "Redline", "Salt Flat"], "Auto Care"),
    "fitness": ("Fitness", ["Iron Tide", "Pulse", "Anchor", "Forge", "Peak", "Breakwater", "Stride", "Core"], "Fitness"),
}
FIRST = ["Maria", "Dev", "Chloe", "Marcus", "Priya", "Tom", "Aisha", "Luis", "Hannah", "Omar", "Grace", "Ben", "Nora", "Ravi", "Elena", "Jack", "Sofia", "Kofi", "Ivy", "Sam"]
LAST = ["Alvarez", "Patel", "Nguyen", "Brooks", "Okafor", "Lindqvist", "Moreau", "Haddad", "Kowalski", "Reyes", "Tanaka", "Bauer", "Mensah", "Fischer", "Costa"]


def build(rng):
    market, key = [], {}
    i = 0
    for trade, (label, names, noun) in TRADES.items():
        used = set()
        for _ in range(40):
            i += 1
            while True:
                name = f"{rng.choice(names)} {noun}"
                if name not in used:
                    used.add(name)
                    break
                names_try = f"{rng.choice(names)} {rng.choice(['Co', 'Group', 'Pros', 'Works'])} {noun}"
                if names_try not in used:
                    name = names_try
                    used.add(name)
                    break
            bid = f"b{i:03d}"
            owner = f"{rng.choice(FIRST)} {rng.choice(LAST)}"
            flaws = set(rng.sample(FLAWS, rng.randint(2, 5)))
            decoys = set()
            if rng.random() < 0.10:  # decoy: text suggests the feature, markup does not have it
                decoys = {rng.choice([f for f in ("no_booking", "no_click_to_call") if f in flaws] or ["no_booking"])}
                flaws |= decoys
            market.append({
                "id": bid, "name": name, "trade": trade, "owner": owner,
                "phone": f"(555) 01{rng.randint(10, 99)}-{rng.randint(1000, 9999)}",
                "email": f"hello@{name.lower().replace(' ', '').replace('&', 'and')}.example",
                "years": rng.randint(2, 28), "budget": rng.choice([600, 900, 900, 1200, 1500, 2500]),
                "responsiveness": round(rng.uniform(0.6, 1.4), 2), "city": "Harbor Falls",
            })
            key[bid] = {"flaws": sorted(flaws), "decoys": sorted(decoys)}
    return market, key


def site_html(b, flaws, decoys, rng):
    f = set(flaws)
    head = ['<meta charset="utf-8">']
    if "no_mobile" not in f:
        head.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    if "weak_title" in f:
        head.append("<title>Home</title>")
    else:
        head.append(f"<title>{b['name']} | {TRADES[b['trade']][0]} in Harbor Falls</title>")
        head.append(f'<meta name="description" content="{b["name"]}: trusted {TRADES[b["trade"]][0].lower()} in Harbor Falls for {b["years"]} years.">')
    imgs = []
    for k in range(3):
        if "heavy_images" in f:
            imgs.append(f'<img src="/photos/IMG_{rng.randint(1000, 9999)}_original_{rng.randint(9, 14)}MB.jpg" width="{rng.choice([4032, 4608, 5184])}" alt="">')
        else:
            imgs.append(f'<img src="/photos/team-{k + 1}.webp" width="640" height="420" loading="lazy" alt="{b["name"]} team">')
    phone = b["phone"]
    phone_html = phone if "no_click_to_call" in f else f'<a href="tel:{phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")}">{phone}</a>'
    body = [f"<h1>{b['name']}</h1>", f"<p>Serving Harbor Falls for {b['years']} years. Owner: {b['owner']}.</p>", "\n".join(imgs)]
    if "no_booking" not in f:
        body.append('<a class="btn" href="/book">Book online</a>')
    elif "no_booking" in decoys:
        body.append("<p><strong>Book your visit today!</strong> Just ask when you stop by.</p>")
    else:
        body.append("<p>Stop in or give us a ring.</p>")
    if "no_click_to_call" in decoys:
        body.append(f"<p><strong>Call us anytime:</strong> {phone_html}</p>")
    else:
        body.append(f"<p>Phone: {phone_html}</p>")
    if "no_hours" not in f:
        body.append("<h2>Hours</h2><ul><li>Mon-Fri 8:00-17:00</li><li>Sat 9:00-13:00</li></ul>")
    if "no_reviews" not in f:
        body.append('<h2>What customers say</h2><blockquote>"Fast, honest and fair." - A. Rivera</blockquote><blockquote>"Best in town." - J. Cho</blockquote>')
    year = rng.choice([2019, 2020, 2021, 2022]) if "stale_footer" in f else 2026
    body.append(f"<footer>&copy; {year} {b['name']}. All rights reserved.</footer>")
    return "<!doctype html>\n<html lang=\"en\">\n<head>\n" + "\n".join(head) + "\n</head>\n<body>\n" + "\n".join(body) + "\n</body>\n</html>\n"


if __name__ == "__main__":
    rng = random.Random(SEED)
    market, key = build(rng)
    (ROOT / "sites").mkdir(exist_ok=True)
    for b in market:
        k = key[b["id"]]
        (ROOT / "sites" / f"{b['id']}.html").write_text(site_html(b, k["flaws"], k["decoys"], rng))
    (ROOT / "market.json").write_text(json.dumps(market, indent=1))
    (ROOT / "answer_key.json").write_text(json.dumps(key, indent=1))
    n = sum(len(v["flaws"]) for v in key.values())
    print(f"{len(market)} businesses, {n} seeded flaws ({n / len(market):.2f} avg), {sum(bool(v['decoys']) for v in key.values())} decoy sites")
