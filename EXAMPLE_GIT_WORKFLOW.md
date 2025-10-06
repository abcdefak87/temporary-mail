# 🚀 Example: Git Remote Branch Workflow

## Scenario: Adding New Feature

### Step 1: Run Git Manager
```bash
# Windows
GIT_COMMIT.bat

# Atau
python git_commit.py
```

### Step 2: Create Feature Branch
1. Pilih option **2** - "Create new branch and switch"
2. Masukkan nama: `feature/add-rules-documentation`
3. Branch akan dibuat dan auto switch

### Step 3: Make Your Changes
```bash
# Edit files sesuai kebutuhan
# Contoh: tambah ASSISTANT_RULES.md, QUICK_REFERENCE.md
```

### Step 4: Commit & Push
1. Di Git Manager, pilih option **1** - "Quick commit & push"
2. Sistem akan tampilkan changes
3. Masukkan commit message atau Enter untuk auto
4. Changes akan di-add, commit, dan push ke remote branch

### Step 5: Create Pull Request
1. Buka GitHub repository
2. Akan muncul notification untuk create PR
3. Review changes dan merge ke main

## 📝 Example Commands (Manual)

### A. Quick Workflow
```bash
# Create branch
git checkout -b feature/awesome-feature

# Make changes
# ... edit files ...

# Commit all
git add .
git commit -m "feat: add awesome feature"

# Push to remote
git push -u origin feature/awesome-feature
```

### B. Dengan Git Manager
```bash
python git_commit.py
# Pilih option 4: "Commit to new branch"
# Otomatis create branch + commit + push
```

## 🎯 Best Practice Workflow

### 1. Start New Day
```bash
git checkout main
git pull origin main
```

### 2. Create Feature Branch
```bash
git checkout -b feature/today-work
```

### 3. Work & Commit Regularly
```bash
# Setelah selesai satu bagian
git add .
git commit -m "feat: complete login UI"

# Setelah bagian lain
git add .
git commit -m "feat: add validation logic"
```

### 4. Push to Remote
```bash
git push origin feature/today-work
```

### 5. Create PR & Merge
- Via GitHub Web UI
- Or use GitHub CLI: `gh pr create`

## ⚡ Quick Tips

1. **Always branch** - Jangan langsung ke main
2. **Commit often** - Small commits lebih baik
3. **Clear messages** - Explain what & why
4. **Test before push** - Pastikan code works
5. **Review PR** - Check changes sebelum merge

---

**Remember**: Use `git_commit.py` for easier workflow! 🚀
