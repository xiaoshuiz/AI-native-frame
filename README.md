# 🚀 AI Native Frame — Frontend-First Edition

A frontend-first repository frame for AI-native product teams.
This version prioritizes UI delivery speed, specification-driven execution, and reliable CI/CD for modern web apps.

## ✨ What this version focuses on

- **Frontend as the main entry point**: `apps/web` (Vite + React + TypeScript)
- **Spec-first collaboration**: reusable templates for PRD, feature spec, tech spec, test plan, and release checklist
- **Clear delivery workflow**: GitHub Actions for lint/build, plus container build and publish
- **Readable documentation**: icon-enhanced docs for architecture, CI/CD, and spec lifecycle

## 🧱 Repository layout

```text
.
├── apps/
│   └── web/                           # Frontend app (Vite + React + TypeScript)
├── docs/
│   ├── ARCHITECTURE.md                # Frontend-first architecture guide
│   ├── CICD.md                        # CI/CD and release flow
│   ├── SPECS.md                       # Spec system overview
│   └── adr/
│       └── 0000-adr-template.md       # ADR template
├── specs/
│   ├── README.md                      # Spec lifecycle guide
│   └── templates/
│       ├── PRODUCT_REQUIREMENTS_TEMPLATE.md
│       ├── FEATURE_SPEC_TEMPLATE.md
│       ├── TECHNICAL_SPEC_TEMPLATE.md
│       ├── UI_UX_SPEC_TEMPLATE.md
│       ├── TEST_PLAN_TEMPLATE.md
│       └── RELEASE_CHECKLIST_TEMPLATE.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── pull_request_template.md
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── scripts/
│   └── bootstrap.sh
├── Dockerfile
├── docker-compose.yml
└── Makefile
```

## ⚡ Quick start

### 1) Bootstrap

```bash
./scripts/bootstrap.sh
```

### 2) Start frontend dev server

```bash
make dev
```

Open: `http://localhost:5173`

### 3) Run quality checks

```bash
make ci
```

### 4) Run with Docker

```bash
docker compose up --build
```

Open: `http://localhost:4173`

## 🔧 Framework policy

This repository is **frontend-first**, but **not framework-locked**.

- Current default: **Vite + React + TypeScript**
- You can migrate to **Next.js**, **Nuxt**, or other web frameworks
- The spec templates and CI structure are intentionally framework-agnostic

## 🧪 CI/CD snapshot

- **CI** (`.github/workflows/ci.yml`)
  - npm install
  - eslint
  - type-safe build
- **CD** (`.github/workflows/cd.yml`)
  - build frontend container image
  - publish to GHCR on `main`, `v*`, or manual dispatch
- **Dependabot**
  - weekly updates for npm and GitHub Actions

For details, see `docs/CICD.md`.

## 🗂️ Specification system

Use `specs/templates/` to standardize planning and delivery:

1. Product requirements
2. Feature spec
3. Technical spec
4. UI/UX spec
5. Test plan
6. Release checklist

For process guidance, see `specs/README.md`.

## 🧩 Backend status

Backend-related Python modules are kept in the repository as legacy reference,
but they are currently de-prioritized in this frontend-first edition.