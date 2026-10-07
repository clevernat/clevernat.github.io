# ChatGPT Beginner to Advanced — cheat sheet (AI Walkthru, October 2026)

Every prompt from the video, in the order you see it. The running example is a made-up business, Kofi's Bike Repair in Denver. Swap in your own business, class or project.

Filmed on ChatGPT Plus in October 2026. Check what your plan includes at chatgpt.com/pricing.

---

## Level 1: Beginner

**1. The vague prompt (to see what goes wrong)**
```
write an ad for my bike repair business
```

**2. The four-part prompt: role, context, task, format**
```
You're a friendly local copywriter. I run Kofi's Bike Repair, a mobile bike repair service in Denver. We come to you.
Write 3 versions of a short ad for these services with their exact prices: Flat fix $20, Basic tune-up $65, E-bike check $85.
Keep each version under 40 words and end with a call to book.
```

**3. Read a photo or file** (+ → Add photos & files)
```
Turn this receipt into a table and check the maths.
```

**4. Follow up in the same chat**
```
Draft a short, polite email to the supplier asking for a refund of the difference.
```

**5. Edit, regenerate, branch.** Hover your message and click the pencil to edit it. Use Regenerate → Try again for another version. Use ⋯ → Open new branch to try a new direction (in Chat or Work).

**6. Search the web** (+ → Web search)
```
What do bike shops in Denver charge for a basic tune-up right now? Give me a price range with sources.
```

**7. Create an image** (+ → Create image)
```
Make a square flyer for Kofi's Bike Repair. Headline: "We come to you." Denver mobile bike repair. Basic tune-up $65. Bright, clean, modern.
```

**8. Voice mode.** Click the voice button and just ask, for example: "What is one quick check I should do on my bike before every ride?"

---

## Level 2: Intermediate

**9. Custom instructions** (Settings → Personalization → Custom instructions → ChatGPT)
```
I run Kofi's Bike Repair, a mobile bike repair business in Denver. Use plain English and US dollars. Keep answers short. Put any numbers in a table.
```

**10. Project instructions** (Projects → + → Create project, then Project settings)
```
You help me run Kofi's Bike Repair, a mobile bike repair business in Denver. Use the files in this project as the source of truth. Show your numbers and keep answers short.
```
Then add your files under **Sources → Add sources → Upload**, and ask:
```
Which service made the most money, and which week was the worst?
```

**11. Charts and analysis** (same project chat)
```
Chart weekly revenue and tell me 3 trends you see.
```
Then always ask one more question:
```
Break it down by service. Which services are growing and which are shrinking week to week?
```

**12. Deep research** (+ → Deep research)
```
What licenses or permits does a mobile bike repair business need to operate in Denver, Colorado? Include costs and official links.
```
Check the citations it gives you before you act on them. It is not legal advice.

**13. Study and flashcards**
```
Help me study how bike gear ratios work. Teach me step by step, and quiz me one question at a time.
```
```
Make 5 flashcards on gear ratios so I can review later.
```

**14. Write a document** (in your project)
```
Write a one-page service guide for Kofi's Bike Repair customers: what each service includes, how long it takes, and the price. Use the price list in this project.
```
Open the editor, select one line, click **Ask for changes**, and type what you want.

**15. Reuse a file from your Library** (+ → Add from library)
```
Which line on this receipt cost the most?
```
Then ask it to check the maths. In our test it repeated the receipt's mistake.

---

## Level 3: Advanced

**16. A skill** (Plugins → Skills → Add → Create with editor). Name: `kofi-quote`. Instructions:
```
When I ask for a quote for Kofi's Bike Repair:
1. Use these prices: Flat fix $20, Basic tune-up $65, Brake service $45, E-bike check $85, Full overhaul $180.
2. Travel is free within 5 miles. After that, add $1 for every mile beyond 5.
3. Show a short table with each line and the total.
4. End with: Quote valid for 14 days.
```
Use it **in Work mode**. In our test, normal Chat did not load the skill:
```
Use my kofi-quote skill: quote a basic tune-up plus a brake service for a customer 8 miles away.
```

**17. Work: a pitch deck** (switch to Work and attach your files with + → Add photos & files)
```
Make a 5-slide pitch deck for Kofi's Bike Repair. We want to sell a monthly bike-fleet service to Denver offices with shared bikes. Use the jobs log and price list for real numbers.
```

**18. Work: a website**
```
Now build a one-page website for Kofi's Bike Repair: a headline, the five services with prices from the price list, the free travel within 5 miles, and a big "Book a repair" button. Don't publish it.
```

**19. Work: fetch information from a website**
```
Open Denver's official city website and find the peddler license page. Tell me the license fee and the steps to apply. Do not fill in or submit anything.
```

**20. A scheduled task**
```
Every Monday at 8am, send me 3 short bike-maintenance tips I can post for my customers.
```
Find it in the sidebar under **Scheduled**. You can pause, edit or delete it there.

---

**Remember:** in our tests ChatGPT slipped four times. It missed two trends until we asked again, it copied a maths error from a receipt, it ignored a skill in Chat mode, and Work missed the project files until we attached them. Check every number that matters.
