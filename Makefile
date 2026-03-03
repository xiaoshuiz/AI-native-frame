FRONTEND_DIR ?= apps/web

.PHONY: setup dev lint typecheck build preview ci

setup:
	npm --prefix $(FRONTEND_DIR) install

dev:
	npm --prefix $(FRONTEND_DIR) run dev

lint:
	npm --prefix $(FRONTEND_DIR) run lint

typecheck:
	npm --prefix $(FRONTEND_DIR) run typecheck

build:
	npm --prefix $(FRONTEND_DIR) run build

preview:
	npm --prefix $(FRONTEND_DIR) run preview

ci: lint build
