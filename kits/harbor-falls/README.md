# Harbor Falls: run the Claude AI agency simulation yourself

This is the kit from the AI Walkthru video "I Let Claude Run an AI Agency for 30 Days (Simulation)".
Everything is fictional: 240 made-up local businesses in a made-up town. Nobody gets emailed.

**What is real:** Claude's audits, emails and replies (headless Claude Code, model Sonnet).
**What is an assumption:** how owners reply, book calls and pay. Those rules are in `SPEC.md`, written before the run, and in `sim/model.py`.

My own results are included in `runs/`, so you can score them without running anything.

## What you need

- A Mac or a Linux computer (on Windows, use WSL).
- Python 3. Type `python3 --version` in the Terminal to check.
- Claude Code, signed in to a paid Claude plan. Type `claude --version` to check.
  The full run is about 600 small requests (240 audits, 240 emails, traps and replies).

## Step by step (the same order as the video)

1. **Check your tools.** `claude --version` and `python3 --version`.
2. **Open the folder.** `cd harbor-falls`, then `ls` and `ls sim`.
   - `gen_market.py` builds the town, `gen_traps.py` builds the trick pages,
     `agent.py` sends each site to Claude, `reply_test.py` sends Claude the owner replies,
     `model.py` scores everything and plays out the 30 days.
3. **Build the town.** `python3 sim/gen_market.py`
   It prints `240 businesses, 865 seeded flaws (3.60 avg), 26 decoy sites`. The seed is fixed, so your town matches mine.
   Count the pages with `ls sites | wc -l`, open one with `open sites/b001.html`, and read its code with `cat sites/b001.html`.
4. **Look at the answer key.** `open answer_key.json`. Claude never sees this file.
5. **Read the prompt.** `open sim/agent.py`: the eight checks, the "quote the page as proof" rule, and the email prompt.
6. **Run Claude on a few sites.** `python3 sim/agent.py 8 market.json live`
   Results land in `runs/live/`. Open one with `open runs/live/b007.json`.
   To run all 240 into `runs/hero/` (about 15 minutes): `python3 sim/agent.py`
   (my 240 results are already in `runs/hero/`; delete that folder first if you want your own).
7. **Score it.** `python3 sim/model.py`. The first line is the audit score against the answer key.
8. **Try to trick it.** `python3 sim/gen_traps.py` builds 12 trap pages in `sites_traps/`.
   Run them: `EMAIL_SEES_HTML=1 python3 sim/agent.py 12 traps.json traps2 sites_traps`
   (my run is in `runs/traps2/`; use a new folder name, for example `traps-mine`, for your own).
9. **Read the emails.** `open runs/hero/b001.json`.
10. **Test the replies.** `python3 sim/reply_test.py reply-mine` sends the 40 scripted owner replies to Claude.
    My run is in `runs/reply/`. Read every "how do I pay?" reply yourself (`runs/reply/buy-*.json`): the AI grader missed invented terms.
11. **Read the owner rules.** `open SPEC.md`.
12. **Play it out.** `python3 sim/model.py` again: one month, 1,000 months, and the levers.
    The day-by-day log of the month is in `results.json` under `"hero"` → `"log"`.
13. **Change a number.** `nano sim/model.py`, change `PRICE, FIXED_COST = 900, 280`, save (Control-O, Enter), exit (Control-X), and run `python3 sim/model.py` again.

## Notes

- On Linux, use `xdg-open` where the steps say `open`.
- `model.py` scores the folders `runs/hero`, `runs/traps`, `runs/traps2` and `runs/reply`.
- `agent.py` runs Claude with `--setting-sources ""` in an empty temporary folder, so your own Claude Code settings do not change the results.
- This is a simulation with my assumptions. It shows the shape of a month, not what you will earn. Not financial advice.
