# Lab 4 — VibeCoding: Lava Escape Repair

**Kshitij G Shettigar · PES1UG24CS240**
**Assigned repo #52 — [`SETAPESU26/52_lava-escape`](https://github.com/SETAPESU26/52_lava-escape)**

A Pygame vertical platformer with one deliberate bug and three features left as tasks.
The bug was fixed and the features added by prompting Claude Code, one commit per task.
Full commit history is in the working fork:
[`Kishi836/52_lava-escape-SE-LAB-CS240`](https://github.com/Kishi836/52_lava-escape-SE-LAB-CS240).

## Deliverables

| File | Contents |
|---|---|
| `before_changes.mp4` | Gameplay before any changes |
| `after_changes.mp4` | Gameplay after the fix and all features |
| `lava-escape/` | Updated code (`python lava-escape/main.py`, needs `pygame`) |
| `Lab-4-Chat-History.pdf` | Complete chat history with the AI assistant |

## Changes

| Task | Change |
|---|---|
| 1 — Collision fix | Land only when falling and the feet were above the platform's top edge on the previous frame; platform spacing capped so every gap stays reachable |
| 2 — Crumbling platforms | Lighter platforms crack after 1 s of contact and break after 3 s, shrinking linearly to 1.8 s near the top |
| 3 — Spring platforms | Dark-blue platforms with a white coil launch the player ~3× a normal jump, reusable |
| 4 — Danger HUD & surges | Lava speed meter, 2 s surges at 3× speed every 12 s, flashing ⚠ warning when lava is within 20 m |
| Extra | MM:SS:mmm run timer; camera starts with the player on screen and lava spawns outside the warning range |
