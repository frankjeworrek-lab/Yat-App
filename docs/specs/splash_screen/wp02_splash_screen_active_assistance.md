# Work Package: Implement Active Assistance Splash Screen

**Objective:**  
Replace the generic loading sequence with an "Active Assistance" Splash Screen that communicates boot state and offers immediate solutions for startup issues.

## Scope of Work

### 1. UI Implementation (`main.py` / `ui_nicegui/splash.py`)
- [ ] **Create `SplashScreen` Component:** A dedicated UI overlay covering the screen.
- [ ] **State Styling:** Implement the Monochromatic Design Rules (Green/Blue/Orange/Red) defined in `splash_spec_v1.md`.
- [ ] **Action Buttons:** Add "Configure ➜" and "Retry ↻" buttons for Orange/Red states.

### 2. Logic Integration
- [ ] **Boot Check:** executing `LLMManager.initialize()` *while* the Splash Screen is visible.
- [ ] **Transition Logic:** 
    - Success -> `ui.open('/')` or fade out overlay.
    - Error -> Stay on Splash, enable buttons.

### 3. Verification
- [ ] **Test Case 1 (Good):** Normal boot -> Green -> App.
- [ ] **Test Case 2 (Empty):** No config -> Orange -> Clicking "Configure" opens Settings.
- [ ] **Test Case 3 (Error):** Corrupt config -> Red -> Retry.

## Reference
- **Spec:** [Splash Screen Spec v1](./splash_spec_v1.md)
