# Work Package: UI Status System Refinement

**Objective:**  
Refine the UI Status System to appeal to professional users, balancing "Active Assistance" with a cleaner, more serious aesthetic. Also, unify the right-side controls with premium micro-interactions.

## Scope of Work (Molding Phase)

### 1. Visual Layout Refinement (Status Left)
- [ ] **Left Alignment:** The status indicator must be strictly left-aligned.
- [ ] **Isolation:** Visually decouple the status from the Model Dropdown/Form. It should stand as a dedicated system line.
- [ ] **Seriousness:** Reduce background noise. Use "Outline" or "Ghost" styles instead of filled bubbles.

### 2. Right-Side Unification (Eye-Catchers)
- [ ] **Uniformity:** All right-side actions (Refresh, Add Chat, Settings Link) must share a consistent visual language (Size, Color, Opacity).
- [ ] **Visibillity First:** Controls must be clearly visible in their resting state ("No Mystery Meat Navigation"). Avoid fully transparent "Ghost Buttons" that disappear.
- [ ] **Micro-Interactions (The Cherry on Top):** Implement subtle animations on hover (e.g., rotation, scale, color-shift).
- [ ] **Scenario-Driven Animations (The Eye-Catcher):** Icons should animate to reflect active system state, not just user interaction.
    - *Example:* "Refresh" button spins continuously *while* fetching models.
    - *Example:* "Status" icon pulses gently if action is required (Orange/Red state).
    - *Goal:* Motion conveys meaning.

### 2. Implementation Strategy
- [ ] **Markup:** Move the status row out of the `Model Configuration` container.
- [ ] **Styling:** Update CSS classes in `sidebar.py`.

## Reference
- Base: [WP01 Implementation](./wp01_implement_active_assistance_ui.md)
- Spec: [Status Matrix v2](./status_indicator_spec_v2.md)
