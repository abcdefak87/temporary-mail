# 📊 Git Visual Commit Rules

## 🎯 Core Principle
**EVERY commit MUST display branch graph visualization** 

## 📋 Mandatory Rules

### 1. Always Use Visual Tools
```bash
# ✅ CORRECT - Use visual tools
python git_visual.py
GIT_VISUAL.bat
git cv  # commit visual alias

# ❌ WRONG - Plain commits without visualization
git commit -m "message"  # NO VISUAL
```

### 2. Commit Message Format
All commits MUST follow semantic format:
```
type(scope): description

# Examples:
feat(auth): add login functionality
fix(api): resolve timeout issue
docs: update README
```

### 3. Required Visual Display After Actions

#### After Every Commit:
```bash
git graph -10  # Show last 10 commits with graph
```

#### After Every Push:
```bash
git graph --all -15  # Show all branches
```

#### After Every Merge:
```bash
git tree  # Show full tree structure
```

## 🛠️ Setup Requirements

### Initial Configuration (ONE TIME)
```bash
# Run setup
python git_visual.py setup

# Or manually set aliases
git config --global alias.graph "log --graph --pretty=format:'%C(auto)%h%d %C(blue)%ar %C(green)%an%C(reset) %s' --all"
git config --global alias.lg "log --color --graph --pretty=format:'%C(auto)%h%d %C(blue)%ar %C(green)%an%C(reset) %s' --abbrev-commit --all"
```

## 📊 Visual Formats

### Standard Graph View
```
* af3e707 (HEAD -> feature/branch) 2 hours ago Developer feat: add feature
|\
| * b2c3d4e (origin/main) 3 hours ago Developer fix: bug fix
|/
* e5f6g7h 4 hours ago Developer docs: update
```

### Tree View with Decorations
```
* commit-hash - (2 hours ago) message - author (HEAD -> branch-name)
|\
| * commit-hash - (3 hours ago) message - author (origin/main)
|/
* commit-hash - (4 hours ago) message - author
```

## 🔄 Workflow Rules

### 1. Feature Development
```bash
# Create branch with visual
git checkout -b feature/name
git graph -5  # MANDATORY: Show graph

# Commit with visual
python git_visual.py  # Use option 1
# OR
git add .
git commit -m "feat: description"
git graph -10  # MANDATORY: Show result

# Push with visual
git push origin feature/name
git graph --all  # MANDATORY: Show all branches
```

### 2. Daily Work Start
```bash
# MANDATORY morning routine
git fetch --all
git graph --all -20  # See overnight changes
git status
```

### 3. Before Any Merge
```bash
# MANDATORY pre-merge check
git graph --all  # Visualize branch positions
git checkout main
git merge feature/branch
git tree  # Show merged result
```

## 📌 Commit Type Rules

| Type | When to Use | Symbol |
|------|------------|--------|
| feat | New feature | ✨ |
| fix | Bug fix | 🐛 |
| docs | Documentation | 📚 |
| style | Formatting | 💎 |
| refactor | Code restructuring | 📦 |
| test | Add tests | 🚨 |
| chore | Maintenance | 🔧 |
| perf | Performance | ⚡ |
| ci | CI/CD changes | 👷 |
| revert | Revert commit | ⏪ |

## 🚫 Prohibited Actions

1. **NEVER** commit without showing graph
2. **NEVER** push without visual confirmation
3. **NEVER** merge without seeing branch structure
4. **NEVER** use generic commit messages
5. **NEVER** skip the visual verification

## ⚡ Quick Commands

### Instant Visual Commit
```bash
# One command does everything
git cv
```

### Quick Status + Graph
```bash
git sg  # status + graph
```

### Commit + Graph
```bash
git cg  # add + commit + graph
```

### Push + Graph
```bash
git pg  # push + graph
```

## 📊 Visual Indicators

### Branch Status Symbols
- `*` Current commit
- `|\` Branch divergence  
- `|/` Branch convergence
- `(HEAD ->)` Current position
- `(origin/)` Remote branch
- `(tag:)` Tagged commit

### Color Meanings
- 🟡 Yellow: Current branch
- 🟢 Green: Remote branches
- 🔵 Blue: Time/Author info
- 🔴 Red: Branch decorations
- ⚪ White: Commit messages

## 🎯 AI Assistant Rules

As an AI assistant, I MUST:

1. **Always use visual commit tools** when making commits
2. **Show graph after every git operation**
3. **Include graph output in responses** when discussing commits
4. **Enforce semantic commit messages**
5. **Educate about branch visualization**

### Example AI Response:
```markdown
I've committed your changes:

📊 Git Graph:
* a1b2c3d (HEAD -> feature/new) just now AI feat: add new feature
* d4e5f6g (origin/main) 2 hours ago User fix: bug fix
* g7h8i9j 3 hours ago User docs: update

✅ Changes pushed to origin/feature/new
```

## 🔧 Troubleshooting

### Graph Not Showing?
```bash
# Reset aliases
python git_visual.py setup

# Check git version
git --version  # Need 2.0+

# Manual graph
git log --graph --oneline --all
```

### Colors Not Working?
```bash
# Windows
set TERM=xterm-256color

# Enable colors
git config --global color.ui auto
```

## 📝 Commit Message Examples

### ✅ GOOD Examples
```bash
feat(auth): implement OAuth2 login with Google
fix(api): handle null response in user endpoint  
docs: add API documentation for v2 endpoints
refactor(database): optimize query performance
test: add unit tests for payment module
```

### ❌ BAD Examples
```bash
update files  # Too vague
fixed stuff  # No context
changes  # Meaningless
wip  # Not descriptive
.  # Just no
```

## 🚀 Implementation Checklist

- [ ] Run `python git_visual.py setup`
- [ ] Set commit message template
- [ ] Configure visual aliases
- [ ] Test graph display
- [ ] Practice visual workflow
- [ ] Review color settings
- [ ] Verify branch display

---

**Remember**: NO COMMIT WITHOUT VISUAL! 📊
