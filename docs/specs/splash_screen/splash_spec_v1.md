# Splash Screen & Boot Sequence (Spec v1)
> Concept: "Active Assistance" from the very first second.

## 🎯 Objective
The Splash Screen is not just a branding element; it is the **First System Check**. It must communicate the application state immediately using the **Active Assistance** design language (Monochromatic, Action-Oriented).

## 🎨 Design Rules (Inherited from Status Matrix v2)
*   **Monochromatic:** The entire Splash Screen background/theme shifts color based on state (Subtle Gradient or Accent).
*   **Truthful:** It shows exactly what is loading (`Loading Providers...`, `Verifying Keys...`).
*   **Actionable:** If boot fails, it offers a **Solution Button** immediately (no dead ends).

## 🔄 State Matrix (Boot Phase)

### 🔵 Phase 1: Initialization (Blue)
*   **Visual:** Clean Dark Background, Pulsing Logo.
*   **Status Text:**
    *   `Initializing System...`
    *   `Loading Plugins...`
    *   `Verifying [Name]...`
*   **Action:** None (Wait).

### 🟢 Phase 2: Success (Green)
*   **Visual:** Green Accent Glow.
*   **Status Text:** `✓ System Operational`
*   **Transition:** Auto-fades to Main App after 0.5s.

### 🟠 Phase 3: Setup Required (Orange)
*App runs, but needs user input to be useful.*
*   **Scenario:** No providers configured, or first run.
*   **Visual:** Orange Accent, Static.
*   **Message:** `Welcome to Y.A.T.`
*   **Assistance Action:** `[ Button: Configure Providers ➜ ]`
    *   *Clicking this opens the Settings Dialog directly.*

### 🔴 Phase 4: Boot Error (Red)
*Critical failure preventing app start.*
*   **Scenario:** Port blocked, Config corrupt, No Plugins.
*   **Visual:** Red Accent, Warning Icon.
*   **Message:** `System Start Failed`
*   **Context:** `Error: Port 8080 in use` (Example)
*   **Assistance Action:** `[ Button: Retry ↻ ]` or `[ Button: Reset App 🛠️ ]`

## 🛠 Integration logic
1.  **App Start:** Show Native Window (PyWebView) or Browser Overlay.
2.  **Run Checks:** `LLMManager.initialize()`
3.  **Result:**
    *   If **Active/Green:** Fade out -> Show Chat.
    *   If **Orange/Red:** Stay open, show Action Button.

## 📝 Work Package Reference
To be implemented in `wp02_implement_splash_screen.md`.
