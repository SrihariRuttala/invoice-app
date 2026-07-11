# Demo setup — the leaked key (do this BEFORE the workshop)

**Goal:** plant a *fake* AWS key in a public repo, let bots find it, show the alerts live.
**Safe:** the key is a canary token — it can't access anything or cost you money. It only tells you when someone tries it.

## Steps

1. **Get the fake key**
   - Go to **canarytokens.org**
   - Token type: **AWS API key**
   - Enter your email → **Create**
   - Copy the **access key** and **secret** it gives you

2. **Put it in the repo**
   - Open `.env`
   - Replace `PASTE_YOUR_CANARYTOKEN_AWS_KEY_HERE` and `PASTE_YOUR_CANARYTOKEN_SECRET_HERE` with the canary values

3. **Push to a PUBLIC GitHub repo**
   ```bash
   cd invoice-app
   git init && git add -A && git commit -m "initial commit"
   gh repo create invoice-app --public --source=. --push
   ```
   (or create the repo on github.com and push — just make sure it's **public**)

4. **Wait & screenshot**
   - Within minutes–hours you'll get alert emails: IP, location, time, user-agent
   - Screenshot 2–3 of them as backup in case the wifi fails

## During the demo
1. Show the repo — key sitting in `.env`
2. Open your inbox — show the alerts that already arrived
3. (optional) Run `gitleaks detect --source . -v` → red "secret found" output
4. Land it: "This is why secrets belong in a vault, never in code." → Door 2

## After
- Delete the repo.
- **Never** do this with a real key.
