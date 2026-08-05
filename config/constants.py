"""
Global constants for the AI Operating System.
"""

from pathlib import Path

# =========================
# Project Paths
# =========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOCS_DIR = PROJECT_ROOT / "docs"
DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CACHE_DIR = DATA_DIR / "cache"
OUTPUT_DIR = DATA_DIR / "output"

PROMPTS_DIR = PROJECT_ROOT / "prompts"

# =========================
# Agent Names
# =========================

LINKEDIN_AGENT = "linkedin_agent"
YOUTUBE_AGENT = "youtube_agent"

# =========================
# Project Information
# =========================

PROJECT_NAME = "AI Operating System"
PROJECT_VERSION = "0.1.0"

# =========================
# Logging
# =========================

LOG_LEVEL = "INFO"

# =========================
# Default AI Models
# =========================

DEFAULT_LLM = "gemini-2.5-flash"
DEFAULT_EMBEDDING_MODEL = "text-embedding-004"
