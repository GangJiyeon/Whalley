## Overview
Briefly describe what this PR does.

- [ ] New Feature
- [ ] Bug Fix
- [ ] Backend Update (FastAPI)
- [ ] Frontend Update (Next.js)
- [ ] API Change
- [ ] DB / Schema Change (PostgreSQL / Alembic)
- [ ] Caching / Redis Change
- [ ] PWA / Notifications
- [ ] i18n / Timezone / Localization
- [ ] Documentation
- [ ] Refactoring
- [ ] Other (describe below)

---

## Scope
Which part(s) of the monorepo are affected?

- `backend/`
- `frontend/`
- Both

---

## Backend (FastAPI)

### Changes
Describe all backend changes here.

- 
- 

### API Changes
List added/updated/removed endpoints.

| Method | Endpoint             | Description           | Breaking? |
|--------|----------------------|-----------------------|-----------|
| GET    | /api/...             |                       | Yes/No    |
| POST   | /api/...             |                       | Yes/No    |

### DB / Alembic
Describe schema changes and migrations.

- Migration file(s): `backend/alembic/versions/xxxx_.py`
- `alembic upgrade head` result:
- `alembic downgrade` tested? (Yes/No)

### Caching / Redis
If Redis or cache is touched, describe it.

- New keys or patterns (e.g. `whalley:country:…`):
- TTL / eviction strategy:
- Invalidation logic:

### Notifications / Background Tasks (if any)
- 

### Backend Notes
Anything reviewers should pay attention to (security, performance, edge cases)?

-  

---

## Frontend (Next.js)

### Changes
Describe pages, components, hooks, etc.
