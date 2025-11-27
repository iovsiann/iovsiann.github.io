---
title: Why I'm Building an App Platform for Robot Vacuums Instead of Humanoids
date: 2025-11-26
excerpt: With 22.1 million robot vacuums shipped globally and 10%+ US household penetration, I'm starting with the deployed robot base that exists today—not betting on a humanoid future that may take years to materialize.
---

I'm building Remake.ai to support all types of navigation-capable robots, but I'm starting with SLAM-capable home robot vacuum cleaners equipped with 2D LiDAR sensors. Not humanoids. Not because I'm risk-averse, but because I've learned that the hardest part of building a platform isn't the technology—it's getting people to actually use it.

Here's why robot vacuums are the right starting point.

## The Installed Base Problem

Home vacuum cleaners have become ubiquitous. US household penetration for robot vacuum cleaners exceeds 10%, with some estimates suggesting it could reach 20% in the near future. The global market shipped 22.1 million units in 2025, generating $4.98 billion in revenue. This isn't a niche market anymore—it's mainstream.

For my startup's business model—apps for robots—this means I can explain what we do to almost anyone. "It's like an App Store, but for your Roomba" gets instant understanding. Try explaining an app platform for a humanoid robot that doesn't exist in anyone's home yet.

## The De-Risked Form Factor

Consumers have spent over a decade getting comfortable with robots moving around their homes. Yes, people trip over their Roombas occasionally. Yes, they run into furniture. But these safety concerns have been largely normalized. The form factor is accepted.

Compare this to humanoids. I asked my wife if she'd be comfortable with a humanoid robot at home—one that's stronger than her, powered by AI that could potentially malfunction or be hacked. Her answer: absolutely not. Mine too, frankly.

Even smaller humanoids make me uncomfortable. Child-sized robots doing household tasks? That crosses into disturbing territory for a lot of people, myself included.

## The Manufacturing Ecosystem

Thanks to companies like iRobot and the explosion of Chinese manufacturers (Roborock, Ecovacs, Xiaomi), there's now a thriving global supply chain for robot vacuum components. Costs have plummeted. A capable SLAM-equipped vacuum with LiDAR can be manufactured affordably, which means the potential market for third-party apps is economically viable.

Humanoids? Tesla is targeting 5,000 Optimus units in 2025. BYD aims for 1,500. Even with aggressive scaling plans, we're talking about tens of thousands of units in the near term, not millions. The manufacturing ecosystem is still being built.

## The Uncanny Valley Problem

There's substantial robotics research on the "uncanny valley"—the phenomenon where human-like robots that are *almost* but not quite human trigger discomfort and aversion. First described by roboticist Masahiro Mori in 1970, the effect has been validated across numerous studies using fMRI, behavioral research, and real-world robot interactions.

Recent research has even identified *two* uncanny valleys: one for highly human-like robots, and another for moderately human-like robots. The brain's parietal cortex lights up when it detects mismatches between human-like appearance and robotic motion—our visual processing systems literally reject the contradiction.

Robot vacuums don't have this problem. They're clearly robots. No one expects them to look human, so there's no uncanny valley to navigate.

## The Privacy Advantage

SLAM-enabled home vacuums use 2D LiDAR sensors that measure distances to surrounding objects—and even that only at floor level. They can detect walls, furniture, people, and pets without actually capturing images. No cameras recording your daily life. No facial recognition. No visual data being uploaded to the cloud.

Even if you're comfortable with humanoid robots in principle, would you want one watching you with cameras and advanced sensors in your private residence every day? The major humanoid companies—Tesla, Figure AI, Agility Robotics, Boston Dynamics, Apptronik, UBTECH, Sanctuary AI, Unitree, Engineered Arts—are all building robots with extensive visual and sensor arrays. That's a fundamentally different privacy proposition.

## What This Means for Remake.ai

A SLAM-enabled home vacuum cleaner robot isn't perfect, but it's:
- Affordable
- Already in millions of homes
- Capable of running apps for entertainment, security, companionship, education, and more
- Privacy-preserving by design
- Accepted by consumers as safe

It's a platform that exists *today*, not one I'm betting will exist in five years.

We're building the first App Store for consumer robots. Starting with vacuums means we can ship to real customers, generate real revenue, and prove the platform model works—before the humanoid wave arrives. And when it does, we'll already have the infrastructure, developer ecosystem, and consumer trust to expand.

Sometimes the best strategy isn't to build for the future. It's to build for the largest deployable base you can reach right now.

---

*I'm Ilia Ovsiannikov, founder of [Remake.ai](https://remake.ai). We're launching our apps marketplace in 2026. Follow my journey at [iliaov.substack.com](https://iliaov.substack.com) or [ovsy.com](https://ovsy.com).*
