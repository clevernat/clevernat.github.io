# Grad school autopilot: the exact prompts

From the AI Walkthru video "Automate Your Grad School Applications with Claude AI (Free Prompts)".
Tested on claude.ai (Projects, web search, artifacts, Claude Docs, scheduled tasks) with Opus 5.5 on November 8, 2026.

Ground rules that made this work:
- Claude collects, drafts and reminds. **You** check every date on the official page, decide what is true in your essay, and press send.
- Projects work on the free plan (up to 5). The weekly scheduled task needs a paid plan (Pro or higher).
- In our test: 45 of 48 facts right on the first answer (3 "not found", 0 wrong), 48 of 48 after one follow-up, 0 invented facts in the statement of purpose.

---

## 1. Set up the project (no prompt)

On **claude.ai**: **Projects → New project**.
- Name: `Grad School 2027`
- What are you trying to achieve: `Apply to 8 master's in data science programs for Fall 2027 and track every deadline, letter and essay.`
- **Create project**, then **Add** next to **Instructions** and paste:

```
You are my grad school application assistant. My CV is in this project.
Rule 1: Use only official university pages for requirements, and give the link for every fact.
Rule 2: If a page only shows last year's dates, say so. Never guess a Fall 2027 date.
Rule 3: Never invent anything about me. Use only my CV. If something is missing, ask me.
Rule 4: Keep it short. Use tables when you list programs.
```

- **Add** next to **Context → Upload from device → Files**, and pick your CV (PDF). Leave out your phone number and home address.
- Also add your program list now: **Add → Add text content**, name it `My programs`, and paste each program with its official link. Scheduled tasks can't read chats, only project files.

## 2. Collect every requirement (change the programs to yours)

```
These are the 8 programs on my list for Fall 2027:
Columbia MS in Data Science, Harvard SM in Data Science, UC San Diego MS in Data Science, UVA MS in Data Science (residential), UChicago MS in Applied Data Science (in-person), Duke MIDS, Boston University MS in Data Science, University of Washington MS in Data Science.
For each one, check the official pages and give me: the deadline, the application fee, the GRE policy, how many recommendation letters, the statement of purpose length, and the minimum TOEFL and IELTS.
One table, with the link for every row. Mark any date that is not clearly for Fall 2027.
```

If anything says "not found", send:

```
Yes, please look up the gaps: the Duke and BU application fees, UChicago's GRE policy, and the word limits for UW's two essays.
```

## 3. The tracker (an artifact that saves your ticks)

```
Turn that table into a tracker I can use every day.
Show each program as a card, sorted by deadline, with a countdown in days.
Give each card a checklist: statement of purpose, 3 letters requested, 3 letters submitted, transcript, IELTS score sent, fee paid.
Add one progress bar for everything, and keep my ticks saved when I come back.
```

## 4. Statement of purpose

```
Now write my statement of purpose. Use only facts from my CV.
About 800 words, built around one story from my work.
Then write a short "Why this program" paragraph for each of the 8 programs, naming one real course or lab from its official page, with the link.
At the end, list every sentence about me that is not in my CV.
```

Read the list of sentences that are not in your CV. Keep only the ones that are true for you, in your own words.

## 5. Recommendation letters

```
Write an email to each of my 3 recommenders asking for a letter.
Keep each under 150 words, and add a short brag sheet with 3 points from my CV that fit what they know about me.
Include the list of programs and the earliest deadline.
Then write one short reminder email to send 2 weeks before that deadline.
```

Claude drafts the emails. Nothing is sent unless you send it.

## 6. The weekly check (Scheduled → Add, Weekly, Monday, 8:00)

Name: `Weekly deadline check`. Instructions:

```
Every Monday, check my 8 programs in this project.
List every deadline in the next 14 days, check each program's official page for any change to its deadline or requirements, and tell me the 3 most important things to do this week.
Use only official pages and give the link for every fact.
```

Press **Run now** once to test it. If it says it can't find your programs, add the program list to the project (step 1).

---

Mistakes we hit, so you don't:
1. The first scheduled run failed: the task couldn't see the chat. Fix: save the program list in the project.
2. A run on a Sunday called Monday's deadline "today". Check the date it prints.
3. Some pages show a month and a day with no year. Don't trust those until the school confirms the year.
