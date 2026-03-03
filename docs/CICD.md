# 🔄 CI/CD for Frontend-First Delivery

## ✅ CI Pipeline (`.github/workflows/ci.yml`)

### 🚦 Triggers

- Every `push`
- Every `pull_request`

### 🛠️ Stages

1. Setup Node.js 22
2. Install dependencies (`npm ci` in `apps/web`)
3. Run lint checks (`npm run lint`)
4. Run type-safe production build (`npm run build`)

### 🎯 CI Intent

- Catch frontend quality issues early (lint + type/build checks)
- Keep pull requests merge-ready with a minimal and reliable gate

## 🚀 CD Pipeline (`.github/workflows/cd.yml`)

### 🚦 Triggers

- Push to `main`
- Push tags matching `v*`
- Manual trigger (`workflow_dispatch`)

### 🛠️ Stages

1. Login to GHCR
2. Generate Docker tags/labels from branch/tag/SHA
3. Build frontend image from `Dockerfile`
4. Push image to `ghcr.io`

### 🎯 CD Intent

- Provide traceable frontend artifacts for every important release path
- Keep release operations deterministic and scriptable

## 🔐 Dependency Governance (`.github/dependabot.yml`)

- Weekly updates for:
  - npm packages in `apps/web`
  - GitHub Actions workflow dependencies
- Keeps both runtime and delivery tooling current
