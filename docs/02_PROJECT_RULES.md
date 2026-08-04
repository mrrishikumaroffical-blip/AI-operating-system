# 02_PROJECT_RULES.md

# AI Operating System — Project Rules & Development Standards

**Version:** 1.0

**Status:** Active

**Last Updated:** August 2026

---

# Purpose

This document defines the mandatory rules, standards, and principles for developing the AI Operating System.

Every developer, AI agent, automation workflow, and future contributor must follow these rules.

These rules are designed to ensure that the system remains secure, scalable, maintainable, reliable, and easy to expand.

If a future feature conflicts with these rules, these rules take priority.

---

# Mission Statement

Build an intelligent AI Operating System that automates complex tasks while maintaining the highest standards of security, reliability, transparency, and modular software engineering.

The project should remain easy to maintain, inexpensive to operate, cloud-friendly, and capable of growing into a production-grade AI platform.

---

# Core Philosophy

The system follows these principles in order of priority:

1. Safety First
2. Security First
3. Data Integrity
4. Reliability
5. Simplicity
6. Automation
7. Scalability
8. Performance
9. Cost Efficiency
10. User Experience

No feature may violate a higher-priority principle to improve a lower-priority one.

---

# Rule 1 — Safety First (Highest Priority)

Safety is more important than speed, convenience, or automation.

The system must never intentionally perform actions that could cause irreversible damage.

Examples include:

* deleting important files
* deleting databases
* removing cloud resources
* exposing private information
* leaking API keys
* executing dangerous commands
* sending messages without permission
* making financial transactions
* changing critical settings automatically

Before performing any irreversible operation, explicit user approval must be required.

If the system is uncertain, it must stop and request confirmation instead of guessing.

---

# Rule 2 — Security First

Security is mandatory throughout the project.

The system must never expose:

* API Keys
* Passwords
* Tokens
* Private URLs
* OAuth credentials
* Environment variables
* Database credentials
* Personal user information

Security Rules:

* Never hardcode secrets.
* Always use environment variables.
* Use GitHub Secrets for deployment.
* Validate every external input.
* Escape dangerous characters.
* Prevent command injection.
* Never trust user input.
* Never log secrets.

---

# Rule 3 — Human Control

The AI assists humans.

It never replaces human judgment.

Critical operations require approval.

Examples:

* deleting data
* publishing content
* sending emails
* purchasing products
* financial decisions
* account deletion
* repository deletion

Automation should always be reversible whenever possible.

---

# Rule 4 — Reliability

The system should continue operating even if one component fails.

Every workflow should:

* detect errors
* retry temporary failures
* log failures
* continue when safe
* notify users when necessary

One failing module must not crash the entire system.

---

# Rule 5 — Accuracy

The AI should never invent facts.

If information is uncertain:

* clearly state uncertainty
* provide available evidence
* avoid guessing
* request clarification when needed

Correctness is more important than appearing confident.

---

# Rule 6 — Transparency

Every important action should be understandable.

The system should explain:

* what happened
* why it happened
* what data was used
* what output was produced

Users should never wonder why the AI performed an action.

---

# Rule 7 — Privacy

User data belongs to the user.

The project must:

* minimize stored information
* avoid collecting unnecessary data
* protect personal information
* never share user data without permission

Personal information should only be stored when absolutely necessary.

---

# Rule 8 — Modular Development

Every module should have one clear responsibility.

Examples:

One file:

* one purpose
* one responsibility
* one logical component

Avoid giant files containing unrelated functionality.

Modules should communicate through clearly defined interfaces.

---

# Rule 9 — Clean Code

Code should be readable before being clever.

Rules:

* meaningful variable names
* descriptive function names
* consistent formatting
* avoid duplicated logic
* keep functions short
* remove dead code
* avoid unnecessary complexity

Future developers should understand code without extensive explanation.

---

# Rule 10 — Documentation First

Every significant feature requires documentation before implementation.

Documentation should include:

* purpose
* inputs
* outputs
* dependencies
* workflow
* limitations
* examples

If a feature cannot be explained clearly, redesign it before implementation.

---

# Rule 11 — Logging

Every important action must generate logs.

Logs should contain:

* timestamp
* module
* workflow
* task
* execution status
* duration
* warning messages
* errors

Logs should never contain passwords, tokens, or confidential information.

---

# Rule 12 — Error Handling

Errors should never be ignored.

Every exception should:

* be caught
* logged
* explained
* handled safely

The system should fail gracefully whenever possible.

---

# Rule 13 — Cloud Friendly

The project is designed to operate primarily on free cloud services.

Development decisions should prioritize:

* low cost
* low resource usage
* portability
* minimal infrastructure

Avoid unnecessary dependencies that increase operating costs.

---

# Rule 14 — AI Behavior Standards

The AI must:

* explain important decisions
* ask questions when uncertain
* avoid hallucinations
* avoid hidden assumptions
* follow project rules
* respect user intent
* remain honest about limitations

The AI must never fabricate outputs to appear intelligent.

---

# Rule 15 — Data Management

Data should always be:

* validated
* versioned when appropriate
* backed up if critical
* organized
* recoverable

Never overwrite important information without confirmation.

---

# Rule 16 — Folder Organization

Every folder has one responsibility.

Example structure:

docs/
agents/
memory/
config/
logs/
workflows/
database/
scripts/
tests/
assets/

Do not place unrelated files together.

---

# Rule 17 — Git Standards

Every commit should:

* represent one logical change
* have a meaningful commit message
* avoid temporary files
* exclude secrets
* keep history clean

Never commit:

* .env files
* API keys
* passwords
* cache files
* large generated files unless required

---

# Rule 18 — Performance

Optimization comes after correctness.

Before optimizing:

* verify correctness
* measure performance
* identify bottlenecks

Avoid premature optimization.

---

# Rule 19 — Scalability

Every new component should support future expansion.

The architecture should allow:

* additional AI models
* new agents
* extra databases
* multiple APIs
* additional workflows

without requiring major rewrites.

---

# Rule 20 — Testing

Every important feature should be tested before release.

Testing includes:

* expected behavior
* edge cases
* failure conditions
* recovery
* integration

Untested code should never be considered production-ready.

---

# Rule 21 — Continuous Improvement

The project should continuously improve.

Regular activities include:

* refactoring
* removing technical debt
* improving documentation
* increasing automation
* simplifying workflows

Improvements must not reduce security or reliability.

---

# Rule 22 — Project Vision Protection

Every future feature must support the long-term vision of building a professional AI Operating System.

Avoid adding features that:

* increase unnecessary complexity
* reduce maintainability
* duplicate existing functionality
* violate project principles

Every addition should strengthen the architecture rather than weaken it.

---

# Non-Negotiable Rules

The following rules are absolute:

* Safety before automation.
* Security before convenience.
* Reliability before speed.
* Accuracy before confidence.
* Documentation before implementation.
* Human approval before destructive actions.
* Never expose secrets.
* Never silently delete data.
* Never fabricate information.
* Keep the architecture modular.
* Keep the system maintainable.
* Keep the code readable.
* Protect user privacy at all times.

Violation of these rules should be treated as a design failure and corrected before deployment.

---

# Final Principle

> Build software that you can confidently maintain, safely expand, and trust to operate for years—not just software that works today.

End of Document.
