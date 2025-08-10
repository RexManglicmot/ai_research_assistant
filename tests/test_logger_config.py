from app.logger_config import get_logger
import os

log = get_logger(__name__)
log.info("Test log entry.")

assert os.path.exists("logs/app.log"), "❌ Log file was not created."
print("✅ Logger works!")
