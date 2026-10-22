# NotebookLM (Gemini Notebook) beginner to advanced: prompt pack

From the AI Walkthru video "NotebookLM Tutorial: Beginner to Advanced (New Gemini Notebook, 2026)". Tested on a Google AI Pro account on October 21, 2026, at notebook.google.com (notebooklm.google.com now redirects there). Plans, limits and menu names change, so some steps may look different on your account.

**The running project:** Juniper Lane Books, a fictional bookshop deciding whether to start a monthly book club. Swap in your own project: a class, a business decision, a trip, a research topic.

**Do this on a laptop or desktop.** Never upload passwords, client files or anything private you would not want stored in your Google account.

---

## Beginner (steps 1-8)

1. **Find the new name.** Go to notebook.google.com. NotebookLM is now called Gemini Notebook.
2. **Create a notebook.** Click New notebook, then Add sources, then Upload files. Rename the notebook by clicking its title.
3. **Add every kind of source.** Add sources > Websites (paste several links, one per line; YouTube links work, it reads the transcript), Copied text (paste notes), and Upload files for PDFs.
4. **Read the source guide.** Click any source to see its summary and key topics.
5. **Ask your first question** (check the citations, hover the small numbers):

   > How many customers said they would join the book club, and which night and time do most of them want?

6. **Make it do the maths**, then add it up yourself:

   > Add up our monthly sales from January to September 2026. What is the total, and which month was the best?

   Answer key: $373,000, best month September ($46,500).

7. **Notes.** Save to note under an answer (saved answers are view only). Add note for your own thoughts, then **Convert to source** so the chat can use it.
8. **First Audio Overview.** Studio > Audio Overview > Deep Dive > Generate. Expect it to be generic: ours drifted into book-club history.

## Intermediate (steps 9-16)

9. **Discover sources on the web** (sources panel search box, Web + Fast Research). Untick sales pages, forums and anything you would not cite before you click Import:

   > how independent bookstores run successful book clubs

10. **Choose which sources answer.** Untick Select all, tick one source, then ask:

    > Using only this survey, what should the first book club pick be, and why?

11. **Configure the chat.** ⋮ > Configure Chat > Custom, Response length: Shorter. Our role:

    > You are a careful small-business advisor for an independent bookshop. Answer in plain English, give one clear recommendation first, then the numbers from the sources that support it, and say when the sources disagree.

    Then ask:

    > Should we launch the book club, and what fee should we charge?

    Check its maths. It told us a $5 fee covers staff and coffee at 15 people: 15 × $5 = $75, but $38 staff + 15 × $3 coffee = $83. It's $8 short.

12. **Audio Overview done right.** Pick Debate, length Short, and steer it:

    > Debate one question: should Juniper Lane Books launch a monthly book club in January? Use the survey and sales numbers. One host argues for Thursday, the other for Tuesday.

13. **Mind Map.** Studio > Mind Map, then Expand and open branches with the arrows.
14. **Reports.** Interactive (new) or Document. Interactive mixes in other Studio items.
15. **Flashcards.** One click. Mark Got it / Missed it.
16. **Quiz.** Fewer questions, Hard, and a topic:

    > Test the numbers a shop owner needs: demand, best night, fees, costs and room size.

## Advanced (steps 17-24)

17. **Deep Research.** Fast Research menu > Deep Research:

    > What makes a bookstore book club last more than a year? Fees, group size, meeting night and book length.

    It imports everything it found. Read the list and delete what you would not cite. Trace any striking statistic back to its source.

18. **Ask what your sources can't answer:**

    > How much did members pay at our last book club meeting?

    A good notebook says the sources don't contain it.

19. **Infographic.** Portrait, Professional style, Standard detail:

    > One page for the shop counter: why Juniper Lane is starting a book club, Thursday 7 pm, a $5 fee, 30 seats, and the top genre.

    Proofread every line before you print it.

20. **Slide Deck.** Presenter Slides, Short:

    > A 6-slide pitch to the staff: the survey results, the costs per meeting, the two open questions (night and room size), and the January launch plan.

    Check the small print (we found garbled side labels), and use Revise to fix a slide.

21. **Video Overview.** Explainer, custom topic:

    > Explain to a new staff member why Juniper Lane Books is launching a book club and how the first meeting will run.

22. **Data Table** then More options > Export to Sheets:

    > One row per month from January to September 2026 with sales, and one row per author event with attendance and sales that evening.

23. **Use the notebook in Gemini.** gemini.google.com > + > More uploads > Notebooks > pick it > Add:

    > Using my Juniper Lane notebook, write a short email to our staff announcing the book club: night, time, fee, and the two questions we still need to settle.

    Read the draft before you send it. Ours changed the fee to free and forgot the room-size question.

24. **Share.** Share > Notebook Access: Restricted, Anyone with a link, or Public. Settings has Output language, Remove watermarks and Usage.

---

## Test data (so you can follow along)

**Owner notes (paste as Copied text):**

```
Notes from Dana (owner), October 2026

I think Tuesday is our best night for the book club. Tuesday is our slowest evening, so a club would bring people in when we need them most.

The back room holds 40 people, so we have plenty of space even if the club is popular.

Fern & Kettle, the cafe next door, offered to bring coffee and pastries for $3 per member.

I'd like the first meeting in January 2027, and I want it to feel friendly, not like homework.
```

**Answer key** (written before recording):

Running project: Juniper Lane Books (fictional shop) is deciding whether to launch a monthly book club.
Sources: survey.pdf, sales-notes.pdf, owner notes (copied text), Wikipedia "Book discussion club", one YouTube video.

| Question | Correct answer | Source |
|---|---|---|
| Survey responses | 214 | survey |
| Would join (yes) | 58% (124); maybe 27%; no 15% | survey |
| Best night | Thursday evening 41% (Tuesday only 22%) | survey |
| Start time | 7:00 pm | survey |
| Fee | Free 34%, $5 29%, $10 26%, $15+ 11% -> 66% would pay $5 or more | survey |
| Top genre | Literary fiction 31% | survey |
| Biggest barrier | Not finishing the book in time 37% | survey |
| Total sales Jan-Sep | $373,000 | sales notes |
| Best month | September $46,500; weakest February $35,900 | sales notes |
| Event-night sales vs normal Thursday | events $1,620 / $1,710 / $2,190 (avg $1,840) vs $1,120 | sales notes |
| Average event attendance | (38+44+56)/3 = 46 | sales notes |
| Room | 30 chairs, fire limit 35 | sales notes |
| Staff cost per meeting | 2 h x $19 = $38 | sales notes |
| Coffee | $3 per member from Fern & Kettle | owner notes |

Planted contradictions (advanced step):
1. Night: owner notes say Tuesday is best; survey says Thursday (41%) vs Tuesday (22%).
2. Room: owner notes say the room holds 40; sales notes say 30 chairs and a fire limit of 35.

Not-in-sources test: "How much did members pay at our last book club meeting?" -> no club has been held; the sources do not say.

