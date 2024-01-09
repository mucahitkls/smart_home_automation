from common_classes import CommonElectricalDevice, CommonChangeMode, CommonChangeIntegerValue


class Thermostat:

    def __init__(self, name: str, available_modes: list, min_temp: int = -10, max_temp: int = 120):
        self.common_device = CommonElectricalDevice(name)
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
    def name(self):
        return self.common_device.name

    @property
    def state(self):
        return self.common_device.state

    @property
    def temperature(self):
        return self.common_temperature_change.value

    @property
    def mode(self):
        return self.common_mode.mode
