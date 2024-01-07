from utils.logger import logger_setup

logger = logger_setup(__name__)


class Light:
    def __init__(self, name: str, dimmable: bool = False, max_brightness: int = 100):
        self.name = name
        self.state = "off"
        self.history = []

        self.is_dimmable = dimmable
        self.brightness = 0
        self.max_brightness = max_brightness

    def turn_on(self):
        self.state = "on"
        logger.info(f"{self.name}: Light turned on")

    def turn_off(self):
        self.state = "off"
        logger.info(f"{self.name}: Light turned off")

    def change_brightness(self, value: int = 0):
        if not self.is_dimmable:
            logger.error(f"{self.name}: This light is not dimmable.")
            return

        new_value = max(0, min(value, self.max_brightness))
        if self.history and self.history[-1] == new_value:
            logger.warning(f"{self.name}: Brightness is already set to {new_value}")
        else:
            self.brightness = new_value
            self.history.append(self.brightness)
            logger.info(f"{self.name}: Brightness changed to {self.brightness}")
