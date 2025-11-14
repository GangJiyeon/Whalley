

# Whalley 🐳

> **A Work & Holiday community platform for global workers and travelers.**
> Built with **FastAPI (Python)** and **Next.js (React/TypeScript)**.

Whalley provides visa information, checklists, community posts, and real-time features for people preparing for or currently on a Work & Holiday experience across various countries such as Australia, Japan, Canada, the UK, and the United States.

---

## 🚀 Tech Stack

### **Backend**

* Python, FastAPI, Uvicorn
* PostgreSQL
* SQLAlchemy 2.x + Alembic
* Redis (caching, ranking, notifications)
* Pydantic v2
* Pytest

### **Frontend**

* Next.js (React, TypeScript)
* Tailwind CSS + shadcn/ui
* TanStack Query
* Internationalization (KR/EN and more)

### **DevOps**

* Docker & Docker Compose
* GitHub Actions (CI)
* Deployment: *TBD* (Vercel, Railway, Fly.io, AWS, etc.)

---

## 🎯 Project Goals

Whalley aims to provide a reliable, community-driven platform for Work & Holiday travelers by offering:

* **Country-specific visa information** and personalized checklists
* **Experience posts, Q&A, and comments** to share real stories
* **Bookmarking and push/PWA notifications**
* **Timezone-aware and multilingual UX** for global accessibility

---

## 📁 Monorepo Structure

```
whalley/
├── backend/      # FastAPI application
├── frontend/     # Next.js application
└── README.md
```

* `backend/`: API server, database models, routes, services, tests
* `frontend/`: User-facing web app, UI components, i18n, API calls

---

## 📌 Status

🚧 **Under active development**
Initial backend & frontend setup in progress.


