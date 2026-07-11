# Invoice App

Small internal service that generates customer invoices and stores them in S3.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Configuration lives in `.env` (AWS credentials, database URL).

## Roadmap
- [ ] PDF templates
- [ ] Email delivery
- [ ] Move secrets out of .env
