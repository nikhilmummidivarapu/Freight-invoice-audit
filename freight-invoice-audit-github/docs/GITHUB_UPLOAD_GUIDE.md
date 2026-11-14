# Push this project to GitHub

From the repository folder in CMD:

```cmd
git init
git add .
git status
```

Check that `.env` is NOT staged. If it is staged, remove it:
```cmd
git rm --cached .env
```

Then:
```cmd
git commit -m "Initial freight invoice audit project"
git branch -M main
```

Create an empty repository on GitHub and copy its HTTPS URL:
```cmd
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

If `origin` already exists, inspect it with `git remote -v` rather than adding it again.

Never commit `.env`, database passwords, private invoices or customer data.
