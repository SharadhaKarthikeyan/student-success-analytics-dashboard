# GitHub Upload Instructions

Follow these steps to upload your project to GitHub for the first time.

## 1. Initial Local Git Setup
Open your terminal (Command Prompt, PowerShell, or Git Bash) in your project folder:

1. **Initialize Git Repository:**
   ```bash
   git init
   ```

2. **Check Status:** (Check that your `.gitignore` is working)
   ```bash
   git status
   ```

3. **Stage All Files:**
   ```bash
   git add .
   ```

4. **Commit the Changes:**
   ```bash
   git commit -m "Initial commit: Student Success Analytics Dashboard"
   ```

5. **Set Main Branch:**
   ```bash
   git branch -M main
   ```

## 2. Connect to GitHub
1. Go to your [GitHub account](https://github.com/).
2. Create a **New Repository**.
3. Name it: `student-success-analytics-dashboard`.
4. Leave it Public and do **not** initialize with README, license, or .gitignore (you already have them).
5. Copy the **Remote Repository URL** (it looks like `https://github.com/your-username/student-success-analytics-dashboard.git`).

## 3. Push to GitHub
1. **Add Remote Origin:**
   ```bash
   git remote add origin <your-repository-url>
   ```

2. **Push Your Code:**
   ```bash
   git push -u origin main
   ```

---

## Common Issues & Fixes

### If git says "remote origin already exists":
Run this to update it to the new URL:
```bash
git remote set-url origin <your-repository-url>
```

### If you get a "permission denied" or "authentication failed" error:
If you haven't set up your GitHub credentials on this machine, you may need to use a [GitHub Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) instead of a password, or use the [GitHub Desktop](https://desktop.github.com/) app for an easier visual experience.
