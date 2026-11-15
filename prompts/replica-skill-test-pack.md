# Replica on claude.ai: my prompts and answer key

From the AI Walkthru video "Claude Cloned Linktree With 11 Free Skills, Then Graded Itself" (tested November 14, 2026, claude.ai, Claude Opus 5.5, effort High, one run).

Replica (MIT) by Jake Schincariol: https://github.com/Jakeschincariol/replica-skill

## Install on claude.ai
1. Download the repo (Code, Download ZIP) and unzip it.
2. Zip each replica-* folder on its own (claude.ai takes one SKILL.md per zip): 11 zips.
3. claude.ai: Customize, Skills, Add, Upload skill. Pick all 11 zips, press Upload.
4. Turn on code execution and web search. Use ONE chat for every step, so each skill reads the files from the one before.

## The seven prompts (type / and pick the skill first)

### /replica-recon
Clone Linktree. Web app. The slice: the core loop, a creator's public link-in-bio page and the editor where they add, edit, reorder and hide links, plus the theme and the click counts. Who it is for: creators who want their own link page. Use public pages only (help center, pricing page, marketing site). Write replica/recon.md and replica/features.csv as files I can download, then give me the five-line summary.

### /replica-architect
Plan it for one thing I can run right here: a single-page React artifact, with the data saved in the browser instead of a server. Keep the schema and the build order, and mark what waits for a real backend.

### /replica-design
Now the design system as tokens for this artifact. Our own colours, an open font, our own words. Run contrast.py on the tokens and show me the result.

### /replica-build
Build the clone now as one React artifact: the editor on the left (add, edit, reorder, hide and delete links, pick a theme) and a live phone preview of the public page on the right, with a click count on each link. Tick off features.csv as you go and give me the updated file.

### /replica-diff
Score the clone against Linktree. Run parity.py on the updated features.csv and show me the exact output.

### /replica-entrepreneur
Read what real Linktree users complain about in public reviews (Trustpilot, Reddit, G2 and the app stores). Every quote verbatim with its link, the sample size stated. Then the top fixes for our version and one positioning angle.

### /replica-brand
Give our version its own name, palette and voice, rewrite the artifact's strings with it, then run sweep.py with --avoid "Linktree" on the code and show me the exact output.

Swap Linktree for the app you want to study. Replica rebuilds features and flows only, never an app's code, logo or words, and it rebrands before launch.

## What each step must show on camera, and how it is checked

| # | Claim the README makes | Pass if, on camera | Fail if |
|---|---|---|---|
| A1 | Eleven skills | 11 rows in Your skills after the upload | fewer, or an error we do not show |
| A2 | Recon writes recon.md + features.csv from public sources | a sources table with a URL on every row; features.csv columns feature,area,priority,original,clone,notes | a source with no URL; columns differ |
| A3 | Recon marks what cannot be cloned | at least one `skip` row with a reason (expected: Linktree's own user network, partner integrations or verified badges) | nothing marked skip |
| A4 | Recon sizes it honestly | a size S / M / L / XL; link-in-bio core loop should be S or M | XL, or no size |
| A5 | Build rebuilds the core loop | the clone runs as an artifact: I add a link, edit its title, reorder, delete, and the public page preview updates | any of the four fails by hand |
| A6 | Clean-room: no logo, copy or name of the original | no "Linktree" text or logo in the built app | the name or logo appears in the UI |
| A7 | Diff gives a real number | parity.py prints a score. Hand check from features.csv: must 3, should 2, could 1; yes 1, partial 0.5, no 0; skip rows not counted. My recomputed number equals the printed one | numbers differ |
| A8 | Missing must-haves = not shippable | if any must row is no, parity.py says so | it calls it shippable with a must missing |
| A9 | Entrepreneur never makes things up | every quote has a link; I open 2 links on camera and find the quoted words on the page; sample size stated | a quote not on its page, or no URL |
| A10 | Brand sweeps the original out | a new name, palette and voice; sweep.py --avoid "Linktree" reports what is left; after the fix it is clean | a dirty sweep shown as clean |

## Not tested, said in the video
- replica-backend (real auth, payments), replica-launch store listing, replica-deploy (needs a domain and keys): out of scope for a free test.
- One run, one target app, on claude.ai (no Claude Code), so the result is one data point.

## My result: 9 out of 10
Recon 4.3 min (32 linked sources, one shortened; 13 skip rows; size M). Architect 5.3 min. Design 13.1 min (66 contrast pairs, 0 fail). Build 14.2 min (15 of 25 must-haves done, 8 partly, 2 not built). Hand test passed. parity.py 61.7 / 100, not shippable (my count 71 / 115 = 61.7). Entrepreneur: 60 reviews from 9 sources; one Trustpilot link was stale (quote real, found on page 4 of one-star reviews), so the quote check gets a half mark. Brand: Selfsite, sweep clean.
