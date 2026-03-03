# CI/CD 设计

## CI（`.github/workflows/ci.yml`）

触发条件：

- 任意 `push`
- 任意 `pull_request`

执行阶段：

1. 安装依赖（`pip install -e ".[dev]"`）
2. 代码质量检查（`ruff check` + `ruff format --check`）
3. 类型检查（`mypy src`）
4. 单元测试（`pytest`）
5. Eval 冒烟（`python -m ai_native_frame.evals.runner ...`）

目标：

- 对语法、风格、类型、基础行为、最小效果做统一门禁；
- 把 AI 工程的评测流程纳入标准 CI。

## CD（`.github/workflows/cd.yml`）

触发条件：

- `main` 分支 push
- `v*` tag push
- 手动触发（`workflow_dispatch`）

执行阶段：

1. 登录 GHCR
2. 生成镜像 metadata（branch/tag/sha/latest）
3. 构建并推送 Docker 镜像

目标：

- 固化产物版本，保证可追溯；
- 让分支/Tag 到镜像发布的路径标准化。

## 依赖治理（`.github/dependabot.yml`）

- 每周自动检查 `pip` 与 `github-actions` 更新；
- 保持基础依赖与 CI action 版本健康。
