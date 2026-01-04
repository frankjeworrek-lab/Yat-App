# Work Package: Implement Active Assistance UI (Status Matrix v2)

**Objective:**  
Implement the comprehensive UI Status Matrix defined in `status_indicator_spec_v2.md` to provide "Active Assistance" and clear feedback to the user.

## Scope of Work

### 1. Code Implementation (`ui_nicegui/sidebar.py`)
- [ ] **Refactor `load_models`:** Replace existing implicit logic with explicit state detection mapped to Matrix IDs [G1]-[R6].
- [ ] **Implement "Assistance Mode":** For Orange/Red states, render text in the `Problem ➜ Solution` format with context prefix (`[Name]:`).
- [ ] **Create Helper `_update_status_badge`:** Centralize UI updates to enforce Generic Design Rules (Bubble Color matches Text Color).
- [ ] **Update `_handle_status_click`:** Implement the Blue Transition states [B1-B3] and the Smart Verification flow.
- [ ] **Smart G3 Detection:** Logic to detect "Active (from Memory)" if verification fails but models exist.

### 2. Cleanup
- [ ] **Remove Temporary Files:** Delete `docs/status_matrix_ids.md` (the printed one) and `tmp/`.
- [ ] **Gitignore:** Remove `tmp/` entry.

## Reference
- **Spec:** [Status Matrix v2](./status_indicator_spec_v2.md)
