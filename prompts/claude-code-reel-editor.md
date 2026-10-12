# Claude Code reel editor: prompt pack

Every prompt from the AI Walkthru video "Claude Code Edited My Reel From 2 Links (Opus 5.5, Full Walkthrough)". Tested on camera on Claude Code v2.1.296, Opus 5.5, high effort.

## Before you start

1. Make your Google Drive folder viewable by link ("Anyone with the link"), or download the clips into the folder yourself.
2. Open Claude Code in an EMPTY folder (terminal: `claude`; or the Claude desktop app: Code tab, choose the folder).
3. Type `/model`, press Enter, move down to **Opus 5.5**, press the right arrow once for **High effort**, then press **s** (this session only).

## Prompt 1: the edit

```
I'm sharing two links with you.

1. Style reference (Instagram Reel): [the Instagram reel you want to copy]
2. Raw footage (Google Drive folder): [your Google Drive folder link]

Please download the reference reel and every clip in the Drive folder. Study the reference closely: its length, aspect ratio, pacing, cut timing, colour grade, music and overall structure. Then edit my clips into one finished video that looks and feels as close to the reference as possible. Combine the footage, match the pacing and the look, and export a final video I can post.

Work in this folder, check your own result before you hand it over, and ask me before making any decision you cannot make on your own.
```

Claude will ask you questions before it edits (in the test: the music and the ending). Answer them; that is the point of the last line.

## Check version 1 yourself

The first version in the test looked close, but it had two problems Claude did not check for:
- **Repeated shots.** It used 51 shots from 19 clips (one clip 8 times).
- **The reference song's extras.** The song had a shouted "Happy Mother's Day" from the other church's event.

## Prompt 2: name each problem in plain words

```
I watched the video, and two things need fixing.

1. Too many shots repeat: the same footage keeps appearing two or three times. Re-edit it so each of my nineteen clips appears only once. If nineteen shots cannot fill the current length at the reference's pace, shorten the video rather than reuse a clip, and end it on a natural musical phrase.
2. Near the end of the song, someone sings "Happy Mother's Day" over the music. Remove that part completely.

Keep the same grade and cut style, check the result again, and export the new version.
```

In the test this fixed both problems, but the video became 21 seconds long (it kept 1 second per shot). Too literal.

## Prompt 3: add a number

```
Good, every clip now appears only once and the "Happy Mother's Day" part is gone. But 21 seconds is too short for this reel.

Hold each shot a little longer, about two seconds on average, still cutting on the beat, so the video runs about 38 seconds. End it where the first chorus resolves, on "It's you, you, you I live for", with a gentle fade-out. Keep each clip used only once, check the result, and export it as the final version.
```

Result in the test: 36.1 seconds, 19 shots, each clip once, every cut on the beat (about 86 BPM), ending on the chorus.

## Notes

- About 38 minutes of Claude work in total (28 min 45 s, then 4 min 13 s and 5 min 3 s).
- Instagram may mute a song that is not yours. Safest: post the video and add the same song in Instagram's music picker; the cuts still line up.
- Claude Code needs a paid Claude plan. It installed or used ffmpeg, yt-dlp and gdown on its own in the test.
