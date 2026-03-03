# 🏗️ Frontend-First Architecture

## 🎯 Goal

This repository now prioritizes fast frontend delivery for AI-native products.
The current baseline is optimized for **UI iteration speed**, **spec-driven implementation**, and **predictable release flow**.

## 🧱 Main Layers

### 1) 🌐 UI App Layer (`apps/web`)

- Vite + React + TypeScript application
- Component-driven and feature-oriented structure
- Fast local feedback loop (HMR + strict TypeScript)

### 2) 🧭 Spec Layer (`specs/`)

- Product and feature-level planning templates
- Technical, UI/UX, testing, and release templates
- Creates a shared language for PM, Design, and Engineering

### 3) 📝 Decision Layer (`docs/adr/`)

- Architecture Decision Records (ADR)
- Captures trade-offs and decision history over time
- Helps future contributors understand "why", not only "what"

### 4) 🔁 Delivery Layer (`.github/workflows/`)

- CI for lint and build checks
- CD for frontend container build + GHCR publish
- Dependabot for dependency freshness

## 🧩 Design Principles

- **Frontend-first, not framework-locked**: default is Vite, migration to other frameworks is allowed.
- **Spec before code**: templates are first-class artifacts, not optional attachments.
- **Automated quality gates**: every change should pass lint and build in CI.
- **Explicit decisions**: major architecture changes must come with an ADR.

## 🗺️ Evolution Path

1. Add module-level boundaries in `apps/web` (feature folders and shared packages).
2. Introduce visual regression and E2E tests.
3. Add optional BFF/API services when product complexity requires it.
4. Extend observability (frontend telemetry + release quality signals).
