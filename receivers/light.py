from utils.logger import logger_setup
from utils.utilities import is_valid_hex_color
from exceptions import InvalidColorException, InvalidModeException

logger = logger_setup(__name__)


class Light:
    def __init__(self, name: str, available_modes: list, color: str, dimmable: bool = False):
        self.name = name
        self.state = 'off'
        self.mode = 'normal'
        self.color = color if is_valid_hex_color(color) else '#FFFFFF'

        self.is_dimmable = dimmable
        self.brightness = 0
        self.max_brightness = 100
        self.available_modes = available_modes if available_modes is not None else ['Normal', 'Cinema', 'Sports',
                                                                                    'Game']

    def turn_on(self):
        self.state = "on"
        logger.info(f"Light: {self.name} -- turned on")

    def turn_off(self):
        self.state = "off"
        logger.info(f"Light: {self.name} -- turned off")

    def change_brightness(self, value: int):

        if not self.is_dimmable:
            logger.error(f"Light: {self.name} -- light is not dimmable.")
            return

        new_value = max(0, min(value, self.max_brightness))
        if self.brightness != new_value:
            self.state = 'off' if new_value == 0 else 'on'
            self.brightness = new_value
            logger.info(f'Light: {self.name} -- brightness changed to {self.brightness}')
        else:
            logger.warning(f'Light: {self.name} -- brightness is already set to {new_value}')

    def change_mode(self, mode: str = "Normal"):

        if mode not in self.available_modes:
            logger.error(f'Light: {self.name} -- does not support mode: {mode}')
            raise InvalidModeException(mode=mode, available_modes=self.available_modes)

        if self.mode != mode:
            self.mode = mode
            logger.info(f'Light: {self.name} -- mode set to {mode}')
        else:
            logger.warning(f'Light: {self.name} -- mode is already {mode}')

    def change_color(self, color: str):
        if not is_valid_hex_color(color):
            logger.error(f'Light: {self.name} -- color setting failed, not valid color code: {color}')
            raise InvalidColorException(color)

        if self.color != color:
            self.color = color
            logger.info(f'Light: {self.name} -- color set to {color}')
        else:
            logger.warning(f'Light: {self.name} -- color is already {color}')
