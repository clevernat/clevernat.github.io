# Claude motion graphics: the prompts from the video

Tested in claude.ai on 2026-10-11 (normal chat, not incognito). Scores are against the answer key at the bottom, written before any test.

## 1. One lazy sentence (Opus 5.5: 9/10, no sound)
```
Make me a 20-second motion graphics promo video for an app called Brewly, a coffee subscription app. Build it as an HTML artifact that plays on its own in 16:9.
```

## 2. The director prompt (Opus 5.5: 10/10, Sonnet 5.5: 10/10)
```
You are a senior motion designer. Make a 20-second launch promo for Brewly, a coffee subscription app, as one HTML file that plays in 16:9.

Style: warm espresso brown, cream and one bright orange accent. Big bold type, kinetic typography, smooth eased motion, no stiff slides.
Shots: 1) a coffee cup fills up as the word BREWLY slams in. 2) three problems flash past (stale beans, empty bag, 7am panic). 3) a phone mock shows the app: pick beans, pick a schedule, tap subscribe. 4) beans fly into a box that ships across a map. 5) logo, "First bag free", and a Download button pulse.
Sound: add a beat made with the Web Audio API (kick, hats, a short synth riff) at 120 BPM, and cut every shot on the beat. Add whooshes on transitions. Start with a big Play button, because browsers block sound until you click.
Add a progress bar and a Replay button.
```

## 3. Get a real MP4 (follow-up in the same chat)
```
Now I need this as a real video file I can post. Add a "Download video" button that plays the promo once and records it, picture and sound, into a video file I can download.
```

## 4. Animated chart from your own numbers (Opus 5.5: 10/10)
```
Make a 20-second animated chart explainer as an HTML artifact in 16:9, with a Play with sound button and a Download video button.
Title: Electric cars went mainstream. Use exactly this data (global electric car sales, millions, IEA Global EV Outlook):
2020: 3 | 2021: 6.6 | 2022: 10 | 2023: 14 | 2024: 17 | 2025: 20
Bars grow year by year on the beat, a counter counts up to 20 million, then end on: "1 in 4 new cars sold in 2025 was electric." Put "Source: IEA" on screen.
```

## 5. "Go all out" showreel (Opus 5.5: 10/10, about 28 minutes)
```
Make a 20-second motion design showreel that shows what an incredible motion designer you are. This is your showreel for a job application, so go all out. One HTML artifact in 16:9, with music made in code, a Play with sound button and a Download video button.
```

## 6. With the free skill installed (Opus 5.5: 10/10, finished MP4)
```
Make me a 20-second promo video for an app called Brewly, a coffee subscription app.
```

## Answer key (one point each)
1. Plays with no errors and no blank frames. 2. 16:9. 3. Length within 3 s of what you asked. 4. At least 5 distinct shots. 5. Brand spelled right and readable on a phone. 6. No overlapping or clipped text. 7. Eased motion, nothing frozen over 1 s. 8. Ends on logo + call to action. 9. Sound after one click, cuts on the beat. 10. Replay works and the progress bar moves.

## Mistakes to skip
- Asking for sound without a Play button: browsers block sound until you click.
- An incognito chat: the promo plays inline but the download never starts. Use a normal chat.
- Letting Claude guess your numbers: paste the real data.
- Uploading a skill with Settings > Capabilities > Code execution and file creation switched off.
