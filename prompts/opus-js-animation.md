# Claude Opus 5.5 + JavaScript 2D animation: the prompt pack

Free pack from the AI Walkthru video "Claude Opus 5.5 Makes Full 2D Animations With Code: 3 Levels Tested". Every prompt below was run for real on Claude Opus 5.5 (High effort).

How to use it: copy a prompt, run it, then score the result against the answer key. Change the story and the style card to make your own animation.

## The answer key (written before any test)

Brief: "The Thirsty Flower", about 20 seconds, 16:9, drawn only with JavaScript. No video model, no images.

Story: a yellow flower droops in a dry sunny field. A small grey cloud drifts in, strains, squeezes out one drop, then rain. The flower lifts and blooms. The sun sets, stars appear, the cloud smiles.

Ten checks, one point each, judged from frames at fixed times (about 1, 4, 8, 12, 16, 19 s):
1. It starts by itself and lasts 18 to 22 seconds.
2. The flower visibly droops at the start.
3. A cloud enters from the side.
4. Rain falls from the cloud (10 or more drops).
5. The flower lifts after the rain starts.
6. The flower blooms (petals open).
7. The sun sets and stars appear at the end.
8. Nothing overlaps badly, is cut off or is off screen.
9. There is sound (music).
10. It looks hand-made in one consistent style.

## Level 1: one line (claude.ai, about 1.5 minutes, scored 6/10)

Open claude.ai, start a new chat (incognito is fine), pick Opus 5.5, and send:

```
Use JavaScript to animate a thirsty flower and a little cloud that brings it rain.
```

What you get: a cute looping scene in the chat. What it cannot do: end after about 20 seconds, bloom, sunset, play sound, or give you a video file.

## Level 2: the four-part brief (Claude Code, 13 minutes, scored 9/10)

Open Claude Code in an empty folder. Type `/model` and pick Opus 5.5 (press S for this session only). Type `/effort` and move to High (press S again). Paste:

```
Make a 20-second 2D animation called "The Thirsty Flower". Draw everything with JavaScript on one canvas. No images, no video models.

STORY
1. A yellow flower droops in a dry, sunny field.
2. A small grey cloud drifts in from the left.
3. The cloud strains, squeezes out one drop, then rain.
4. The flower lifts its head and blooms.
5. The sun sets, stars appear, and the cloud smiles.

STYLE CARD
Hand-drawn crayon on cream paper. Wobbly outlines that re-jitter 8 times a second. Flat crayon fills with visible grain. No gradients, no shadows.
Palette: paper #F6EEDC, sun #F4A62A, flower #FFD23F, leaf #4FA36B, cloud #B9C4CF, rain #4C8DDB, night #2B3A67.

PACING
A new motion every 2 to 3 seconds. Beats: 0s droop, 3s cloud enters, 6s first drop, 8s rain, 12s flower lifts, 15s bloom, 18s sunset and stars, 20s end on the smiling cloud. Ease every move.

TECH
One file, index.html, 1920x1080. Write a pure function render(t) that draws the whole frame for any time t in seconds, so any frame can be drawn on request.

SOUND
Compose an original gentle 20-second track in Python (numpy and wave) and save it as music.wav. Add soft noise under the rain.
```

You get `index.html` (open it and click play), `music.py` and `music.wav`. The one point it missed: it does not start by itself (browsers need a click for sound).

### Swap only the style card (paper-cut collage, also 9/10)

Replace the STYLE CARD part with:

```
Paper-cut collage with real depth. Every shape is a layer of coloured paper with torn edges and a soft drop shadow. Stack three depth layers (far hills, middle field, near grass) that drift at different speeds as the scene plays, so the camera feels like it moves. Subtle paper grain. No gradients.
Palette: paper #F3E9D2, sun #F4A62A, flower #FFD23F, leaf #3E8F5A, cloud #AEBBC9, rain #4C8DDB, night #243461.
```

### Let Claude write the brief for your own idea

```
Turn this idea into an animation brief I can give Claude Code: a sleepy robot learns to ride a bike. About 20 seconds, drawn only with JavaScript. Use four parts, plus sound. Story as numbered beats. Style card with a hex palette and how the lines look. Pacing with the second each beat lands. Technical rules with a pure render(t) function at 1920x1080. Then sound: original music composed in Python. Keep it under 250 words.
```

Paste the answer into Claude Code unchanged. Our robot idea ran in 17 minutes and exported its own mp4.

### Same brief on Claude Sonnet 5.5 (8/10)

Type `/model`, pick Sonnet 5.5 (press S for this session only) and paste the same Level 2 brief. Our run scored 8 out of 10, one point under Opus: cheaper and still good, but the details were less polished.

## Level 3: reference, tools and a check loop (Claude Code, 14 minutes, scored 10/10)

One-time setup:

1. Install Claude Code (it needs a paid Claude plan).
2. Get an API key from your ElevenLabs account settings.
3. Connect the ElevenLabs server (needs `uv` installed): `claude mcp add elevenlabs -e ELEVENLABS_API_KEY=YOUR_KEY -- uvx elevenlabs-mcp`

Put your level 2 `index.html`, `music.py` and `music.wav` in a folder, and make a clip of the level 2 result at `reference/level2.mp4` (a screen recording of the page playing works fine). Then paste:

```
Turn the Level 2 animation in this folder into a finished, narrated film called "The Thirsty Flower". Keep the look exactly: the reference clip is reference/level2.mp4. Match its style, pacing and colours frame for frame.

TOOLS
1. Set up HyperFrames in this folder (npx hyperframes init, install its skills) and build the film as a HyperFrames project. Reuse the drawing code from index.html and the track from music.wav.
2. Use the ElevenLabs MCP server to record a warm, calm narrator reading three short lines. Pick the voice yourself.
   - at 0.5s: "The little flower had waited all summer for rain."
   - at 3.5s: "Then a small grey cloud drifted by, and it tried its very best."
   - at 16s: "By nightfall, the whole field was smiling."
3. Mix the narration over the music. Lower the music under the voice, never the other way round.

CHECK LOOP
Render a draft, then take snapshots at 1, 4, 8, 12, 16 and 19.5 seconds and compare each one with the same moment in the reference clip. Fix anything that overlaps, is cut off or does not match. Repeat until every snapshot matches. Do not stop before that.

OUTPUT
final/the-thirsty-flower.mp4 at 1920x1080, 30 fps, about 20 seconds, with voice and music in one file.
```

HyperFrames is free and installs itself when Claude follows the prompt.

## The three mistakes

1. Asking for "an animation" and nothing else gives you a loop with no ending and no sound. Say how long it runs and how it ends.
2. Stopping at the web page. You cannot upload a web page to YouTube or TikTok. Add the reference, the tools and the check loop.
3. Trusting the default audio mix. In our run the picture matched on the first render but the sound needed three drafts. Always check the mix.

## Notes

- Tested on 2026-10-11 with Claude Opus 5.5 (High effort) in claude.ai and Claude Code v2.1.296.
- Run times are Claude's time on the author's machine: level 1 about 1.5 minutes, level 2 about 13 minutes, level 3 about 14 minutes.
- Results vary run to run. Score your own results against the answer key before you trust them.
- Source for the YouTube numbers in the video: YouTube Data API, 2026-10-11.
