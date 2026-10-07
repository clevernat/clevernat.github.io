# Claude from Beginner to Advanced: cheat sheet

Every prompt from the AI Walkthru video, in the order it appears, plus the settings that go with it.
Tested on the new Claude (chat and Cowork merged on September 16, 2026), Sonnet 5.5 unless noted.

Swap "Maya's Coffee Cart" for your own business, class or project.

---

## Level 1: Beginner

### Know your plan
- **Free:** chat on web, desktop and mobile, web search, file creation, memory, connectors, artifacts.
- **Pro** (USD 17 a month yearly, or 20 monthly): more usage, scheduled tasks, Claude Design, Slides and Docs, Projects, more models, Claude in Chrome.
- **Max** (from USD 100 a month): 5x or 20x Pro usage.
- **Limits:** see them in Settings > Usage (current session and weekly limit, with reset times).

### Pick a model
- **Haiku:** fastest, for quick answers.
- **Sonnet:** everyday work (the default).
- **Opus:** complex work.
- **Fable:** the toughest problems, with its own weekly limit.

Use Sonnet by default. Switch to Opus when the answer matters: it is more likely to catch what you forgot to say.

### The four-part prompt: role, context, task, format
```
You're a friendly cafe copywriter. I run a small weekend coffee cart at a Denver farmers market.
Write a menu for these 5 items with their exact prices: Latte 5.50, Cold brew 5.00, Drip coffee 3.00, Chai 4.75, Muffin 3.50.
Give each item a description under 15 words. Format it as a table: item, price, description.
```
Compare it with the vague version: `write a menu for my coffee cart`. The vague one made up drinks and prices.

### Read a photo or file, and check it
Click **+**, then **Add files or photos**. Then ask:
```
Turn this receipt into a table and check the maths. Is anything wrong?
```

### Follow up in the same chat
```
A 5 lb bag of beans makes about 200 drinks. What do the beans cost per drink?
```

---

## Level 2: Intermediate

### Instructions for Claude
Click your name > **Settings** > **Account** > **Instructions for Claude**:
```
I run a small weekend coffee cart in Denver. Use plain English and US dollars. Put any numbers in a small table. Keep answers short, and ask me one question if something important is missing.
```

### Project
Go to **Projects** > **New project**. Add files under **Context**.

Goal:
```
Help me run my weekend coffee cart at a Denver farmers market. Use the sales file and price list as the source of truth, show your maths, and tell me when you are guessing.
```
Then ask:
```
Which item made the most money, and which week was the worst?
```

### Artifact (a small app)
```
Build me an interactive break-even calculator as an artifact.
Inputs: monthly fixed costs, price per cup, cost to make one cup, Saturdays per month.
Show cups needed per month and per Saturday, rounded up. Keep it simple and clean.
```
Test it with numbers you already know the answer to. In the test: 1,200 / 4 / 5.00 / 1.40 gives 334 cups a month and 84 a Saturday.

### Research
Click **+** > **Research**, then:
```
What licenses and permits do I need to run a mobile coffee cart at a farmers market in Denver, Colorado? List each one, who issues it, and the cost if published. Cite official sources.
```
Open two or three of the cited sources and check them.

### Memory
```
What do you remember about my coffee cart?
```
Memory builds up over time. Anything Claude must know goes in your Instructions or in a Project.

### Privacy
- **Settings > Privacy:** the "Help improve our AI models" switch (training on your chats).
- **Incognito:** the ghost icon at the top right.
- **Delete a chat:** open the chat's menu next to its name, then Delete.

---

## Level 3: Advanced

### Skills and plugins
- **Find them:** Customize > Skills / Plugins.
- **Run a skill:** type `/` in the message box.
- **Check before installing:** read the install warning. Some plugins can access everything on your computer.
```
/canvas-design Make a bold poster for my farmers market stall. Use our real menu and prices from the price list, and the line "Open Saturdays 8 to 1".
```

### Claude Slides
```
Make a 5-slide pitch deck asking the market manager for a permanent Saturday spot. Use our real sales numbers from the sales file.
```
Edit by asking:
```
On the weekly sales slide, highlight the best week and label it with its total.
```

### Claude Docs
```
Write a one-page market-day checklist as a doc I can print: before I leave home, setup at the market, during service, and pack-down.
```

### Connectors (Google Calendar), Manual vs Auto
```
Add my next 4 Saturday markets to my Google Calendar: October 10, 17, 24 and 31, 2026, 8:00 AM to 1:00 PM Denver time, titled "Coffee cart - farmers market".
```
- **Manual:** Claude asks before every action.
- **Auto:** Claude only pauses if something looks unsafe.

Use Manual while learning.

### Scheduled task
In the project, find **Scheduled** and click **Add**. Set it to Weekly, on Monday.
```
Read the latest sales file in this project. Write me a 5-line summary of last week: total sales, best item, anything that went up or down, and one thing to try next Saturday. Show your maths.
```
Scheduled tasks run without pausing for approval, so write the instructions carefully.

### Claude in Chrome
```
Find the vendor application page for the Old South Pearl Street Farmers Market in Denver and tell me the application fee, the booth fee, and how to apply. Just read, don't fill in or submit anything.
```

---

## The habit that matters most
Check the answers. In the test Claude got almost everything right, and it made three slips:
- It said "9 Saturdays" when the file had 8.
- Its memory wasn't there yet.
- A checklist said to bake muffins at home, which breaks the Denver rule the research found.

Every one was easy to spot, because I checked.
