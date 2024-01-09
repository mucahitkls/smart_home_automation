from .base_command import Command
from receivers.light import Light
from receivers.exceptions import InvalidValueException, InvalidModeException, NoUndoFoundException
import numbers
from utils.logger import logger_setup

logger = logger_setup(__name__)


class TurnOnLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light
        self.previous_state = light.state

    def execute(self):
        self.previous_state = self.light.state
        self.light.turn_on()

    def undo(self):
        if self.previous_state == 'off':
            self.light.turn_off()


class TurnOffLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light
        self.previous_state = light.state

    def execute(self):
        self.previous_state = self.light.state
        self.light.turn_off()

    def undo(self):
        if self.previous_state == 'on':
            self.light.turn_on()


class ChangeBrightnessCommand(Command):
    def __init__(self, light: Light, value: int):
        self.light = light
        self.value = value
        self.previous_brightness = light.brightness

    def execute(self):
        if isinstance(self.value, numbers.Real):
            self.previous_brightness = self.light.brightness
            self.light.change_brightness(self.value)
        else:
            logger.error(f"Light: {self.light.name} -- invalid brightness value, operation failed...")
            raise InvalidValueException(value=self.value, max_value=self.light.max_brightness)

    def undo(self):
        if self.previous_brightness:
            self.light.change_brightness(self.previous_brightness)
        else:
            logger.error(f'Light: {self.light.name} -- there is nothing to undo...')
            raise NoUndoFoundException(self.light)


class ChangeLightModeCommand(Command):
    def __init__(self, light: Light, mode: str):
        self.light = light
        self.mode = mode
        self.previous_mode = self.light.mode

    def execute(self):
        if isinstance(self.mode, str) and self.mode in self.light.available_modes:
            self.light.change_mode(self.mode)
        else:
            logger.warning(f"Light: {self.light.name} -- invalid mode: {self.mode}, operation failed...")
            raise InvalidModeException(mode=self.mode, available_modes=self.light.available_modes)

    def undo(self):
        if self.previous_mode:
            self.light.change_mode(self.previous_mode)
        else:
            logger.warning(f"Light: {self.light.name} -- there is nothing to undo...")
            raise NoUndoFoundException(self.light)