# Google AI job-hunt prompt pack (AI Walkthru, tested 2026-10-09)

Tested in Gemini (Flash, Canvas, Deep Research) and Gemini Notebook, with a fictional person (Jordan Ellis) and an answer key written before recording.
Rule that ran through every step: check the output against your own resume and the real job page. The AI is 80%; you are the other 20%.

## Before you start
- Put your real resume (PDF) and your criteria in one folder. Criteria = job titles, years asked, place, salary floor, full-time only, how recent.
- Write down your own "never invent" list: tools, numbers and titles that are NOT yours.

## Stage 1: find jobs
Attach your resume, then:
```
Use my resume. Find 5 real job postings that fit me, posted in the last 14 days.
My criteria: roles [your titles]. [x] to [y] years of experience asked. [place]. Salary [floor] or more (if no salary is listed, flag it). Full-time only, no contract and no staffing agencies.
For each job give: company, title, location, salary, years asked, the link, and a fit score from 1 to 10 with one line on why.
Then list the jobs you rejected and the rule each one broke.
```
Mistake: "Find me jobs." (no criteria, no links, a Senior role slipped in).
Check: open every link. Years asked, salary city and "remote" were wrong on our list.

## Stage 2: tailor the resume
In Canvas, attach your resume, paste the job description, then:
```
Here is the job description above. Create a customized resume for me for this job. Make it one page.
```
Mistake: this draft invented GA4, dbt, Looker Studio, Power BI and a certification.
Fix:
```
Check every line against my resume. Remove any tool, number or skill that is not in my resume, and list what you removed.
```
Gap check:
```
Which requirements in the job description are missing from my resume? List them. Do not add any of them to the resume.
```

## Stage 3: cover letter
Deep Research:
```
I am applying for the [role] role at [company] (my resume is attached). Research the company: what it does, the brands it runs, recent news from the last 12 months, and how it talks about [the job's topic]. Use the company's own website and press releases as the main sources and cite every claim.
```
Letter:
```
Now write a short cover letter (under 220 words) for the [role] role. Use only facts from my resume and the research above. Do not invent quotes, numbers or events.
```
Check every company claim on the cited page, then add one true personal line.

## Stage 4: interview prep (Gemini Notebook)
Add your resume, the job description, your letter and the company page as sources, then:
```
Act as the hiring manager for this role. Ask me one interview question at a time, based only on my sources. After each answer, rate it from 1 to 10 and tell me what is missing.
```
Test the ratings with a weak answer and a strong answer. Test grounding with a question the sources cannot answer.

Fictional resume and job pages used in the video: Jordan_Ellis_Resume.pdf.
