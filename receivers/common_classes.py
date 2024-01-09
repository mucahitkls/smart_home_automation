from utils.logger import logger_setup
from utils.utilities import is_valid_hex_color
from exceptions import InvalidColorException, InvalidModeException, InvalidValueException, NotDimmableDevice

logger = logger_setup(__name__)


class CommonDevice:

    def __init__(self, name: str, state: str = 'off'):
        self.name = name
        self.state = state

    def turn_on(self):
        self.state = 'on'
        logger.info(f'{self.name} -- turned on')

    def turn_off(self):
        self.state = 'off'
        logger.info(f'{self.name} -- turned off')


class CommonChangeColor:
    def __init__(self, name, color: str):
        self.name = name
        self.color = color if is_valid_hex_color(color) else '#FFFFFF'

    def change_color(self, color: str):
        if not is_valid_hex_color(color):
            logger.error(f'{self.name} -- color setting failed, not valid color code: {color}')
            raise InvalidColorException(color)

        if self.color != color:
            self.color = color
            logger.info(f'{self.name} -- color set to {color}')

        else:
            logger.warning(f'{self.name} -- color is already set to {color}')


class CommonChangeBrightness:
    def __init__(self, name: str, state: str, is_dimmable: bool = False):
        self.name = name
        self.state = state
        self.brightness = 0
        self.is_dimmable = is_dimmable
        self.max_brightness = 100

    def change_brightness(self, value: int):
        if not self.is_dimmable:
            logger.info(f'{self.name} -- light is not dimmable')
            raise NotDimmableDevice(self.name)

        new_value = max(0, min(value, self.max_brightness))
        if self.brightness != new_value:
            self.state = 'off' if new_value == 0 else 'on'
            self.brightness = new_value
            logger.info(f'{self.name} -- brightness changed to {self.brightness}')
        else:
            logger.warning(f'{self.name} -- brightness is already set to {new_value}')


class CommonChangeMode:
    def __init__(self, name: str, available_modes: list):
        self.name = name
        self.mode = 'Normal'
        self.available_modes = available_modes if available_modes is not None else ['Normal', 'Cinema', 'Sports',
                                                                                    'Game']

    def change_mode(self, mode: str):
        if mode not in self.available_modes:
            logger.error(f'{self.name} -- does not support mode: {mode}')
            raise InvalidModeException(mode=mode, available_modes=self.available_modes)

        if self.mode != mode:
            self.mode = mode
            logger.info(f'{self.name} -- mode set to {mode}')
        else:
            logger.warning(f'{self.name} -- mode is already set to {mode}')


class CommonChangeIntegerValue:
    def __init__(self, name: str, attribute_to_change: str, min_val: int, max_val: int):
        self.name = name
        self.attribute = attribute_to_change
        self.value = 0
        self.min_value = min_val
        self.max_value = max_val

    def change_value(self, value: int):
        new_value = max(self.min_value, min(value, self.max_value))
        if self.value != new_value:
            self.value = new_value
            logger.info(f'{self.name} -- {self.attribute} is set to {new_value}')
        else:
            logger.info(f'{self.name} -- {self.attribute} is already set to {new_value}')
