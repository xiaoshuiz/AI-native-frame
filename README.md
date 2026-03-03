# AI Native Frame (示例仓库骨架)

一个面向 **AI-native 项目** 的可运行模板仓库，覆盖以下关键能力：

- 代码分层（API / Workflow / Agent / LLM Provider）
- PromptOps（`prompts/` 文件化管理）
- EvalOps（`evals/` 数据集 + 自动评测）
- CI/CD（GitHub Actions：质量门禁 + 镜像发布）
- 本地与容器化运行（`Makefile` + `Dockerfile` + `docker-compose`）

> 默认使用 `mock` provider，零密钥即可跑通全链路；也可切换到 OpenAI provider。

---

## 1. 快速开始

### 1.1 本地运行

```bash
./scripts/bootstrap.sh
source .venv/bin/activate
cp -n .env.example .env
uvicorn ai_native_frame.api:app --reload --host 0.0.0.0 --port 8000
```

### 1.2 运行质量门禁

```bash
make ci
```

### 1.3 Docker 运行

```bash
cp -n .env.example .env
docker compose up --build
```

---

## 2. 目录结构（推荐分布）

```text
.
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── configs/
│   ├── agents/research.yaml
│   └── workflows/research_pipeline.yaml
├── docs/
│   ├── ARCHITECTURE.md
│   └── CICD.md
├── evals/
│   └── datasets/sample_tasks.jsonl
├── prompts/
│   ├── system/research.md
│   └── tasks/research_task.md
├── scripts/
│   └── bootstrap.sh
├── src/ai_native_frame/
│   ├── agents/
│   ├── evals/
│   ├── llm/
│   ├── workflows/
│   ├── api.py
│   ├── config.py
│   └── prompts.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── pyproject.toml
```

---

## 3. 核心设计说明

1. **Provider 抽象**：`llm/` 下统一接口，便于切换 `mock/openai/其他`。
2. **Workflow 编排层**：避免 API 直接耦合 Agent 细节。
3. **Prompt 文件化**：Prompt 可审查、可回滚、可和代码一起评审。
4. **Eval 冒烟门禁**：不仅验证“跑得起来”，也验证“输出最小可用”。
5. **CI/CD 一体化**：代码合入后自动检查，主干自动产出镜像。

---

## 4. API 示例

### Health Check

```bash
curl -s http://127.0.0.1:8000/health | jq
```

### Research Task

```bash
curl -s -X POST http://127.0.0.1:8000/v1/tasks/research \
  -H "Content-Type: application/json" \
  -d '{
    "query":"How should we design AI native repo frame?",
    "context":["Need CI/CD, prompts, evals and model abstraction"]
  }' | jq
```

---

## 5. 环境变量

| 变量 | 说明 | 默认值 |
|---|---|---|
| `AINF_APP_NAME` | 服务名 | `AI Native Frame Demo` |
| `AINF_ENVIRONMENT` | 运行环境 | `dev` |
| `AINF_LOG_LEVEL` | 日志级别 | `INFO` |
| `AINF_LLM_PROVIDER` | 模型 provider（`mock/openai`） | `mock` |
| `AINF_LLM_MODEL` | 模型名 | `gpt-4.1-mini` |
| `AINF_OPENAI_API_KEY` | OpenAI Key（`openai` provider 时必填） | 空 |

---

## 6. CI/CD 概览

- **CI**（`ci.yml`）：ruff + mypy + pytest + eval smoke
- **CD**（`cd.yml`）：`main`/`v*` 自动构建并推送 GHCR 镜像
- **Dependabot**：每周更新 Python 依赖与 GitHub Actions

详见：`docs/CICD.md`

---

## 7. 下一步可扩展方向

- 接入向量检索与 RAG（compose 已预置 Qdrant）
- 增加多 Agent 协作与工具调用
- 引入在线观测（trace/token/cost）
- 扩展离线 benchmark 与回归评测矩阵