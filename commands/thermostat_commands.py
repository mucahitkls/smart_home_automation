from base_command import Command
from receivers.thermostat import Thermostat
import numbers

class TurnOnThermostatCommand(Command):
    def __init__(self, thermostat: Thermostat):
        self.thermostat = thermostat

    def execute(self):
        self.thermostat.turn_on()

    def undo(self):
        self.thermostat.turn_off()


class TurnOffThermostatCommand(Command):
    def __init__(self, thermostat: Thermostat):
        self.thermostat = thermostat

    def execute(self):
        self.thermostat.turn_off()

    def undo(self):
        self.thermostat.turn_on()


class ChangeTemperatureCommand(Command):
    def __init__(self, thermostat: Thermostat, value: int):
        self.thermostat = thermostat
        self.value = value

    def execute(self):
        if isinstance(self.value, numbers.Real) and self.thermostat.min_temp <= self.value <= self.thermostat.max_temp:
            self.thermostat.change_temperature(self.value)
        else:
            print(f"{self.thermostat}: Invalid temperature value, operation failed...")

    def undo(self):
        if self.thermostat.history:
            last_value = self.thermostat.history.pop()
            self.thermostat.change_temperature(last_value)
        else:
            print(f"{self.thermostat.name}: Thermostat there is nothing to undo...")

