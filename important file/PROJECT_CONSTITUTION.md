# PROJECT_CONSTITUTION.md

# AI Operating System - Project Constitution

Version: 1.0

---

# Purpose

This document defines the permanent principles, vision, architecture, and rules of the AI Operating System.

Unless there is a strong technical reason, this document should not change frequently.

Whenever development begins, read this document first.

---

# Vision

Build a production-quality AI Operating System that allows multiple AI agents to work together using one shared core.

The project should be scalable, modular, maintainable, secure, and suitable for open-source development.

The goal is not to build one automation script.

The goal is to build a reusable operating system for AI agents.

---

# Mission

Create one platform capable of running many AI agents.

Every future AI agent should be able to plug into the system without changing the core architecture.

---

# Long-Term Goals

Build an operating system capable of supporting:

* LinkedIn AI Agent
* YouTube Automation Agent
* Research Agent
* Study Assistant
* Coding Assistant
* Email Assistant
* Business Automation Agents
* Future AI Agents

The system should continue growing while the core remains stable.

---

# Core Philosophy

The core controls the agents.

Agents never control the core.

Everything should be reusable.

Everything should be modular.

Everything should be replaceable.

---

# Non-Negotiable Rules

## Architecture

Always keep code modular.

Avoid tightly coupled modules.

One responsibility per module.

Never create duplicate functionality.

---

## Development

Build one module completely before starting another.

Test before moving forward.

Keep commits small and meaningful.

Never skip documentation for important architectural decisions.

---

## Code Quality

Readable code is better than clever code.

Prefer simple solutions over complex ones.

Write maintainable code.

Avoid unnecessary dependencies.

---

## Security

Never hardcode secrets.

Use environment variables.

Protect API keys.

Keep sensitive files out of Git.

---

## Scalability

Design for future growth.

Assume more agents will be added later.

Avoid designs that only work for today's requirements.

---

# Repository Architecture

AI-operating-system/

* docs/
* src/

  * core/
  * shared/
  * linkedin_agent/
  * youtube_agent/
  * dashboard/
* config/
* prompts/
* data/
* tests/
* scripts/
* .github/
* README.md
* requirements.txt
* .gitignore
* .env.example

Python application code belongs inside the src/ directory.

Configuration files belong inside config/.

Documentation belongs inside docs/.

---

# Core Modules

The Core is responsible for:

* Configuration
* Logging
* Memory
* Planning
* Task Management
* Agent Management

The Core must remain independent of any specific AI agent.

---

# Shared Modules

Reusable code only.

No business logic.

---

# AI Agents

Every AI agent must use the shared core.

Agents should never duplicate existing functionality.

---

# Development Philosophy

Think before coding.

Design before implementing.

Test before expanding.

Refactor only when necessary.

---

# Success Criteria

The project is successful when:

* New AI agents can be added easily.
* Existing modules require minimal changes.
* The architecture remains clean.
* Documentation stays synchronized with the code.
* Another developer can understand the project quickly.

---

# Final Rule

If a future decision conflicts with this constitution, stop and discuss the decision before implementing it.
