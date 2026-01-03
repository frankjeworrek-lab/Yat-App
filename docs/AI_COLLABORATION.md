# AI Collaboration Guidelines

## Core Principles

### 1. Isolated Tasks
- Execute **exactly** what is requested, nothing more
- No "while I'm at it..." improvements
- No preemptive fixes of related issues

### 2. Diagnostics Before Therapy
- **Understand** the problem first (add logging, investigate)
- Only **then** implement the fix
- Never bundle diagnosis and fix in one step

### 3. Test-Driven Workflow
1. AI makes commits (locally only)
2. **STOP** - Wait for user testing
3. User tests in dev environment
4. User gives explicit push approval
5. AI pushes to GitHub

### 4. Pre-Push Checklist
Before every push, the AI must:
1. Run `git status` - ensure nothing uncommitted
2. Ask: "All committed. Push approved?"
3. Wait for explicit "yes"
4. Then push + tag (if applicable)

### 5. No Assumptions
- If unclear: **Ask**, don't guess
- If multiple solutions exist: **Present options**, don't choose
- If a dependency is needed: **State it explicitly**

### 6. Incremental Changes
- One logical change = One commit
- Multiple related changes = Multiple sequential commits
- Never bundle unrelated changes

### 7. Error Recovery
- If a mistake is made: **Acknowledge it**
- Propose rollback or fix, don't auto-execute
- Let the user decide the recovery path

## Anti-Patterns (Learned the Hard Way)

### ❌ "While I'm at it" Syndrome
```
User: "Add debug logging"
AI:  - Adds logging
     - Fixes unrelated bug
     - Refactors 3 files
     - Updates docs
Result: Chaos, hard to test, unclear what broke
```

### ❌ Premature Optimization
```
User: "Why doesn't Windows build work?"
AI: Immediately rewrites entire plugin system
Result: Original bug masked, new bugs introduced
```

### ❌ Git Chaos
```
AI: Commits → Resets → Cherry-picks → Force-pushes
Result: Lost changes, confusion
```

## Success Patterns

### ✅ Focused Execution
```
User: "Add debug logging to plugin_loader.py"
AI:  1. Adds logging to discover_plugins()
     2. Commits
     3. STOPS, waits for test feedback
```

### ✅ Transparent Communication
```
AI: "I see two ways to fix this:
     Option 1: Simple, touches 1 file
     Option 2: Robust, touches 3 files
     Which do you prefer?"
```

### ✅ Clean Git History
```
Commit 1: "Add: Debug logging for plugin discovery"
Commit 2: "Add: Critical error badge for 0 plugins"
Commit 3: "Add: Reset utilities"
Each testable, each revertible
```

## Collaboration Mantras

1. **"One thing at a time"** - Resist the urge to "improve" everything
2. **"Ask first, code second"** - When in doubt, clarify
3. **"Test before push"** - The user tests, not GitHub Actions
4. **"Explicit over implicit"** - State assumptions, don't hide them

## Version
Document created: 2026-01-03
Based on: Real collaboration lessons from Y.A.T. development
