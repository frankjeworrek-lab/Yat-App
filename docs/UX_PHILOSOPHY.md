# UX Philosophy: Active User Assistance
> "Honest about problems, kind about solutions."

## Core Concept
We believe software should treat the user as an intelligent partner, not a helpless operator. When things go wrong, the system should act like a good co-pilot: truthful about the situation but offering a clear path forward.

## 1. Trust through Verification
**Problem:** Uncertainty creates anxiety. A "Warning" state without interaction leaves the user feeling helpless.
**Solution:** Every non-green state must be **verifiable**.
- **User Action:** Interactive badges allow the user to trigger a re-check.
- **System Response:** Immediate feedback ("I am checking...") followed by a definitive result.
- **Goal:** The user can actively work to restore their sense of security.

## 2. traffic Light System (The Signal)
We use the universal traffic light model with specific psychological contracts:

| State  | Meaning | Psychological Contract | UI Behavior |
| :--- | :--- | :--- | :--- |
| **GREEN** | **Nominal** | "You are safe. Focus on your work." | Passive. Static. |
| **YELLOW** | **Warning** | "Pay attention. Verification recommended." | **Active.** Subtle Pulse. Clickable. |
| **RED** | **Critical** | "Stop. Action required." | **Active.** Pulse. Clickable. |

## 3. The "Secret Door" (Affordance)
A warning text alone is often overlooked or misunderstood ("It's broken").
We use **Visual Affordance** (Animation/Pulse) to signal: *"This is not just an error message. It is a button. Use it to fix me."*

## 4. Honest but Safe
The system never lies about connection issues (honesty), but it always provides a "Retry" or "Settings" option immediately (safety). We do not leave the user in a dead end.
