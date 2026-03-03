# AI-native Frame 架构说明

## 1. 设计目标

这个示例仓库用于展示一个最小可运行、可持续演进的 AI-native 工程骨架。核心原则如下：

- **代码与 Prompt 并行管理**：prompt 文件被纳入版本控制并可在 CI 中验证。
- **模型可替换**：通过 provider 抽象，支持 `mock` 与真实模型切换。
- **评测前置**：在单测之外引入 eval smoke，避免“能跑但效果漂移”。
- **交付可自动化**：主干分支与 tag 自动构建镜像，减少手工发布。

## 2. 分层结构

### API 层（`src/ai_native_frame/api.py`）

- 提供 `health` 与 `research task` HTTP 接口；
- 负责请求校验与响应模型封装；
- 不直接耦合具体模型实现。

### Workflow 层（`src/ai_native_frame/workflows/`）

- 编排任务执行路径；
- 管理“输入 -> Agent -> 输出”的流程；
- 作为未来多 Agent / Tool Calling / RAG 的接入点。

### Agent 层（`src/ai_native_frame/agents/`）

- 负责构造上下文和提示词；
- 调用 LLM 抽象接口；
- 输出标准化结果对象。

### LLM Provider 层（`src/ai_native_frame/llm/`）

- `mock` provider：零密钥、可重复、适合 CI；
- `openai` provider：用于真实线上推理；
- `factory` 根据环境变量选择具体实现。

### Prompt 与配置层（`prompts/` + `configs/`）

- Prompt 文件化，支持版本比较与回滚；
- Agent / Workflow 运行配置可单独演进；
- 保持“代码逻辑”和“提示策略”解耦。

### Eval 层（`src/ai_native_frame/evals` + `evals/datasets`）

- 数据集使用 JSONL；
- 通过 `ainf-eval` 或模块命令触发；
- 在 CI 里执行 smoke 级门禁。

## 3. 未来可扩展点

- 挂载向量数据库与检索（当前 compose 内已预置 Qdrant）；
- 增加多 Agent 路由、反思链路与工具调用；
- 加入线上观测（trace/span/token/cost）与告警；
- 增加离线 benchmark 与回归评测矩阵。
