from base_command import Command
from receivers.thermostat import Thermostat
import numbers
from utils.logger import logger_setup
from receivers.exceptions import NoUndoFoundException


logger = logger_setup(__name__)


class TurnOnThermostatCommand(Command):
    def __init__(self, thermostat: Thermostat):
        self.thermostat = thermostat
        self.previous_state = self.thermostat.state

    def execute(self):
        self.thermostat.turn_on()

    def undo(self):
        if self.previous_state == 'off':
            self.thermostat.turn_off()


class TurnOffThermostatCommand(Command):
    def __init__(self, thermostat: Thermostat):
        self.thermostat = thermostat
        self.previous_state = self.thermostat.state

    def execute(self):
        self.thermostat.turn_off()

    def undo(self):
        if self.previous_state == 'on':
            self.thermostat.turn_on()


class ChangeTemperatureCommand(Command):
    def __init__(self, thermostat: Thermostat, value: int):
        self.thermostat = thermostat
        self.value = value
        self.previous_temp = self.thermostat.temperature

    def execute(self):
        if isinstance(self.value, numbers.Real) and self.thermostat.min_temperature <= self.value <= self.thermostat.max_temperature:
            self.thermostat.change_temperature(self.value)
        else:
            logger.error(f"{self.thermostat.name}: Invalid temperature value, operation failed...")

    def undo(self):
        if self.previous_temp:
            self.thermostat.change_temperature(self.previous_temp)
        else:
            logger.warning(f"{self.thermostat.name}: Thermostat there is nothing to undo...")
            raise NoUndoFoundException(self.thermostat)
        
        
class ChangeThermostatModeCommand(Command):
    def __init__(self, thermostat: Thermostat, mode: str):
        self.thermostat = thermostat
        self.mode = mode
        self.previous_mode = self.thermostat.mode

    def execute(self):

        if isinstance(self.mode, str) and self.mode in self.thermostat.available_modes:
            self.thermostat.change_mode(self.mode)
        else:
            print(f"{self.thermostat.name}: Invalid mode value, operation failed...")

    def undo(self):
        if self.previous_mode:
            self.thermostat.change_mode(self.previous_mode)
        else:
            print(f"{self.thermostat.name}: thermostat there is nothing to undo...")
            raise NoUndoFoundException(self.thermostat)