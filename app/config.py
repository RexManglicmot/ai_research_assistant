# app/config.py
"""
Centralized configuration for AI Research Assistant.
- Loads environment variables from .env
- Parses values into correct types
- Validates required settings (like Hugging Face token)
- Provides a single settings object for the whole app
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

# --------------------------
# Load .env into environment
# --------------------------
# This reads your `.env` file and makes its variables available via os.getenv().
# If running in a cloud environment (Heroku, AWS, etc.), .env may not exist —
# in that case, variables must be set directly in the environment.
load_dotenv()


# --------------------------
# Helper parsing functions
# --------------------------
def _to_bool(val: str | None, default: bool = False) -> bool:
    """Convert string env var to boolean, with a default fallback."""
    if val is None:
        return default
    return val.strip().lower() in {"1", "true", "yes", "y", "on"}


def _to_int(val: str | None, default: int) -> int:
    """Convert string env var to integer, with a default fallback."""
    try:
        return int(val) if val is not None else default
    except ValueError:
        return default


def _to_float(val: str | None, default: float) -> float:
    """Convert string env var to float, with a default fallback."""
    try:
        return float(val) if val is not None else default
    except ValueError:
        return default


# --------------------------
# Settings Data Class
# --------------------------
@dataclass(frozen=True)
class Settings:
    """
    Stores all configurable settings for the application.
    Frozen=True makes it immutable after creation (good for safety).
    """

    # --- Auth / Providers ---
    HF_TOKEN: str                          # Hugging Face API token

    # --- Models ---
    MODEL_ID: str                          # Generator LLM
    EMBEDDING_MODEL: str                   # Embedding model for vector search

    # --- Retrieval / RAG ---
    TOP_K: int = 5                         # How many chunks to retrieve per query
    CHUNK_SIZE: int = 1000                 # Characters per chunk when splitting docs
    CHUNK_OVERLAP: int = 200               # Overlap between chunks (prevents missing context)

    # --- Generation ---
    MAX_TOKENS: int = 512                  # Max tokens in LLM response
    TEMPERATURE: float = 0.1               # Creativity level (0=deterministic)

    # --- Paths / Persistence ---
    DATA_DIR: str = "data"                 # Directory for raw PDF/doc files
    VECTOR_DIR: str = "vectorstore"        # Directory for FAISS index storage
    LOG_FILE: str = "logs/app.log"         # Log file location

    # --- Optional features ---
    ENABLE_OCR: bool = False               # Toggle OCR for scanned PDFs/images


# --------------------------
# Settings Loader
# --------------------------
def load_settings() -> Settings:
    """
    Create a Settings object from environment variables.
    - Applies defaults if not provided
    - Validates required variables (HF token)
    """
    # Validate required Hugging Face token
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN", "").strip()
    if not hf_token:
        raise ValueError(
            "HUGGINGFACEHUB_API_TOKEN is missing. Add it to your .env file."
        )

    # Model configuration (with defaults)
    model_id = os.getenv("MODEL_ID", "mistralai/Mistral-7B-Instruct-v0.2").strip()
    embed_model = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    ).strip()

    return Settings(
        HF_TOKEN=hf_token,
        MODEL_ID=model_id,
        EMBEDDING_MODEL=embed_model,
        TOP_K=_to_int(os.getenv("TOP_K"), 5),
        CHUNK_SIZE=_to_int(os.getenv("CHUNK_SIZE"), 1000),
        CHUNK_OVERLAP=_to_int(os.getenv("CHUNK_OVERLAP"), 200),
        MAX_TOKENS=_to_int(os.getenv("MAX_TOKENS"), 512),
        TEMPERATURE=_to_float(os.getenv("TEMPERATURE"), 0.1),
        DATA_DIR=os.getenv("DATA_DIR", "data"),
        VECTOR_DIR=os.getenv("VECTOR_DIR", "vectorstore"),
        LOG_FILE=os.getenv("LOG_FILE", "logs/app.log"),
        ENABLE_OCR=_to_bool(os.getenv("ENABLE_OCR"), False),
    )


# --------------------------
# Global Settings Instance
# --------------------------
# Load settings once at import, so other modules can just do:
# from app.config import settings
settings = load_settings()
