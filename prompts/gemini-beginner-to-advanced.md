# Gemini Beginner to Advanced: the prompt pack (AI Walkthru, October 2026)

Every prompt from the video, in the order you see it, with the answer-key check for each one. The running project is a made-up newsletter, Maple Court Neighbor News, for 14 homes on a Denver cul-de-sac. Swap in your own street, club or class.

Tested on 2026-10-08 and 2026-10-09 on a Google AI Pro account. Plans, limits and menu names change, so check what your own plan includes at gemini.google/subscriptions.

How to use it: open gemini.google.com on a laptop or desktop, copy a prompt, change the details to yours, and compare the answer with the check under it. Gemini fills gaps with guesses, so every check below is something you can verify in about a minute.

---

## Level 1: Beginner

**Step 1. Pick your plan.** No prompt. Read the public plans page (gemini.google/subscriptions) and match it to what you need. Everything in the video ran on Google AI Pro.

**Step 2. The screen and the model picker.** Same question on each model, to compare speed:
```
Explain in two sentences what a block party permit is.
```
Check: all four answers (3.5 Flash-Lite, 3.8 Flash, 3.1 Pro, Pro with Extended thinking) were two correct sentences. Speed order in the video: Flash-Lite about 2 s, Flash about 4 s, Pro about 7 s. Your times will differ.

**Step 3. Your first good prompt (MISTAKE #1).**
The vague prompt, to see what goes wrong:
```
write a newsletter
```
Check: you get a question back, not a newsletter, because you gave it nothing.

The four-part prompt (role and task, context, format, limit):
```
You are the editor of Maple Court Neighbor News, a one-page newsletter for 14 homes on a Denver cul-de-sac. Write the October issue. Include: block party Saturday Oct 17 from 2 to 6 pm in the cul-de-sac, bring a side dish, the HOA pays for the drinks; leaf pickup on Oct 24; a welcome to the new family at number 9. Format: a title, three short sections with bold headings, a friendly tone, under 150 words, end with one question for neighbors.
```
Check: all three facts with the right dates and times, three bold headings, 150 words or fewer, and it ends with a question. In the video it passed (127 words) but added a guess ("by 8 a.m.") that was not in the prompt. Read what it adds.

**Step 4. Teach Gemini about you.** Settings (gear) > Personal Intelligence > Instructions for Gemini > Add:
```
Always answer in under 60 words and end with: Anything else, neighbor?
```
Test it in a new chat:
```
What is a block party permit?
```
Check: under 60 words and ends with "Anything else, neighbor?" (54 words in the video). Delete the instruction when you are done testing, or keep one you really want.

**Step 5. Upload a file and a photo.** Plus (+) > Upload files, then:
```
Read this quote from a party rental company for our block party. Check the math line by line. Is the total correct?
```
Check (a quote with a planted error): tables 6 x $18 = $108, bounce house $145, pizza 8 x $12 = $96, cleanup $35. The correct total is $384. The quote printed $394, so a correct answer flags the $10 difference.

With a photo of a notice board:
```
Describe what you see in this photo. Then write a one-line sign for our block party that would fit on this kind of notice board.
```
Check: the description matches what is visible. The sign in the video invented a time ("4 PM") that the prompt never gave.

**Step 6. Temporary chat (MISTAKE #2: what not to paste).** Click the dashed temporary-chat icon, top right, then:
```
Write a one-line welcome note for the Maple Court block party. Our made-up Wi-Fi password is EXAMPLE-ONLY-1234.
```
Check: Gemini repeats the password in the note. Lesson: do not paste passwords, ID numbers or client files into any chat, even a temporary one. Use made-up values like this one for tests.

**Step 7. Check the answer (MISTAKE #3: trusting the first answer).**
```
What do I need to do to close a residential street for a block party in Denver?
```
Check: hover a source chip, open View sources, and open the official city page. In the video the answer cited the city (official), a private blog and a different city. Confirm each claim on the official page: residential streets only, a petition signed by about 75 percent of impacted residents, and a request at least five working days ahead. Treat any claim only a blog or another city supports as unconfirmed.

---

## Level 2: Intermediate

**Step 8. Gemini in Google Docs.** Open a blank doc, then the Ask Gemini side panel:
```
Write a short, friendly intro for the October issue of Maple Court Neighbor News, a newsletter for 14 homes on a Denver cul-de-sac. Mention the block party on Saturday Oct 17 from 2 to 6 pm in the cul-de-sac, bring a side dish, the HOA pays for the drinks. One paragraph, under 80 words.
```
Follow-up (comes back as a suggestion you can accept or reject):
```
Make it warmer, and add one sentence welcoming the new family at number 9.
```
Check: date, time, side dish and HOA drinks are all there. In the video Gemini ignored "one paragraph" and added headings and a details table, and invented "lawn chairs".

**Step 9. Gemini in Google Sheets.** Make a sheet of 12 made-up subscribers (Name, Street number, Email at example.com, Joined month), then ask in the side panel:
```
Summarize this subscriber list in two sentences.
```
```
Write a formula that counts how many neighbors joined in each month, and put the counts in a small table in column F.
```
Check (computed from the typed data before asking): Jan 2, Feb 3, Mar 2, Apr 1, May 1, Jun 1, Oct 2, total 12. The formula in the video was `=COUNTIF(D$2:D$13, F2)`. Do not click Insert on the formula explanation after the table is built: it pasted a second, raw-markdown copy.

**Step 10. Deep Research.** Plus (+) > More tools > Deep research:
```
How do small neighborhood newsletters get neighbors to contribute and keep it going for years? Give me the 5 practices that work, with sources.
```
Edit the plan, then:
```
Looks good. Please make sure at least one source is a real neighborhood or town newsletter.
```
Check: a report with at least 5 practices and a Sources list, and you open at least one source yourself. It took about 4.5 minutes in the video.

**Step 11. Canvas.** Plus (+) > More tools > Canvas, and paste the Step 3 four-part prompt. Select one paragraph and use the Describe changes box:
```
Make this paragraph funnier and mention that the pizza will not last long.
```
Check: only that paragraph changed. The video's edit invented "a stack of pizzas" paid for by the HOA. Re-read edits.

**Step 12. Build an app in Canvas.**
```
Build an RSVP counter app for the Maple Court block party: a name field, an RSVP button, a list of the neighbors who said yes, and a running total that starts at 0.
```
Check (test it yourself): add three names and press the button three times. The total must read 3 and the list must show three names. In the video the app headline had an invented date ("July 4th").

**Step 13. Guided Learning.** Plus (+) > More tools > Guided learning:
```
Teach me to write great newsletter headlines.
```
Then: `Let's start with Critique and Rewrite.` and `Quiz me with one multiple-choice question to check what I learned.` Check: it asks guiding questions one step at a time instead of dumping an answer. The interactive quiz widget failed once; the fallback button "Try again without interactive quiz" worked.

**Step 14. Gemini Notebook.** Create a notebook, add your Deep Research report as pasted text, then:
```
Create an Audio Overview of my sources.
```
Check: on this account it returned a text transcript, not audio.

**Step 15. Create an image.** Plus (+) > Create image:
```
Create a wide banner image for a newsletter called "Maple Court Neighbor News" with colorful fall leaves and a small cul-de-sac with houses.
```
Then edit it: `Make the sky sunset orange.`
Check: the title is spelled right. The video's image also printed an invented line ("AUTUMN 2024 ... VOL. 14, ISSUE 9"). Any text inside an image needs proofreading.

**Step 16. Create a video.** Plus (+) > Create video:
```
A single orange maple leaf blows across a quiet suburban cul-de-sac in autumn, golden hour light, cinematic.
```
Check: about 5 minutes for a 10-second 720p clip in the video, no limit message on Google AI Pro. Limits depend on your plan.

**Step 17. Create music.** Plus (+) > Create music:
```
A 25 second upbeat, cheerful acoustic jingle for a neighborhood block party, with handclaps and a happy whistle.
```
Check: it failed three times in the first session and worked on a later retry (133 seconds), but the track came back 1:07 long, not 25 seconds.

---

## Level 3: Advanced

**Step 18. Build a Gem.** Gems page > New Gem. Name: `Newsletter Editor`. Description: `Writes each Maple Court issue in our house style.` Instructions:
```
You are the editor of Maple Court Neighbor News, a one-page newsletter for 14 homes on a Denver cul-de-sac. Follow the attached style guide. Write in a friendly tone, keep every issue under 150 words, use exactly three short sections with bold headings, and always end with one question for the neighbors.
```
Add a short style-guide file as knowledge, Save, then ask:
```
Write the November issue: leaf pickup is done, and a thank-you to the 4 volunteers.
```
Check: three bold headings, under 150 words, ends with a question (98 words in the video). It invented four volunteer names and a December event. Google's banner says Gems start migrating to skills on Nov 17, 2026.

**Step 19. Create a skill.** Settings > Skills > Create manually. Name: `maple-issue`. Description:
```
Use when asked to write an issue of the Maple Court Neighbor News. Starts running on prompts like "write the November issue".
```
Instructions: the same rules as the Gem, without the file. Then in a new chat type `/`, choose maple-issue and send the same November prompt.
Check: same key as Step 18. The skill answer had headings but not bold ones, and it did not invent an event.

**Step 20. Scheduled action.** Settings > Scheduled actions > New action. Name `Friday neighbor news`. Instructions:
```
Every Friday at 8 am remind me to collect neighbor news for Maple Court Neighbor News
```
How often: Weekly, Friday. Deliver by 8:00 AM. Check: it appears in My actions with an ON switch. Delete test actions so they do not fire.

**Step 21. Connected apps.** Settings > Personal Intelligence > Connected Apps, and type `@` in the composer to see what you can call. Check what is already switched on before you rely on it. Do not connect an app you do not need.

**Step 22. Gemini Spark (MISTAKE #4: an agent on sensitive data).** Switch to Spark in the sidebar and read Spark Settings first. Check: Spark browses and runs code for you, and it can act in the Workspace apps that are switched on. Start with a throwaway account or one small folder, and review what it does. The video did not run a task.

**Step 23. Daily brief.** Open it from the rail and read the intro first: it pulls from Gmail and Calendar. Only press Generate now if you are happy for it to read your inbox.

**Step 24. Scorecard.** What worked, what slipped, and what was not tested are in the video. Not tested: Gemini Live (not on the web in this test), the Chrome side panel, and the Mac and Windows apps.

---

## The four mistakes

1. **Your first prompt.** A vague request gets a vague answer. Give role and task, context, format and a limit.
2. **What not to paste.** No passwords, ID numbers or client files in any chat, even a temporary one.
3. **Trusting the first answer.** Open the sources and confirm the key claims on the official page.
4. **An agent on sensitive data.** Do not let an agent loose on your real inbox or folders. Start small and review.

## Your 10-minute checklist

1. Pick a plan.
2. Write four-part prompts.
3. Add one instruction.
4. Check the sources.
5. Use Docs and Sheets.
6. Try Deep Research.
7. Make one Gem or skill.

---

Tested on 2026-10-08 and 2026-10-09 on a Google AI Pro account. Plans, limits and menu names change.
