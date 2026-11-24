# ChatGPT vs Gemini vs Claude: the six everyday jobs (AI Walkthru test pack)

From the video "ChatGPT vs Gemini vs Claude: I Tested the New Models on 6 Real-Life Jobs" (AI Walkthru, November 2026).

## How I ran it

- Same prompt and same files in every app. One run each. No follow-up messages.
- A private chat in each app: ChatGPT **Temporary chat** with **Personalization: Unpersonalized**; Gemini **temporary chat**; Claude **incognito**.
- Each app on Medium: ChatGPT **Chat** tab, **GPT-6.2**, **Thinking effort: Medium**; Gemini **4 Neon** ("Deeper analysis"), **Thinking level: Medium**; claude.ai **Fable 5.2**, **Effort: Medium**.
- Time from pressing Send to the moment the app stops writing.
- Every document in the test files is made up. No real person, company or account.

## The prompts

### Job 1: why did my electric bill jump?

Attach: northfield-bills.pdf

```
These are my last two electric bills. Why did my October bill jump so much? Break down exactly where the extra money came from, with numbers.
```

### Job 2: what am I owed?

Attach: order-confirmation.pdf, packing-slip-photo.jpg, bank-statement.png

```
I ordered from Brightwell Home. Here's the order confirmation, the packing slip that came in the box, and my card statement. Cross-check them: was I charged correctly? Tell me exactly how much I'm owed, then write a short refund request I can send.
```

### Job 3: leaving my lease three months early

Attach: maple-grove-lease.pdf

```
This is my lease. I need to move out at the end of May 2027 instead of when the lease ends. What will it cost me in total, what exactly do I have to do, and by what date? Point me to the sections.
```

### Job 4: who owes whom after the cabin weekend

No files.

```
Help me settle up after our cabin weekend. Five of us: Ana, Ben, Cleo, Dev, Eli.
- Ana paid the cabin, $900, split by all 5.
- Ben paid groceries, $240, split by all 5.
- Cleo paid gas, $90, split by Cleo, Dev and Eli (they rode in her car).
- Dev paid ski passes, $360, for Ana, Ben and Dev only.
- Eli paid dinner, $150, split by everyone except Ben (he skipped dinner).
- Ben already sent Ana $100.
Who pays whom, and how much? Use as few payments as possible and show your math in a table.
```

### Job 5: last day to return Black Friday gifts (needs web search)

No files.

```
I live in Illinois. On Black Friday (Nov 27, 2026) I'm buying gifts: AirPods Pro 3 ordered on apple.com (delivered Nov 30), a DJI drone for $599 at a Best Buy store, Beats headphones at Target, and a LEGO set at Target. No store memberships. If someone wants to return a gift, what's the last day to return each one, and are there any fees? Link each store's own policy page.
```

### Job 6: the trap round (same lease)

Attach: maple-grove-lease.pdf

```
Quick questions about my lease:
1. I'm getting a dog next month. How much is the pet deposit?
2. My friend says the security deposit comes back within 14 days of moving out. Right?
3. Can my security deposit just cover my last month's rent?
4. If I stay until the lease ends, by what date do I have to tell them I'm leaving?
5. What happens if I forget to tell them?
```

## The answer key (written before any run)

## Job 1: why did my electric bill jump? (testdata/northfield-bills.pdf, two monthly bills)
September bill 133.33, October bill 224.76.
1. The total rise is 91.43 (133.33 to 224.76).
2. A 35.00 late fee: September's payment posted Sep 30, due Sep 25.
3. The energy rate went up from 14.2 to 15.8 cents per kWh (about 13 dollars of the rise on 812 kWh).
4. Usage went up 172 kWh (640 to 812), but the October period is 33 days against 29: per day 22.1 to 24.6 kWh, about 11 % more.
5. A new Grid Modernization Rider of 9.80.

## Job 2: what am I owed? (order-confirmation.pdf, packing-slip photo, bank-statement screenshot)
Correct total 197.30. Charged 213.81, plus a second charge of 26.74.
1. Coupon COZY20 was not applied to the table lamp: 8.00 (8.56 with tax).
2. Shipping 7.95 was charged; the order said free shipping over 75.
3. The towel set was charged twice: 26.74 extra on Nov 4.
4. Total owed 43.25 (16.51 + 26.74). Accept 42.69 only as a near miss (no point).
5. A refund request that names the order number BW-482917 and lists the three items with amounts.

## Job 3: leaving the lease three months early (maple-grove-lease.pdf, 6 pages)
Rent 1,850; lease ends Aug 31, 2027; leaving May 31, 2027.
1. Notice: 60 days, written, so by April 1, 2027.
2. How: certified mail or the resident portal; email is not accepted (14.5).
3. Early termination fee 3,700 (two months' rent), paid with the notice (14.3).
4. Hidden costs: repay the free-month concession 1,850 (3.5), re-letting fee 350 (22.6), cleaning 175 (19.4).
5. Total 6,075 on top of rent through May.

## Job 4: who owes whom after the cabin weekend (typed in the prompt, no files)
Owed shares: Ana 385.50, Ben 348.00, Cleo 295.50, Dev 415.50, Eli 295.50 (sum 1,740 = paid).
1. Ana is owed 414.50 once Ben's 100 is counted.
2. Cleo pays Ana 205.50.
3. Eli pays Ana 145.50.
4. Dev pays Ana 55.50 and Ben pays Ana 8.00.
5. Four payments in all (the fewest possible), and the totals add up.

## Job 5: last day to return my Black Friday gifts (web search, store pages)
Bought Friday Nov 27, 2026 in Illinois; AirPods ordered on apple.com and delivered Nov 30; no store memberships.
1. AirPods Pro 3 (apple.com, received Nov 30): by Jan 8, 2027, no fee (Apple Holiday Return Policy).
2. DJI drone (Best Buy store, Illinois): by Jan 15, 2027 (extended holiday period).
3. The drone has a 15 % restocking fee if opened: 89.85 on 599 (Illinois is not exempt).
4. Beats headphones (Target): by Jan 8, 2027 (Apple and Beats: 14 days from Dec 26), not Jan 24.
5. LEGO set (Target): 90 days, so by Feb 25, 2027; and a link to each store's own page.

Sources for job 5 (read 2026-11-24): apple.com/shop/help/returns_refund (Holiday Return Policy: received Nov 6 to
Dec 25, 2026, returnable through Jan 8, 2027); bestbuy.com return-exchange-policy (purchases Oct 30 to Dec 31 through
Jan 15, 2027; drones 15 % of purchase price; no fee if unopened or in AL, CO, HI, IA, MS, OH, OK, SC); target.com
help article 000088565 (Nov 1 to Dec 24 purchases; electronics by Jan 24, 2027; Apple and Beats by Jan 8, 2027) and
Target's standard 90-day policy.

## Job 6: the trap round (same lease, five quick questions, written 2026-11-24 before the run)
1. Pet deposit: the lease names NO pet deposit. A dog needs a signed Pet Addendum; an unauthorized pet costs 250 plus cleaning or repairs (8). An answer that gives a deposit amount fails.
2. "14 days" is wrong: the deposit comes back within 30 days, less lawful deductions, with an itemized statement (4.2).
3. No: the deposit may not be applied to the last month's rent (4.3).
4. Written notice at least 60 days before Aug 31, 2027: by July 2, 2027 (2.2).
5. The lease continues month to month at the then-current rate (2.2).
