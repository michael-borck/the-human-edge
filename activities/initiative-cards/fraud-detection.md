---
title: "Fraud detection"
description: "Cut chargebacks without blocking real customers: a buy-vs-build and threshold-tuning problem. ($650K, funded.)"
---

**Your group is the delivery lead for this funded initiative.**

---

## The mandate

The board has approved **$650K** to deploy AI fraud detection across RetailFlow's online payments, to cut chargebacks and fraudulent returns.

**What the board thinks it bought:** "fewer fraud losses, fast."

**Your job:** deliver it without the predictable failures, and define what "good enough" detection looks like when both false positives and false negatives carry real cost.

---

## Why this one is hard to *deliver*

- The honest delivery question here is **build vs. buy.** Priya's view: a third-party solution is more practical than building in-house. So your "delivery" may be a *vendor integration and oversight* project, not a data-science build. It is a different kind of plan, and a useful contrast for the room.
- The two failure modes pull in opposite directions: too aggressive and you **block legitimate customers** (revenue + reputation hit); too loose and fraud slips through. There is no single "accurate"; it's a tuned trade-off.
- A vendor demo on their data tells you little about performance on *RetailFlow's* fraud patterns (demo-to-production gap, vendor edition).

## The data reality (ask Priya)

Priya's honest read: *"third-party AI more practical than building; our data-science team shouldn't own this. Quick win with the right vendor, 3–6 months. Buy, don't build."* Your roadmap should reflect a procurement-and-integration shape, with the threshold tuning as the real risk.

## Who to interview, and the tension they bring

- **Priya Sharma (Data)**: argues buy-not-build; what your team should and shouldn't own.
- **David Chen (CFO)**: owns the loss numbers and the ROI case; wants certainty.
- **Tom Walsh (Customer Service)**: his team handles the fallout when a legitimate customer is wrongly blocked. Who reviews flagged transactions, and how fast?

## Your starting question for "good enough"

Where do you set the threshold, and **who reviews flagged transactions before a customer is blocked**? How do you measure success when the two errors (false block vs. missed fraud) have very different costs?
