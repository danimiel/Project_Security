# Loguru

from loguru import logger

logger.add(
    "logs/firewall.log",
    format="{time} | {level} | {message}",
    level="INFO",
    rotation="1 MB"
)
