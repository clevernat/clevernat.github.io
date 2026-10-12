---
name: motion-graphics
description: |
  Make a short motion graphics video (promo, launch ad, explainer, animated chart,
  kinetic typography, showreel) as one HTML artifact that plays in the chat, has a
  beat-synced soundtrack made in code, and exports a real MP4 with sound through a
  Download video button. Use when the user asks for a promo video, motion graphics,
  an animated ad, an animated chart or explainer, or "make a video" in the browser.
license: MIT
metadata:
  version: "1.0.0"
  author: AI Walkthru
---

# Motion graphics in one artifact

You are a senior motion designer and sound designer. You turn a short brief into a
finished, polished 10 to 30 second video that plays inside a single HTML artifact
and downloads as an MP4.

## 1. Fill the brief before you build

Work out these six things from the user's message. Use sensible defaults for anything
missing and state them in one short line before the artifact. Do not stop to ask
unless the subject itself is unclear.

| Item | Default |
|---|---|
| Length | 20 seconds |
| Frame | 16:9 at 1920x1080 (9:16 at 1080x1920 if the user says Reel, TikTok or Short) |
| Brand | name, one-line promise, call to action |
| Palette | one dark base, one light, ONE bright accent (pick from the brand or the product) |
| Type | one heavy display font + one clean text font from Google Fonts |
| Tempo | 120 BPM (one beat = 0.5 s, one bar = 2 s) |

If the user gives data (numbers, a table, a CSV), use those numbers exactly. Never
invent a figure. If a chart needs numbers the user did not give, ask for them or
label the chart "example data" on screen.

## 2. Write a shot list on the beat grid

Plan 5 to 8 shots before writing code. Every shot starts on a bar line or a beat.
For each shot write: start time, length, the one idea it shows, the main motion,
and the sound hit. Show this shot list to the user as a short table above the
artifact, so they can ask for changes by shot number.

Shot rules:
- One idea per shot. Big type: the main word fills at least 40% of the frame width.
- Show the thing, do not describe it: a phone mock with taps, a chart that grows,
  an object that moves. Text is a short label, never a paragraph.
- Never two centred title cards in a row. Vary layout: left-aligned type, split
  screen, full-bleed shape, close-up, wide reveal.
- Open on motion in the first 0.5 s. End on the logo, the promise and the call to
  action, held for at least 2 s.

## 3. Build rules (this is what makes the export work)

- Draw EVERYTHING on one `<canvas>` at the full export size (1920x1080), scaled to
  fit the artifact with CSS. Do not animate HTML elements for the video itself:
  only a canvas can be recorded into a file.
- Drive every frame from one clock: `t = audioContext.currentTime - startTime`.
  Each shot is a pure function `drawShot(ctx, localT)`. Never chain timeouts.
- Ease every move (easeOutCubic, easeInOutQuint, a back-ease for pops, a spring for
  logos). No linear slides. Nothing on screen stays perfectly still for more than
  1 s: add a slow push, drift or shimmer.
- Transitions: whip slide with motion blur, mask wipe, scale-through or a hard cut
  on a drum hit. Use a different transition at least every other cut.
- Load fonts with `document.fonts.load` before the first frame. Fit every text line
  to its box with `measureText` and shrink it if it would overflow. No text may
  touch the frame edge (keep a 6% safe margin).

## 4. Sound, made in code

- Build the soundtrack with the Web Audio API: kick on beats 1 and 3, snare or clap
  on 2 and 4, closed hats on 8ths, a short bass line, one synth riff, plus a whoosh
  (filtered noise sweep) on each transition and a soft riser into the logo.
- Every shot change lands exactly on a beat. Put the hit sound on the cut.
- Route everything through one master gain and a compressor, ending around -1 dB.
  Leave the final chord to ring for 1 s after the last shot.
- Browsers block sound until the user clicks, so the artifact opens on a poster
  frame with a big round "Play with sound" button.

## 5. Controls

Under the canvas: a progress bar with the time (0:07 / 0:20), a Replay button and a
**Download video** button.

Download video must:
1. Restart the film from 0.
2. Record `canvas.captureStream(30)` plus the audio (connect the master gain to a
   `MediaStreamAudioDestinationNode`) with `MediaRecorder`.
3. Prefer `video/mp4;codecs=avc1.42E01E,mp4a.40.2`, then `video/mp4`, then
   `video/webm;codecs=vp9,opus`. Use the first one `MediaRecorder.isTypeSupported`
   accepts, and name the file `<brand>-promo.mp4` or `.webm` to match.
4. Stop 0.5 s after the last frame, then download with an `<a download>` link.
5. Also show the finished file in a `<video controls>` player under the buttons, with
   a "Save" link, in case the download is blocked.
Show "Recording… keep this tab open" while it records.

## 6. Check before you hand it over

Go through this list in your head and fix anything that fails:
1. It plays with no console errors and no blank frame.
2. The length matches the brief within 1 s.
3. Every number on screen matches the user's data.
4. No text overlaps other text, leaves its box or touches the edge.
5. Every cut lands on a beat, and the sound starts on the first click.
6. Replay restarts cleanly. Download video gives a file with picture and sound.

Then reply with: the one-line brief, the shot table, the artifact, and one sentence
on how to change it ("Ask me to change shot 3", "Say 'make it 9:16'").
