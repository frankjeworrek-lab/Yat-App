# Y.A.T. Status Matrix (Specification v2)
> FINAL CONCEPT. READY FOR IMPLEMENTATION.

## 🎨 Generic Design Rules (The "Active Assistance" Look)

### 1. Monochromatic Harmony
The text color MUST always match the bubble's base color group to ensure high contrast and a clean, premium look.
*   **Green States:** Base `green-900` + Text `text-green-400`
*   **Blue States:** Base `blue-900` + Text `text-blue-400`
*   **Orange States:** Base `orange-900` + Text `text-orange-400`
*   **Red States:** Base `red-900` + Text `text-red-400`
*   *(Exception: Critical Failure uses a darker/blacker background for drama)*

### 2. Contextual Clarity
*   **Placeholder `[Name]`:** Whenever a status refers to a specific provider (e.g. Mistral, OpenAI), the provider's name MUST be prefixed.
    *   *Format:* `[Name]: [Message] ➜ [Action]`
*   **Global States:** If no provider is selected or the system is broken globally, no prefix is used.

### 3. Action-Oriented Text (Assistance)
*   For **Warning** and **Error** states, the text MUST follow the pattern: `Problem ➜ Solution`.
*   The arrow (`➜`) signifies that clicking the badge will trigger the solution.

---

## 🟢 ACTIVE / TRUSTED (Green)
*System is operational. Trust is established.*

*   **[G1] Active Healthy:**
    *   Text: `Active: [Name]`
    *   Style: 🔵 `bg-green-900/30` | 🟢 `text-green-400`
    *   Icon: `circle` ⬤
*   **[G2] Verified Success:**
    *   Text: `✓ Verified: Operational`
    *   Style: 🔵 `bg-green-900/40` | 🟢 `text-green-300`
    *   Icon: `check_circle` 🟢
*   **[G3] Active (Cached):**
    *   Text: `Active (from Memory)`
    *   Style: 🔵 `bg-green-900/20` | 🟢 `text-green-500`
    *   Icon: `save` 💾

## 🔵 PROCESS / TRANSITION (Blue)
*System is working for you. Please wait.*

*   **[B1] Connecting:**
    *   Text: `Connecting to [Name]...`
    *   Style: 🔵 `bg-blue-900/40` | 🔵 `text-blue-400`
    *   Icon: `sync` (spin) 🔄
*   **[B2] Verifying:**
    *   Text: `Verifying Status...`
    *   Style: 🔵 `bg-blue-900/40` | 🔵 `text-blue-400`
    *   Icon: `search` (spin) 🔍
*   **[B3] Downloading:**
    *   Text: `Downloading Model...`
    *   Style: 🔵 `bg-blue-900/40` | 🔵 `text-blue-400`
    *   Icon: `download` (bounce) ⬇️

## 🟠 WARNING / ASSISTANCE (Orange)
*Problem detected. Action proposed.*

*   **[O1] Setup Needed:**
    *   Text: `[Name]: Setup Needed ➜ Configure`
    *   Style: 🔵 `bg-orange-900/40` | 🟠 `text-orange-400`
    *   Icon: `settings` (pulse) ⚙️
*   **[O2] Partial Config:**
    *   Text: `[Name]: Invalid Config ➜ Fix It`
    *   Style: 🔵 `bg-orange-900/40` | 🟠 `text-orange-400`
    *   Icon: `tune` 🎚️
*   **[O3] Empty Models:**
    *   Text: `[Name]: No Models ➜ Refresh`
    *   Style: 🔵 `bg-orange-900/40` | 🟠 `text-orange-400`
    *   Icon: `folder_off` 📂
*   **[O4] No Provider:**
    *   Text: `No Provider ➜ Select One`
    *   Style: 🔵 `bg-orange-900/30` | 🟠 `text-orange-400`
    *   Icon: `touch_app` (pulse) 👆
*   **[O5] Rate Limit:**
    *   Text: `[Name]: Limit Reached ➜ Wait`
    *   Style: 🔵 `bg-orange-900/40` | 🟡 `text-amber-400`
    *   Icon: `hourglass_full` ⏳

## 🔴 ERROR / EMERGENCY (Red)
*System halted. Immediate intervention required.*

*   **[R1] Auth Failed:**
    *   Text: `[Name]: Auth Failed ➜ Edit Key`
    *   Style: 🔵 `bg-red-900/40` | 🔴 `text-red-500`
    *   Icon: `lock` (pulse) 🔒
*   **[R2] Connection Lost:**
    *   Text: `[Name]: Connection Lost ➜ Retry`
    *   Style: 🔵 `bg-red-900/40` | 🔴 `text-red-500`
    *   Icon: `wifi_off` (pulse) 📶
*   **[R3] API Error:**
    *   Text: `[Name]: API Error ➜ Retry`
    *   Style: 🔵 `bg-red-900/40` | 🔴 `text-red-500`
    *   Icon: `cloud_off` (pulse) ☁️
*   **[R4] System Error:**
    *   Text: `[Name]: Crash ➜ Review Log`
    *   Style: 🔵 `bg-red-900/50` | 🔴 `text-red-400`
    *   Icon: `bug_report` 🐞
*   **[R5] Quota Exceeded:**
    *   Text: `[Name]: Quota Exceeded ➜ Plan`
    *   Style: 🔵 `bg-red-900/40` | 🔴 `text-red-400`
    *   Icon: `payments` 💲
*   **[R6] CRITICAL FAILURE:**
    *   Text: `Critical Failure ➜ Help`
    *   Style: ⚫ `bg-red-950` | 🔴 `text-red-600`
    *   Icon: `dangerous` (pulse) 💀
