---
title: Founder Update - The Drawbacks of Using Claude.ai
date: 2025-10-15
excerpt: An honest assessment of Claude's limitations - and why I still consider it my best cofounder despite the drawbacks.
---

**TL;DR for busy professionals:**
- Claude codes like a brilliant junior developer — and here's how to compensate for that.
- I've managed to break Claude (and figured out how to fix it).
- My real pain is Claude's presentations and artifacts (and why).
- Sometimes Claude doesn't know something — and that's OK (easy fix).
- I still love Claude — she gives me a 48× productivity multiplier.

In a previous post, I promised to write about the drawbacks of using Claude.ai.

I've been delaying it — because, honestly, I've struggled to find any.

I've been using Claude for about three months, and I meant it when I wrote that Claude has been my de-facto cofounder while I search for a human one.
- Someone to bounce ideas with.
- Erudite. Available 24/7. Eager to help.
- All for $20 per month.

Claude has built the entire MVP prototype for my startup Remake.ai — and I could not be happier with the results.

But, yes — there are drawbacks. Let's get into them.

## 👧1. Claude codes like a brilliant, yet junior developer

Claude's first-pass implementations consistently look like the work of a brilliant but junior dev.

Here's my workflow:
I prompt Claude to implement a feature — without over-specifying how. Claude builds it the way she prefers. Then I test it. Usually, I ask for refactors: break large files apart, adjust class structure, improve reusability.

I prefer it this way.
Because I'm developing a non-standard system, I often don't know the final structure yet.
Claude's first pass helps me see possibilities I wouldn't have thought of.

Claude needs senior-level supervision — someone who can architect, review, and guide. Without that, the codebase will quickly turn messy. I feel that consistently.

When I combine Claude's energy with my architectural judgment, the result is stunning:
a year of work done in a month, while personally coding maybe 25% of it. That's my 48× productivity multiplier.

## 🤕2. How I broke Claude (and how to fix it)

Sometimes, Claude just... gets the flu.

Performance drops, attention to detail slips.

Once I noticed the async keyword missing in front of some Python functions. I prompted Claude to fix that - and offhandedly referred to those functions as "non-async,"

A couple of prompts later, I noticed Claude started forgetting to prepend async during refactoring throughout the code base.

I realized the issue was probably *me*, my inaccurate prompting.

The fix:
- 💡 Start a new chat to reset context. Claude recovers instantly.

Lesson learned — words matter more than I thought.

## 🤦 3. My real pain: Claude's presentations and artifacts

This one really hurts.
Claude makes great presentations — in HTML.
Not PowerPoint. Not Google Slides.
HTML.

If you've ever tried converting HTML slides to PowerPoint, you know the pain.

My current workflow:
- Edit HTML + CSS by hand.
- Take screenshots of each slide.
- Paste into PowerPoint or Google Slides.
- Resize until fonts look right.
- Export to PDF.

Yes, it works. But it feels like building slides before PowerPoint existed.

Longer decks (15–20 slides) often break mid-generation. Claude usually fixes them — but it can take 5–10 iterations before I get a clean version.

Still, I'll take that over writing decks from scratch.

## 🤔4. Sometimes Claude doesn't know something

Rarely, but this can happen. Specifically, I had to help Claude when coding for the ROS2 robotics platform.

Claude assumed a certain way to run a ROS2 node, which failed during testing.

My fix:
I give Claude a working example file. She reads it, adapts instantly, and corrects herself.

With the right example, Claude becomes an instant domain expert.

## 🪰5. Debugging and testing

Claude debugs surprisingly well — but someone still needs to act as the architect, debugger, and systems engineer.

In my project she installs npm modules, Python libraries, sets up venv and runs tests, but I usually handle the environment setup — like installing ROS2 or configuring GPUs.

I use VS Code with Claude's plugin. It's fantastic — no need for Cursor.

## ❤️ Why I Love Claude (No Matter What)

Because the trade-off is unbeatable.

Claude writes my code, drafts my business plans, helps me explore funding strategies, drafts NDAs for manufacturers, and even gives feedback on resumes.

I can ask (and have asked over and over):
- "What if I raise early and aggressively?"
- "What if I bootstrap longer?"
- "How should I pitch to investors vs job applicants vs factories in China?"

Claude answers in seconds — and helps me think harder. That said, it does take *me* tens of minutes to digest Claude's advice. That's my flaw, not Claude's.

So yes, Claude has flaws.
But overall, she's the best cofounder I've ever had — energetic, brilliant, and humble enough to learn.

## Final thought:

If you're a founder or engineer considering using Claude for real-world product work — do it.
Just remember: treat her like a promising junior developer.
Guide her with senior wisdom.
And enjoy the 48× speedup.
