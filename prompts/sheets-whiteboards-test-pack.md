# Claude Sheets + Whiteboards test pack (AI Walkthru)

Three jobs I gave Claude Sheets and Claude Whiteboards on claude.ai, with my answer key. Paste each prompt into a new chat.

## p1-budget

Make a hiring budget by team and quarter for 2027. New hires per quarter (Q1, Q2, Q3, Q4): Engineering 2, 1, 3, 0. Sales 1, 2, 0, 1. Support 0, 1, 1, 2. Yearly salary per hire: Engineering $120,000, Sales $80,000, Support $55,000. Every hire costs a quarter of their yearly salary in each quarter they are on the team, starting with the quarter they join. Put the inputs in their own cells and use formulas for every cost. Add totals for each team, each quarter and the whole year, and a Status dropdown for each team with Planned, Approved and On hold.

## p1-ask

Why is Q3 so much higher than Q2?

## p1-move

Engineering moves its three Q3 hires to Q4. Update the sheet and tell me how much the year total changes.

## p1-chart

Add a bar chart of the total cost per quarter.

## p2-invoices

Turn this file into a sheet for our conference budget. Remove duplicate invoices, fix any amount stored as text, and add: the total by vendor, the total paid, the total still owed, and the budget remaining from $20,000 after every invoice. Highlight every unpaid invoice that is overdue as of November 11, 2026. Tell me what you removed or fixed.

## p3-board

Brain dump for launching our app Tidy on March 2, 2027. Priya runs the closed beta from January 19 to February 9. Maya finishes the app store screenshots by February 6. Leo writes the launch email by February 13, after Maya's screenshots are done. Leo books three podcast interviews by February 16. Maya records the demo video by February 18. Sam fixes the beta bugs by February 20, after the beta ends. Priya submits the app for review by February 23, after Sam's fixes. Sam sets up the help center by February 25. Leo schedules the launch posts by February 27. Everyone joins the launch day call on March 2. Put this on a whiteboard: group it by person, lay it out on a timeline, and connect the tasks that depend on each other.

## p3-gaps

What's missing between submitting the app for review and launch day? Add your suggestions to the board.

## p3-plan

Turn this board into a project plan.

Job 2 needs conference-invoices.csv (download it next to this file).

# Answer key

Model: whatever claude.ai's default is on the account at recording time (Opus 5.5, effort High, as shown in the composer). One run per test.

## Test 1: hiring budget (prompt `prompts/p1-budget.txt`)

Cost per quarter = hires on the team so far x yearly salary / 4.

| Team | Hires on team Q1..Q4 | Per hire per quarter | Q1 | Q2 | Q3 | Q4 | Year |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Engineering | 2, 3, 6, 6 | 30,000 | 60,000 | 90,000 | 180,000 | 180,000 | 510,000 |
| Sales | 1, 3, 3, 4 | 20,000 | 20,000 | 60,000 | 60,000 | 80,000 | 220,000 |
| Support | 0, 1, 2, 4 | 13,750 | 0 | 13,750 | 27,500 | 55,000 | 96,250 |
| Total | | | 80,000 | 163,750 | 267,500 | 315,000 | **826,250** |

Checks on camera:
- Every cost cell holds a formula (click a cost cell, read the formula bar).
- Status column is a dropdown with exactly Planned, Approved, On hold.
- Range question "Why is Q3 so much higher than Q2?": Q3 - Q2 = **103,750** = Engineering +90,000 (three new hires x 30,000) + Support +13,750 (one new hire), Sales +0.
- Move Engineering's 3 Q3 hires to Q4: Engineering becomes 60,000 / 90,000 / 90,000 / 180,000 = 420,000. Q3 total 177,500, Q4 total 315,000 (unchanged), year **736,250**, a drop of exactly **90,000**.
- Bar chart: four bars, heights 80,000 / 163,750 / 177,500 / 315,000 after the move.

## Test 2: messy invoices (file `files/conference-invoices.csv`, prompt `prompts/p2-invoices.txt`)

13 lines, 12 invoices. Planted: INV-102 appears twice; INV-103's amount is the text "$1,450".

- Removed: 1 row (the second INV-102). Fixed: INV-103 to 1,450.
- Total of all invoices **18,715**. Paid **6,865** (INV-101, 106, 109). Still owed **11,850**.
- Budget remaining from 20,000: **1,285**. (Had the duplicate stayed: 21,915, i.e. 1,915 over budget.)
- By vendor: Venue Hall 8,500; Catering Co 4,350; AV Rentals 2,350; Print Shop 505; Badge Makers 550; Speaker Travel 2,460.
- Overdue on Nov 11, 2026 and unpaid: **4 invoices**, INV-102 (3,200), INV-104 (380), INV-108 (900), INV-110 (1,840) = **6,320**. INV-101 is past due but paid: must NOT be highlighted.

## Test 3: whiteboard (prompt `prompts/p3-board.txt`)

10 items, 4 people plus "Everyone":
| Owner | Task | Date |
| --- | --- | --- |
| Priya | Closed beta | Jan 19 to Feb 9 |
| Maya | App store screenshots | Feb 6 |
| Leo | Launch email | Feb 13 |
| Leo | Book three podcast interviews | Feb 16 |
| Maya | Demo video | Feb 18 |
| Sam | Fix beta bugs | Feb 20 |
| Priya | Submit app for review | Feb 23 |
| Sam | Help center | Feb 25 |
| Leo | Schedule launch posts | Feb 27 |
| Everyone | Launch day call | Mar 2 |

Dependencies (exactly 3 arrows asked for): screenshots -> launch email; beta -> bug fixes; bug fixes -> submit for review.
Checks: all 10 on the board with the right owner and date, grouped by person, on a timeline, the 3 links present, no invented dates on my tasks.
- Gaps question: Claude's additions must be marked apart from my tasks (help center says it adds suggestions "for you to check").
- Project plan: all 10 tasks, owners and dates carried over unchanged; the 3 dependencies kept.

## Test 2b: my own edit (added 2026-11-11 before the test take)
I type "Paid" over INV-110's status by hand. Live formulas must give: paid 8,705; still owed 10,010; overdue amount 4,480 (3 invoices); budget remaining unchanged 1,285; INV-110 no longer highlighted.
