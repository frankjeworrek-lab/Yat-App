# Work Package: Future Guideline Handling & Restructuring

**Objective:**  
Refactor the monolithic `AI_COLLABORATION.md` into a modular system to ensure **Portability** and **Transferability**. The goal is to separate universal "Lessons Learned" (Core) from specific implementation details, allowing the Core Guidelines to be dropped into any new software project as a mature starting point.

**EXECUTION RULE (STAGE-GATE):**  
This Work Package must be executed sequentially. The AI must **STOP and ask for approval** after each Phase before proceeding to the next.

## Scope of Work (Defined Draft)

### Phase 1: Deep Audit & Analysis
- [ ] **Content Audit:** Scan `AI_COLLABORATION.md` for consistency (Logical contradictions, redundancies).
- [ ] **Structural Analysis:** Tag every section as either:
    - **CORE:** Universal principles (e.g., "Diagnose before Fix", "Work Package Protocol"). *Keep this clean for export.*
    - **PROJECT:** Context-specific rules (e.g., "Auto Download Builds", "NiceGUI specifics"). *Keep this local.*
- [ ] **GATE:** Present Analysis -> Wait for User Approval.

### Phase 2: Refactoring & Directory Decoupling
- [ ] **Legacy Preservation (Safety Net):** Archiving `AI_COLLABORATION_LEGACY_v1.md`.
- [ ] **Directory Strategy:** Create `docs/guidelines/core/` and `docs/guidelines/project/`.
- [ ] **Content Split:** Migrate content into the new files.
- [ ] **GATE:** Present New Structure -> Wait for User Approval.

### Phase 3: Self-Explanation & Philosophy
- [ ] **Core Preamble:** Add "Philosophy", "Benefit", and "Usage" sections to `Agantic_CORE.md`.
- [ ] **GATE:** Present Preamble Text -> Wait for User Approval.

### Phase 4: The "Living Constitution" Protocols
- [ ] **The "Guardian" Protocol (Intelligent Change Analysis):** AI Smart Routing (Core vs Project).
- [ ] **Validation Protocol:** Consistency Checks.
- [ ] **Evolution Protocol:** Override rules.
- [ ] **Final SEAL:** Wait for final User Sign-off.

## Reference
- Baseline: `AI_COLLABORATION.md` (Current Version)
