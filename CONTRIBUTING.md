# Contributing

## 1. 本地开发

```bash
./scripts/bootstrap.sh
source .venv/bin/activate
```

## 2. 提交前检查

```bash
make format
make ci
```

## 3. 目录约定

- `src/`：应用核心代码
- `prompts/`：提示词模板
- `evals/`：评测数据
- `configs/`：运行配置
- `docs/`：架构与流程文档

## 4. 提交规范

- 一个 commit 只做一类逻辑修改；
- 涉及行为变更必须补测试；
- 涉及 prompt 变更建议补 eval 样本。
