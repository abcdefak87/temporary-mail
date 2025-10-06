# Quick Reference Guide

## 🎯 Core Principles
1. **Safety First** - Never compromise data or system security
2. **Read Before Edit** - Always understand existing code
3. **Test Everything** - Verify changes work as expected
4. **Document Clearly** - Make code self-explanatory

## 🛠️ Essential Commands

### File Operations
```bash
# Find files
find_by_name -Pattern "*.py" -SearchDirectory /path

# Search content
grep_search -Query "function_name" -SearchPath /path

# Read files
Read -file_path /full/path/to/file.py

# Edit files
MultiEdit for multiple changes
Edit for single changes
```

### Project Setup
```bash
# Python
python -m venv venv
pip install -r requirements.txt

# Node.js
npm install
npm run dev

# Git
git init
git add .
git commit -m "message"
```

## 📁 Standard Project Structure
```
project/
├── src/            # Source code
├── tests/          # Unit tests
├── docs/           # Documentation
├── config/         # Configuration
├── scripts/        # Utilities
├── .env            # Environment variables
├── .gitignore      # Git ignore rules
├── README.md       # Project overview
└── requirements.txt # Dependencies
```

## 🔒 Security Checklist
- [ ] No hardcoded credentials
- [ ] Input validation implemented
- [ ] Sensitive files in .gitignore
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CORS configured properly

## 🐛 Debugging Steps
1. **Reproduce** - Understand the problem
2. **Log** - Add print/console statements
3. **Isolate** - Find exact failure point
4. **Fix** - Address root cause
5. **Test** - Verify solution works
6. **Document** - Update comments/docs

## 📝 Code Review Checklist
- [ ] Follows naming conventions
- [ ] Has error handling
- [ ] Includes necessary comments
- [ ] No duplicate code
- [ ] Passes all tests
- [ ] Performance acceptable
- [ ] Security considered

## 🚀 Deployment Checklist
- [ ] Environment variables set
- [ ] Dependencies installed
- [ ] Database migrations run
- [ ] Tests passing
- [ ] Logs configured
- [ ] Monitoring enabled
- [ ] Backup created

## ⚡ Performance Tips
1. **Profile First** - Measure before optimizing
2. **Cache Results** - Store expensive computations
3. **Async I/O** - Use for network/file operations
4. **Batch Operations** - Process in groups
5. **Index Databases** - Speed up queries

## 🔧 Common Fixes

### Python
```python
# Virtual environment issues
python -m pip install --upgrade pip
pip cache purge

# Import errors
sys.path.append('/path/to/module')
```

### JavaScript
```javascript
// Async handling
await Promise.all([...])
try/catch for error handling

// Memory leaks
Remove event listeners
Clear intervals/timeouts
```

### Git Remote Branch Workflow
```bash
# Use automated tool (RECOMMENDED)
python git_commit.py
# atau Windows: GIT_COMMIT.bat

# Quick commit to current branch
git add .
git commit -m "feat: your message"
git push origin branch-name

# Create and push new branch
git checkout -b feature/new-feature
git push -u origin feature/new-feature

# Switch branches
git checkout branch-name

# Pull latest
git pull origin main

# Merge branch
git merge feature/branch

# Delete branch
git branch -d local-branch
git push origin --delete remote-branch

# Undo last commit
git reset --soft HEAD~1

# Fix merge conflicts
git status
# Edit conflicted files
git add .
git commit
```

## 📊 Testing Commands
```bash
# Python
pytest -v
pytest --cov=src

# JavaScript
npm test
npm run test:coverage

# General
curl http://localhost:8000/api/test
```

## 🎨 Code Style

### Python (PEP 8)
- 4 spaces indentation
- snake_case for functions
- PascalCase for classes
- UPPER_CASE for constants

### JavaScript
- 2 spaces or tabs
- camelCase for variables
- PascalCase for classes
- UPPER_SNAKE_CASE for constants

## 📚 Documentation Template

### Function Documentation
```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description.
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Description of return value
    
    Raises:
        ExceptionType: When it occurs
    """
```

## 🆘 Emergency Procedures
1. **Stop all operations**
2. **Assess damage/impact**
3. **Create backup if possible**
4. **Notify user immediately**
5. **Provide recovery options**

---

*Keep this reference handy for quick access to common patterns and procedures.*
