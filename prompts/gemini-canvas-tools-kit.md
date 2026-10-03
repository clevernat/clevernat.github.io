# Gemini Canvas client-tools kit (AI Walkthru)

Four prompts, tested live in Gemini Canvas (3.1 Pro) on three fictional local businesses, plus the follow-ups that fixed what broke.
Every number was checked against answers worked out by hand before the first prompt. No income promises: the prices are my examples.

> Do this on a laptop or desktop. Gemini Canvas failed a lot of my requests ("I encountered an error..."): retry, and keep a downloaded copy of every version that works.

## How to switch Canvas on
1. Go to gemini.google.com. Optional: open a **Temporary chat** (nothing saved). Use a **normal chat** if you need a share link.
2. Model picker: **3.1 Pro** (Flash failed six times in a row in my test).
3. Click **+** > **More tools** > **Canvas**. A Canvas chip appears in the box.

## 1. Gym goal calculator (Peak Form Fitness)
```
Build a goal calculator for Peak Form Fitness, a local gym. Inputs: sex, age, height in feet and inches, current weight and goal weight in pounds, and training days per week (0 to 7). Use the Mifflin-St Jeor formula for BMR. Activity multiplier: 0-1 days 1.2, 2-3 days 1.375, 4-5 days 1.55, 6-7 days 1.725. To lose weight: maintenance minus 500 calories at 1 lb per week. To gain: maintenance plus 250 calories at 0.5 lb per week. Show daily calories, weeks to goal, and recommend a membership: Starter for 0-2 days, Plus for 3-4 days, Elite for 5 or more.
```
Branding follow-up:
```
Brand it for Peak Form Fitness: primary color #E4572E, dark color #1B1B3A, white background, Montserrat font, and a 'PEAK FORM' logo at the top. Make sure it looks great on a phone. Don't change any of the calculations.
```
Test it yourself: male, 35, 5 ft 10 in, 200 -> 180 lb, 3 days = **2,042 kcal/day, 20 weeks, Plus**. Also try 6 ft **0** in: one earlier build turned 0 inches into 10.

## 2. Dental quiz that collects leads (Bright Smile Dental)
```
Build a 3-question quiz for Bright Smile Dental called 'Which whitening option fits you?'. Q1: Are your teeth sensitive? (Yes / No). Q2: When do you want results? (This week / Within a month / No rush). Q3: What's your budget? (Under $200 / $200-$600 / Over $600). Apply these rules in order: sensitive = Gentle Sensitive-Teeth Plan; this week AND over $600 = In-Office Express Whitening; under $200 = Starter Whitening Kit; anything else = Custom Take-Home Trays. Show the result with a short description and a Book a consult button.
```
Lead follow-up (leads go to the OWNER's Google Form, not the app):
```
Before showing the result, ask for first name, email and phone. Don't keep the leads in the app. Send each lead to my Google Form instead. Here is its pre-filled link, so you can see the field IDs: [PASTE YOUR FORM'S PRE-FILLED LINK]
```
If the preview is blank or shows code: "This opened as a code document, not a working preview, and the code is cut off. Please rebuild it as one complete HTML file that runs in the preview."

### The Google Form, step by step
1. forms.google.com > **Blank form**. Close the Gemini helper.
2. Title it (e.g. "Bright Smile Dental - Leads").
3. Questions: **First name**, **Email**, **Phone**, each as **Short answer**.
4. **Publish** and confirm.
5. Three-dot menu > **Pre-fill form**. Type a sample answer in each field > **Get link** > **Copy link**. Paste that link into the lead follow-up above.
6. Leads appear under **Responses**, visible only to the form's owner.

Why not Canvas's own database? Google's help page: data shared between users of a Canvas app "can be seen or edited by anyone with a public link to the app".

## 3. Roof quote calculator (Ridgeline Roofing)
```
Build an instant roof replacement quote calculator for Ridgeline Roofing. Inputs: house footprint in square feet, roof pitch (Low x1.05, Medium x1.15, Steep x1.30), material (Asphalt shingles $4.50, Metal $9.75, Tile $12.00 per square foot), a 'remove old roof' checkbox ($1.25 per square foot of roof area), and stories (1 or 2). Roof area = footprint x pitch. Material cost = roof area x 1.10 for waste x material price. Add the tear-off if checked. Two stories adds 10% to the total. Show the roof area, the estimate, and a range of plus or minus 10%.
```
AI follow-up (works for signed-in Google users only):
```
Add a box where the homeowner describes their roof problem in their own words, and use AI to reply with a short, friendly summary and an urgency level: Emergency, Soon, or Can wait.
```
Test: 1,800 sq ft, medium, asphalt, tear-off, 1 story = **$12,834** (roof area 2,070 sq ft).

## 4. Your own pricing calculator
```
Build a pricing calculator for my own service: I build interactive tools for local businesses. Packages: Basic $250 (one tool), Branded $450 (client branding plus one revision), Lead Machine $750 (branded, lead capture to Google Sheets, plus two revisions). Add-ons: extra revision $60 each, second language $120, and rush 48-hour delivery adds 20% to the one-time total. Optional care plan $40 per month, shown separately. The price updates live as options change.
```
If "extra revision" comes out as a single checkbox:
```
Bug: Extra revision is a single checkbox, but it's sixty dollars EACH. Let the client choose how many extra revisions they want, and charge sixty dollars for each one. Don't change anything else.
```
Test: Branded + 2 extra revisions + rush = **$684**.

## Deliver it the safe way
- **Share link**: visitors first see Gemini's warning "This app was created by another person. It may be unsafe", and AI features need a Google sign-in.
- **Download** (one HTML file): runs on its own; put it on the client's own website. AI features won't run from the file.
- Write your expected answers first, and test every number before you send anything to a client.
