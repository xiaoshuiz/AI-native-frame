#!/usr/bin/env bash
set -euo pipefail

npm --prefix apps/web ci

cp -n .env.example apps/web/.env.local || true

echo "Bootstrap completed."
echo "Run: npm --prefix apps/web run dev"
