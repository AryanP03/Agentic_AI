# 🦜🔗 LangChain v1 Complete Masterclass & Cheat Sheet

Welcome to the comprehensive documentation and project guide for the updated **LangChain v1 Crash Course**. This repository tracks core concepts, updated syntaxes, state management, tool integration, and agentic workflows introduced in the latest version of LangChain.

---

## 📋 Table of Contents

- [Environment Setup (`uv`)](#1-environment-setup-uv)
- [Module 1: LangChain Agents (The Basics)](#module-1-langchain-agents-the-basics)
- [Module 2: Multi-Model Integration](#module-2-multi-model-integration)
- [Module 3: Streaming & Batch Processing](#module-3-streaming--batch-processing)
- [Module 4: Custom Tools Creation & Execution Loop](#module-4-custom-tools-creation--execution-loop)
- [Module 5: Message Structures & Metadata](#module-5-message-structures--metadata)
- [Module 6: Structured Outputs](#module-6-structured-outputs)
- [Module 7: Middlewares & Human-In-The-Loop (HITL)](#module-7-middlewares--human-in-the-loop-hitl)

---

## 1. Environment Setup (`uv`)

We use **`uv`**, an extremely fast Python package and project manager written in Rust, to initialize project environments and manage dependencies.

### Commands

```bash
# Initialize a new working repository
uv init

# Create a virtual environment with the latest Python version
uv venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies from requirements.txt
uv add -r requirements.txt