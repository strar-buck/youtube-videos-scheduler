import logging

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)s %(pathname)s:%(lineno)s %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
