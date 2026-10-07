# Free Google AI faceless video prompts (AI Walkthru)

The four prompts from the video "I Made a Faceless YouTube Video With Only Google's Free AI Tools". Every one was tested on camera on 2026-10-06. Change the parts in [brackets] to fit your channel.

---

## 1. Google Trends: find the niche (trends.google.com)

No prompt needed for classic Explore:

1. Type 2 or 3 niche ideas as search terms.
2. Set the time to **Past 5 years**.
3. Open the last menu and switch **Web Search** to **YouTube Search**. The winner often changes.
4. Search the winner on its own, scroll to **Related queries**, and keep **Rising** selected to find an angle.

For the new Explore page, click **Suggest search terms** and type your idea in plain words, for example:

```
History videos people watch to fall asleep
```

Then switch the property to **YouTube Search**.

---

## 2. Gemini Notebook: the script (notebook.google.com)

1. Create a notebook. Add 2 or 3 **Websites** as sources, plus a short channel brief as **Copied text**.
2. Open each source. If one says "Checking your browser" or similar, delete it (a site blocked the import).
3. Paste:

```
Write a 60-second voiceover script for a calm faceless [history] video: [why Roman concrete lasted 2,000 years]. Use 6 scenes. For each scene give the narration (25 words max) and one image prompt. Then give 3 title ideas. Use only facts from my sources.
```

4. Click the citation number on every fact you will say out loud.
5. Optional: Studio > Video Overview > pencil > Cinematic, Short or Explainer, add your focus, Generate now.

---

## 3. Gemini Canvas: the monetization planner (gemini.google.com)

Plus > More tools > Canvas, then paste:

```
Build a YouTube monetization planner app. Rules: the fan-funding tier needs 500 subscribers, 3 public uploads in the last 90 days and 3,000 public watch hours in the last 12 months. The full YouTube Partner Program needs 1,000 subscribers and 4,000 public watch hours. From February 1, 2027, new applicants for the full program need 8,000 watch hours instead of 4,000. Today is [today's date]. Add sliders for subscribers, watch hours, new subscribers per week and new watch hours per week. Show the week and the date each tier is reached, and warn me if the full program date lands after February 1, 2027. Start with [your subscribers] subscribers, [your hours] hours, [subscribers per week] subscribers a week and [hours per week] hours a week. Ignore watch hours expiring.
```

Check the answer by hand: hours needed divided by hours per week gives the weeks. Rules source: support.google.com/youtube/answer/72851 and the YouTube Blog post of Aug 10, 2026.

---

## 4. Google Flow: the visuals (flow.google.com)

Turn on **Agent** in a project and paste (replace the six scene lines with yours):

```
Make 6 images, 16:9, one per scene, for a calm [history-for-sleep] video about [Roman concrete]. Keep one style for all: soft painterly realism, warm low light, no text.
1. [scene one]
2. [scene two]
3. [scene three]
4. [scene four]
5. [scene five]
6. [scene six]
```

Tip from the test: do not ask an image model to "number" images. It painted a number into one of them. Rename the files yourself after you download them.

To animate:

```
Animate [image name] and [image name] into two 8-second 16:9 videos. Slow camera push-in, calm, no text.
```

The agent asks before it spends credits (2 clips cost 24 credits in the test).

---

Before you upload: if any clip looks photorealistic, turn on the AI disclosure in YouTube Studio. Do not mass-produce or copy other channels' videos (YouTube's inauthentic content policy).
