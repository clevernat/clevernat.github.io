# Claude job search: 4 prompts + a criteria template

From the AI Walkthru video "I Let Claude Run a Job Search, Then Checked Every Answer".
Tested on claude.ai (Projects, web search, Claude in Chrome, Scheduled tasks), October 2026.

Ground rules that made this work:
- Claude researches, filters, tailors and pre-fills. **You** read it, attach your files, answer the personal questions and press **Submit**.
- Indeed's terms prohibit automating Indeed Apply, and LinkedIn's User Agreement bans bots and plugins that automate its site. Don't let any AI auto-submit there.
- Check the jobs yourself. In our test Claude said 8 of 10 jobs met every rule; the pages showed 5.

---

## 0. The criteria file (save as `job-criteria.md` and add it to your project)

Write rules you can check, not wishes. "2 to 5 years" can be checked; "mid-level" can't.

```
# My job criteria

- Roles: [Product Analyst, Data Analyst, ...]
- Level: [2–5] years of experience required. No [Senior, Lead, Manager, Principal, intern] roles.
- Location: [City] metro (on-site or hybrid) or fully remote in [country]
- Salary: [$85,000] or more (if no salary is listed, keep it but flag it)
- Full-time only. No contract, temp or staffing-agency postings.
- Posted in the last [14] days
- Work authorization: [e.g. US citizen, no sponsorship needed]
- Rule: never invent experience, tools or numbers that are not in my resume.
- Rule: never submit an application or create an account without asking me first.
```

## 1. The project (setup, not a prompt)

In Claude: **Projects → New project**.
- Name: `Job Hunt - [your name]`
- What are you trying to achieve: `Find [role] jobs that fit my resume, keep a tracker of every job, and prepare tailored resumes and cover letters. Never invent experience. Never submit anything without my OK.`
- Add context: your resume (PDF) and `job-criteria.md`.

## 2. Search prompt

```
Use my resume and job-criteria file in this project. Search the web (Indeed, LinkedIn, Built In and company career pages) for up to 10 real job postings that fit me, posted in the last 14 days. Only include jobs that meet every rule; if fewer fit, give me fewer.
For each job give: company, job title, location / remote, salary if listed, years of experience asked for, the link, and a fit score from 1 to 10 with one line on why.
Check every job against my criteria. List anything you rejected and the rule it broke.
Then put the jobs in a tracker spreadsheet with a Status column set to "Not applied", and save the tracker in this project.
```

"Up to 10" matters: when we asked for exactly 10, Claude padded the list with near misses.

## 3. Tailoring prompt

```
Let's do #[number], the [company] [job title] job. Open the posting first.
Then make me a tailored one-page resume and a short cover letter for it, as Word files.
Use only facts from my resume: no new tools, numbers, titles or degrees.
At the end, list every change you made and the resume line it came from.
```

## 4. Application prompt (Claude in Chrome, paid plans)

```
Apply step for the [company] [job title] job: [link]
Use Claude in Chrome on my browser and open a new tab.
Click through to the real application form and fill it in with my details from my resume.
Do NOT click Submit, and don't create an account. If something needs my files, a login, or a personal question like salary, EEO or work hours, stop and list it for me.
When you're done, tell me exactly what you filled, what you left blank, and why.
```

Then read the form yourself, attach your files, answer the personal questions and press Submit.

## 5. Scheduled task (optional)

Project page → **Scheduled → Add**. Name: `Morning job scan`. Frequency: Weekdays, 07:00.

```
Search Built In, Indeed and company career pages for new jobs that match my resume and job-criteria file, posted since the last run. Check each one against my rules, add only new ones to the job tracker with Status "Not applied", and give me a 5-line summary. Never apply, never create accounts, never submit anything.
```

Delete the task when your search is over.
