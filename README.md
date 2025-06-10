# Mini Blog Demo – AI Coding Agent Playground

Created on 2025-06-10T00:49:05.495925 UTC.

## Features
* **FastAPI** + in‑memory DB (dict) – zero external deps.
* **3 intentionally failing tests** to showcase bug‑fixing:
  1. **crud.py** – wrong dict key (`posts[slug]`)
  2. **services.py** – `user.posts` may be `None`
  3. **api.py** – missing `await` (will raise `RuntimeWarning` / 500)

* **2 refactor missions** (both currently **TODO**, tests will need edits after you refactor):
  1. **Unify `Post` and `Article`** models into one.
  2. Rename `User.email` → `User.contact_email` across codebase & tests.

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install fastapi uvicorn[standard] pytest
uvicorn mini_blog.api:app --reload  # dev server
pytest -q                           # 3 failures expected
```

Happy hacking! 🎉