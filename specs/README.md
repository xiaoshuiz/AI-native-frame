# 🗂️ Specs Workflow Guide

This project uses a **spec-first workflow** to reduce ambiguity and accelerate frontend delivery.

## 🧭 When to write a spec

Create a spec when a change:

- touches multiple pages or feature areas
- introduces non-trivial UI/UX behavior
- affects performance, security, or release risk
- requires cross-team alignment (PM, Design, Engineering)

## 🧱 Template map

- `PRODUCT_REQUIREMENTS_TEMPLATE.md`: business goals, scope, success criteria
- `FEATURE_SPEC_TEMPLATE.md`: feature behavior and acceptance criteria
- `TECHNICAL_SPEC_TEMPLATE.md`: architecture and implementation design
- `UI_UX_SPEC_TEMPLATE.md`: user flow, interaction details, and states
- `TEST_PLAN_TEMPLATE.md`: quality strategy and validation matrix
- `RELEASE_CHECKLIST_TEMPLATE.md`: launch readiness checklist

## 🔁 Suggested sequence

1. Product requirements
2. Feature spec
3. Technical spec + UI/UX spec
4. Test plan
5. Release checklist
6. ADR (if architecture-level decision is involved)

## 📎 PR requirement

Every medium/large PR should include:

- a link to the source spec file(s)
- explicit acceptance criteria mapping
- screenshots or recordings for UI changes
