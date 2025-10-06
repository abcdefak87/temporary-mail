# 🚀 Git Workflow dengan Remote Branch

## 📋 Quick Start

### Run Git Manager (Recommended)
```bash
# Windows
GIT_COMMIT.bat

# atau
python git_commit.py
```

## 🌿 Branch Strategy

### Main Branches
- `main` / `master` - Production ready code
- `develop` - Development integration branch
- `feature/*` - New features
- `fix/*` - Bug fixes
- `hotfix/*` - Emergency production fixes

### Naming Convention
```
feature/add-login-system
fix/email-validation-bug
hotfix/critical-security-patch
docs/update-readme
```

## 📝 Common Git Commands

### 1. Setup & Configuration
```bash
# Initialize repository
git init

# Add remote repository
git remote add origin https://github.com/username/repo.git

# Verify remote
git remote -v

# Configure user
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

### 2. Branch Management
```bash
# Create new branch
git branch feature/new-feature

# Switch branch
git checkout feature/new-feature

# Create and switch in one command
git checkout -b feature/new-feature

# List all branches
git branch -a

# Delete local branch
git branch -d feature/old-feature

# Delete remote branch
git push origin --delete feature/old-feature
```

### 3. Commit & Push Workflow
```bash
# Check status
git status

# Add all changes
git add .

# Add specific file
git add filename.py

# Commit with message
git commit -m "feat: add new login system"

# Push to remote branch
git push origin feature/new-feature

# Set upstream (first push)
git push -u origin feature/new-feature
```

### 4. Pull & Merge
```bash
# Pull latest from remote
git pull origin main

# Merge branch into current
git merge feature/new-feature

# Rebase (alternative to merge)
git rebase main
```

## 🔄 Typical Workflow

### A. New Feature Development
```bash
# 1. Create feature branch from main
git checkout main
git pull origin main
git checkout -b feature/awesome-feature

# 2. Make changes and commit
git add .
git commit -m "feat: implement awesome feature"

# 3. Push to remote
git push -u origin feature/awesome-feature

# 4. Create Pull Request on GitHub
# 5. After review, merge to main
```

### B. Bug Fix
```bash
# 1. Create fix branch
git checkout -b fix/bug-name

# 2. Fix the bug
# ... edit files ...

# 3. Commit and push
git add .
git commit -m "fix: resolve bug in email validation"
git push origin fix/bug-name

# 4. Create PR and merge
```

### C. Hotfix (Emergency)
```bash
# 1. Create from main/master
git checkout main
git checkout -b hotfix/critical-issue

# 2. Apply fix
git add .
git commit -m "hotfix: patch critical security issue"

# 3. Push immediately
git push origin hotfix/critical-issue

# 4. Merge to main AND develop
git checkout main
git merge hotfix/critical-issue
git push origin main

git checkout develop
git merge hotfix/critical-issue
git push origin develop
```

## 📊 Commit Message Format

### Conventional Commits
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Add/modify tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes

### Examples
```bash
# Simple
git commit -m "feat: add email validation"

# With scope
git commit -m "fix(auth): resolve login timeout issue"

# With description
git commit -m "refactor: optimize database queries

Reduced query count from 10 to 3
Improved page load time by 40%"
```

## 🔀 Merge Strategies

### 1. Merge Commit (Default)
```bash
git merge feature/branch
```
- Preserves complete history
- Creates merge commit
- Non-destructive

### 2. Squash and Merge
```bash
git merge --squash feature/branch
```
- Combines all commits into one
- Clean history
- Good for feature branches

### 3. Rebase and Merge
```bash
git rebase main
```
- Linear history
- No merge commits
- Cleaner but rewrites history

## ⚠️ Common Issues & Solutions

### 1. Merge Conflicts
```bash
# See conflicted files
git status

# Edit files to resolve conflicts
# Look for <<<<<<, ======, >>>>>>

# After resolving
git add .
git commit
```

### 2. Undo Last Commit (Not Pushed)
```bash
# Keep changes
git reset --soft HEAD~1

# Discard changes
git reset --hard HEAD~1
```

### 3. Update Fork
```bash
# Add upstream
git remote add upstream https://github.com/original/repo.git

# Sync fork
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### 4. Stash Changes
```bash
# Save current changes
git stash

# List stashes
git stash list

# Apply latest stash
git stash pop

# Apply specific stash
git stash apply stash@{2}
```

## 🔒 Best Practices

### Do's ✅
1. **Commit Often** - Small, logical commits
2. **Write Clear Messages** - Explain what and why
3. **Pull Before Push** - Avoid conflicts
4. **Review Before Commit** - Check `git diff`
5. **Use .gitignore** - Exclude unnecessary files
6. **Branch for Features** - Keep main clean

### Don'ts ❌
1. **Don't Force Push** - Unless absolutely necessary
2. **Don't Commit Secrets** - Use environment variables
3. **Don't Commit Large Files** - Use Git LFS
4. **Don't Work on Main** - Use feature branches
5. **Don't Ignore Conflicts** - Resolve properly

## 📁 .gitignore Template
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
venv/
env/
.env

# Node
node_modules/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Secrets
config/bot_config.json
*.key
*.pem

# Logs
*.log
logs/

# Database
*.db
*.sqlite
```

## 🚀 GitHub Actions (CI/CD)

### Basic Workflow
```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest
```

## 📱 GitHub CLI Commands
```bash
# Install: https://cli.github.com

# Create PR
gh pr create --title "Feature: New login" --body "Description"

# List PRs
gh pr list

# Check CI status
gh run list

# Create issue
gh issue create --title "Bug: Login fails"
```

## 🔗 Useful Links
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [Conventional Commits](https://www.conventionalcommits.org)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

**Pro Tip**: Use `git_commit.py` script for automated workflow! 🚀
