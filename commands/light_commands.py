from .base_command import Command
from receivers.light import Light
import numbers
from utils.logger import logger_setup

logger = logger_setup(__name__)


class TurnOnLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class TurnOffLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


class ChangeBrightnessCommand(Command):
    def __init__(self, light: Light, value: int):
        self.light = light
        self.value = value

    def execute(self):
        if isinstance(self.value, numbers.Real) and 0 <= self.value <= self.light.max_brightness:
            self.light.change_brightness(self.value)
        else:
            logger.error(f"{self.light}: Invalid brightness value, operation failed...")

    def undo(self):
        if self.light.history:
            last_value = self.light.history.pop()
            self.light.change_brightness(last_value)
        else:
            logger.warning(f"{self.light.name}: Light there is nothing to undo...")


