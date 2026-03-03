# 🤝 Contributing Guide

## ⚙️ 1. Local setup

```bash
./scripts/bootstrap.sh
make dev
```

## ✅ 2. Checks before opening a PR

```bash
make ci
```

## 🧱 3. Repository conventions

- `apps/web/`: frontend application code
- `docs/`: architecture, CI/CD, and decision records
- `specs/`: product/feature/technical/testing templates
- `.github/`: CI workflows and collaboration templates

## 📝 4. Spec-first workflow

Before large implementation work:

1. Start from a file in `specs/templates/`
2. Fill product and feature context
3. Add technical decisions and risks
4. Link the spec in your PR description

## 🧾 5. Commit and PR rules

- Keep each commit focused on one logical change
- Include screenshots or recordings for UI changes
- Include an ADR when changing architecture-level decisions
