# 贡献指南
首先，感谢大家为 Ascension 贡献代码
本张旨在引导你更规范地向 Ascension 提交贡献，请务必认真阅读。

**我们欢迎一切贡献！并对每个愿意贡献的人表示衷心的感谢！** 💖

> 如果你喜欢这个项目，可以为本项目点亮 ⭐️，这是对我们最大的鼓励。

## 提交 Issue

在提交 Issue 前，我们建议你先查看 [已有的 Issues](https://github.com/MyXiaoNan/nonebot-plugin-ascension/issues)，以防重复提交。

### 报告问题

该插件仍然是一个不够稳定的开发中项目，如果你在使用过程中发现问题并确信是由 本插件 引起的，欢迎提交 Issue。

### 建议功能

本插件 目前只是测试版，欢迎在 Issue 中提议要加入哪些新功能。

为了让开发者更好地理解你的意图，请认真描述你所需要的特性，可能的话可以提出你认为可行的解决方案。

## Pull Request

本插件 使用 PDM 管理项目依赖，由于 pre-commit 也经其管理，所以在此一并说明。

下面的命令能在已安装 PDM 的情况下帮你快速配置开发环境。

```bash
# 安装 python 依赖
pdm install
# 安装 pre-commit git hook
pre-commit install
```

### 使用 GitHub Codespaces（Dev Container）

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/MyXiaoNan/nonebot-plugin-ascension)

### 使用 GitPod

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#/https://github.com/MyXiaoNan/nonebot-plugin-ascension)

### Commit 规范

请确保你的每一个 commit 都能清晰地描述其意图，一个 commit 尽量只有一个意图。

本插件 的 commit message 格式遵循 [gitmoji](https://gitmoji.dev/) 规范，在创建 commit 时请牢记这一点。


### 工作流概述

`master` 分支为 本插件 的开发分支，在任何情况下都请不要直接修改 `master` 分支，而是创建一个目标分支为 `nonebot-plugin-ascension:master` 的 Pull Request 来提交修改。Pull Request 标题请尽量更改成中文，以便阅读。

如果你不是 本团队 的成员，可在 fork 本仓库后，向本仓库的 master 分支发起 Pull Request，注意遵循先前提到的 commit message 规范创建 commit。我们将在 code review 通过后通过 squash merge 方式将您的贡献合并到主分支。

### 参与开发

本插件 的代码风格遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 与 [PEP 484](https://www.python.org/dev/peps/pep-0484/) 规范，请确保你的代码风格和项目已有的代码保持一致，变量命名清晰，有适当的注释与测试代码。
