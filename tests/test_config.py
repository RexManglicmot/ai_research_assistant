# test_config.py
from app.config import settings

print("✅ Config loaded successfully!")
print("HF_TOKEN:", settings.HF_TOKEN[:10] + "..." if settings.HF_TOKEN else "❌ Missing")
print("MODEL_ID:", settings.MODEL_ID)
print("EMBEDDING_MODEL:", settings.EMBEDDING_MODEL)
print("TOP_K:", settings.TOP_K)
print("ENABLE_OCR:", settings.ENABLE_OCR)
