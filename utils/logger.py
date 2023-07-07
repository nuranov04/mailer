import logging

logging.basicConfig(
    filename="logs/logs.log",
    filemode="w",
    format='%(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("app")

