import logging

# Configura logger
LOGGER = logging.getLogger("default_logger")
CH = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s", "%H:%M:%S")
CH.setFormatter(formatter)
LOGGER.addHandler(CH)
