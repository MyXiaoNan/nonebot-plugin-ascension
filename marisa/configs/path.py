from pathlib import Path

BOT_DIR = Path.cwd()
"""机器人根目录"""

DATA_DIR = BOT_DIR / "data" / "marisa"
"""数据保存目录"""
LOG_DIR = DATA_DIR / "logs"
"""日志保存目录"""
TEMPLATE_DIR = DATA_DIR / "templates"
"""模板保存目录"""
