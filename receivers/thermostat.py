from common_classes import CommonElectricalDevice, CommonChangeMode, CommonChangeIntegerValue
from receivers_schemas.thermostat_schema import ThermostatDetails


class Thermostat:

    def __init__(self, name: str, available_modes: list, min_temp: int = -10, max_temp: int = 120):
        self.common_device = CommonElectricalDevice(device_type='Thermostat', name=name)
        self.common_mode = CommonChangeMode(name, available_modes)
        self.common_temperature_change = CommonChangeIntegerValue(name, 'temperature', min_temp, max_temp)

    def turn_on(self):
        self.common_device.turn_on()

    def turn_off(self):
        self.common_device.turn_off()

    def change_temperature(self, new_temp):
        self.common_temperature_change.change_value(value=new_temp)

    def change_mode(self, mode):
        self.common_mode.change_mode(mode=mode)

    @property
    def device_type(self):
        return self.common_device.device_type

    @property
    def name(self):
        return self.common_device.name

    @property
    def state(self):
        return self.common_device.state

    @property
    def temperature(self):
        return self.common_temperature_change.value

    @property
    def min_temperature(self):
        return self.common_temperature_change.min_value

    def max_temperature(self):
        return self.common_temperature_change.max_value

    @property
    def mode(self):
        return self.common_mode.mode

    @property
    def available_modes(self):
        return self.common_mode.available_modes

    def get_info(self):
        return ThermostatDetails(
            device_type=self.device_type,
            name=self.name,
            state=self.state,
            temperature=self.temperature,
            min_temperature=self.min_temperature,
            max_temperature=self.max_temperature,
            mode=self.mode,
            available_modes=self.available_modes
        )
