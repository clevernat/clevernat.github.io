# Fable 5.2 vs Opus 5.5: the test pack

The three prompts, the file and the answer key from the AI Walkthru video "I Gave Fable 5.2 and Opus 5.5 the Same 3 Jobs".
Run it yourself: a new chat on claude.ai for each job, the same effort setting for both models, the prompt sent once, no follow-up. Start a clock when you press Send.

My results (one run each, effort High, 10 November 2026): Opus 5.5 took 14:18, 3:00 and 4:03. Fable 5.2 took 20:46, 5:25 and 7:53. Both passed every check. Yours may differ.

## Job 1: a teaching tool

Prompt:

> Build an interactive simulator of a car's open differential that I can use to teach how it works. One page that runs in the browser. Show the ring gear and carrier, the spider gears and both axle shafts, all turning. Give me buttons for: drive straight, turn left, turn right, and hold the left wheel still. Show live RPM for the carrier, the left wheel and the right wheel. The physics must be correct.

Answer key. In an open differential, left wheel speed + right wheel speed = 2 x carrier speed, always.

1. Drive straight: left = right = carrier.
2. Turn left: left is slower than the carrier, right is faster, and left + right = 2 x carrier.
3. Turn right: the mirror of check 2.
4. Hold the left wheel still: left = 0, right = 2 x carrier.
5. All four buttons exist and the gears are seen turning.

Pass = the RPM readouts obey the rule in every mode. Extras are noted, not scored.

## Job 2: a messy spreadsheet

File: `expenses-messy.csv` (88 rows; made-up spending, no real person's data). Attach it, then send the prompt.

Prompt:

> This file is three months of my spending and it is messy. Clean it and build me a one-page budget dashboard. Remove rows that are exact duplicates. Treat category names as the same when they differ only by capital letters or spaces. Refunds are negative and reduce the total. Show the total for each category, the grand total, how many rows you removed, and a chart. Check your totals against the file before you finish.

Answer key. 88 rows in the file, 4 exact duplicates to remove, 84 rows left, 3 refunds.

| Category | Total |
| --- | --- |
| Rent | 4,350.00 |
| Health | 1,641.81 |
| Utilities | 1,254.30 |
| Groceries | 809.22 |
| Eating out | 463.98 |
| Transport | 463.25 |
| Subscriptions | 92.29 |
| **Grand total** | **9,074.85** |

Pass = seven categories and no more, every total and the grand total match to the cent, 4 rows removed, a chart is shown.

## Job 3: an operating system in the browser

Prompt:

> Build an operating system that boots in the browser, in one page. A boot screen, then a desktop with icons and a clock. Windows I can open, drag and close. Four apps that really work: a notes app that keeps what I type after I close and reopen it, a calculator, a paint app, and a snake game I play with the arrow keys.

Answer key, six checks:

1. A boot screen, then a desktop with icons and a clock.
2. A window opens, drags and closes.
3. Notes: type "milk and eggs", close the window, reopen it. The text is still there.
4. Calculator: 12 x 12 = 144.
5. Paint: a drawn line stays on the canvas.
6. Snake: the snake moves with the arrow keys.

Score = how many of the six pass.
