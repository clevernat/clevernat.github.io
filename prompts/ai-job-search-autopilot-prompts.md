# AI Job Search Autopilot: the 5 prompts (claude.ai, no coding)

From the AI Walkthru video "How to Automate Your Job Search With Claude AI". Tested live on claude.ai on 5 November 2026 with a fictional CV.
Swap in your own job titles, years, city and companies.

## Step 1: Make the project
claude.ai → Projects → New project. Name it "Job Search Autopilot". Paste this into the description, then click Add context and pick your CV (PDF), then Create project.

> Run my job search. Find Data Analyst, Product Analyst or Business Analyst jobs that need 2 to 5 years of experience, remote in the US or in New York City. Skip any title with Senior, Lead, Staff or Principal. Use only facts from my CV. Never apply or submit anything.

## Step 2: Find real jobs (send in the project)
> Find real open jobs for me. Use only the rules and the CV in this project, and use web search and web fetch, not the browser. Check the career pages of these 15 companies: Stripe, Brex, Coinbase, Reddit, Datadog, Robinhood, Affirm, Ramp, Vanta, Notion, Airtable, Duolingo, Squarespace, HubSpot and Plaid.
> Keep only jobs that pass my rules. Open each posting and check the title, location, years of experience and salary (write "not listed" if there is none). Show me a table with the link to each job.

Why the two lines: without "not the browser", Claude may try Claude in Chrome and stop to ask which browser to use. Without "only the rules and the CV in this project", it may read old notes from your account memory.

## Step 3: Widen, score, build a tracker
> One job is too few. Widen my rules a little: also include Analytics, Strategy, Operations and Finance analyst titles, and Senior titles if they ask for 5 years or less.
> Score every job from 1 to 10 against my CV, with one reason it fits and one gap. Then build me a job tracker as an artifact: every job sorted by score, with a status for each one (New, Applied, Interview).

Check every link yourself. In the test, 2 of the 9 jobs in the tracker were already closed.

## Step 4: CV and cover letter for the top job
> For the top job, write a one-page CV and a short cover letter. Use only facts from my CV. Never invent skills, tools or numbers. At the end, list any requirement I don't meet.

## Step 5: Put it on a schedule (paid plans)
> Now make this run by itself. Every weekday at 7 a.m., check the same 15 companies for new jobs that pass my wider rules, score them against my CV, and give me a short list: title, company, score and link. Never apply or submit anything.

See it, pause it or run it now: sidebar → Scheduled.

Rule of thumb: let Claude do the searching and the first drafts. You do the checking and the applying.
