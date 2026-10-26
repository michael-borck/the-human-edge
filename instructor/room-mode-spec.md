# Spec: room mode for the trust tool game

Status: proposal, for after the first run of the redesigned course. The paper voting cards do this job for now; build room mode once the card votes show which discussions are worth the extra setup.

## Why

The card vote in Exercise 2 works because placement is blind and the reveal is simultaneous: nobody anchors on the most senior person in the room, and a split room makes the lesson visible. Room mode does the same on phones, plus two things paper can't: participants can submit their **own** tasks anonymously, and the screen can show where the room disagreed.

## Who uses it

- **Facilitator:** creates a session, shows a join code, controls each round, reveals results.
- **Participants:** join on a phone with the code, no login, and place cards.
- **Projector:** a read-only view of the current round.

## Rounds

1. **Scenario round.** The facilitator picks a scenario (from the existing domain packs, or typed live). Each participant taps a corner. The screen shows only the count of votes ("23 of 27 placed") until the facilitator presses Reveal. Then it shows a 2x2 heat map with counts per corner, and the game's existing explanation.
2. **Own-task round.** Each participant types one real task from their week (max 80 characters) and places it. Submissions are anonymous. On Reveal, the screen shows every task as a dot in its corner. The facilitator can tap a task to put it up for a second blind vote by the whole room: that's where the best discussions come from.
3. **Contested list.** After any round, a list of the scenarios or tasks with the widest split (for example, no corner above 50%), ready for discussion.

## Requirements

- Works on any phone browser, with no app and no account. Joining takes under 20 seconds.
- Anonymous by default. Store no names or emails. Delete session data automatically after 24 hours, and give the facilitator an "end and delete" button.
- Tolerates poor Wi-Fi: votes are small, and a reconnecting phone resumes its session.
- Same corner names, colours and orientation as the game and the course: precision across, consequences up.
- Up to about 60 participants per session.
- Accessible: large tap targets, works with a screen reader, doesn't rely on colour alone (corners are lettered A to D like the paper cards).
- Optional export: a CSV of the round results (no personal data) for the facilitator.

## Suggested build

- Extend the existing static game at trusttool.borck.education rather than starting a new app. Add `/room/new` (facilitator), `/room/CODE` (participant) and `/room/CODE/screen` (projector).
- Realtime layer: a small hosted service with websockets or realtime subscriptions and a key-value store with expiry (for example, a serverless worker with a durable object, or a hosted realtime database). Keep all logic in the client except vote counting and the reveal flag.
- No participant data leaves the session store. No analytics.

## Not in scope

- Scoring or leaderboards: they reward speed, and the point is honest placement.
- Free-text chat.
- Integration with Mentimeter, Slido or Padlet.

## Done means

A facilitator can run the five card-vote scenarios and an own-task round with 30 phones on venue Wi-Fi, reveal each round on cue, and end the session with all data deleted.
