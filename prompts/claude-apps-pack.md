# Build 3 Mac apps with Claude: the exact prompts (AI Walkthru, November 2026)

Claude's **Install as app** turns an artifact into a real Mac or Windows app with its own icon and window.
You need the Claude desktop app (Claude for Mac or Windows, version 6.28899.0 or later; Claude menu > Check for Updates).
It is in beta on every plan.

## How to use these prompts
1. Open the Claude desktop app and start a new chat.
2. Paste one prompt below and press Enter. Wait for Claude to finish the app.
3. Open the artifact's menu (or right-click it) and choose **Install as app**, then **Install**.
4. The app opens and asks for what it needs. Read the request, then choose **Allow** or **Don't allow**.
5. To change an app later, go back to the same chat and ask for one change. The app updates itself and asks for permission again.

Tip: before the folder apps, make a test folder on your Desktop called `Tidy Demo` with `Inbox` and `Screenshots` inside, and try them on copies of a few files first.

## 1. CPU Watch (menu bar + notifications)
```
Make me a small Mac app called CPU Watch. It lives in my menu bar and shows how busy my Mac is as a percent, updated every 2 seconds. If it stays above 85% for 10 seconds, send me a notification that names the app using the most. The window shows the 5 apps using the most right now. Make it a desktop app I can install.
```

## 2. Tidy Folder (sorts a folder by file type)
```
Make me a Mac app called Tidy Folder. It watches the folder "Tidy Demo/Inbox" on my Desktop. Every few seconds it moves new files into folders by type: Images, Documents, Videos, Audio, Archives and Other. Send me a notification saying how many files it sorted, and show a list of every move in the window.
```
The update I asked for afterwards:
```
Update Tidy Folder: give spreadsheets (.csv, .xlsx and .numbers files) their own folder called Spreadsheets, with its own tile in the window.
```

## 3. Screenshot Namer (Claude names your screenshots)
```
Make me a Mac app called Screenshot Namer. It watches the folder "Tidy Demo/Screenshots" on my Desktop. When a new screenshot lands there, it asks Claude to look at the picture and renames the file to a short description of what is in it, like "Eiffel Tower Wikipedia page.png". Send me a notification with the new name, and show a list of every rename in the window.
```
This app asks twice: once for access to your Mac, and once to use Claude. Each rename counts toward your Claude plan's usage.

## The five things every app prompt says
1. **A name** (the app gets its own icon and title)
2. **Where it lives** (menu bar, a window, a folder it watches)
3. **What starts it** (every 2 seconds, a new file, a new screenshot)
4. **What it does**, in plain words
5. **How it tells you** (a notification, a list, a number in the menu bar)

## My results (November 25, 2026)
- CPU Watch: 98% in the menu bar 3 seconds after a heavy load started; the alert came at 12.5 seconds and named the right process; Activity Monitor agreed (94% busy). It fell back to 34% at 8.6 seconds, just missing the 8 seconds in my answer key (4 of 5 checks).
- Tidy Folder: 18 of 18 files sorted in under 3 seconds; after the update, 4 of 4 (2 into Spreadsheets).
- Screenshot Namer: 4 of 4 screenshots renamed correctly.

How I tested: Install and every Allow are yours to press; Claude can't approve them, and on a Mac it can't click inside an installed app. So I ran each app's own published code in a test window wired to my Mac's real files, processor and Claude, and checked every result from outside (Finder, Activity Monitor). Your own installed app will ask you for permission the first time and after every update.

Limits (from Anthropic's help page): you must be online and signed in to Claude to open an app; not on Linux, web or mobile; Docs, Slides and Sheets artifacts can't be installed; full access only for apps you made (or made in your organization); Anthropic does not review apps, so only allow full access to apps you trust.
