ai_research_assistant/
│
├── app/                                # Core logic (modular, testable)
│   ├── __init__.py
│   ├── config.py                       # Loads .env (HF token, settings)
│   ├── ingestion.py                    # Read 1..N PDFs (optional OCR hooks)
│   ├── utils.py                        # Text chunking, helpers
│   ├── embeddings.py                   # FAISS build/load (persistence)
│   ├── agent.py                        # RAG chain w/ Hugging Face LLM
│   └── logger_config.py                # File + console logging
│
├── data/                               # Put your PDFs here
│
├── logs/                               # app.log (auto-created)
│
├── vectorstore/                        # Saved FAISS index (auto-created)
│
├── tests/                              # Unit tests
│   ├── test_ingestion.py               # PDF extraction tests
│   ├── test_utils.py                   # Chunking tests
│   └── resources/                      # Tiny sample PDFs for tests
│
├── .github/
│   └── workflows/
│       └── test.yml                    # CI: install + pytest on push/PR
│
├── run.py                              # CLI entrypoint (ask questions)
├── requirements.txt                    # Runtime deps (HF, langchain, faiss, pymupdf, dotenv)
├── requirements-dev.txt                # Dev-only tools (pytest, black, isort, mypy, coverage, flake8)
├── Dockerfile                          # Container build (optional)
├── .env                                # HUGGINGFACEHUB_API_TOKEN=...
├── .gitignore                          # venv/, logs/, .env, __pycache__/, PDFs, vectorstore/
└── README.md                           # Description, setup, usage, status
