from common_classes import CommonElectricalDevice, CommonChangeColor, CommonChangeBrightness, CommonChangeMode


class Light:
    def __init__(self, name: str, color: str, available_modes: list, is_dimmable: bool = False):
        self.common_device = CommonElectricalDevice(name)
        self.common_color = CommonChangeColor(name, color)
        self.common_brightness = CommonChangeBrightness(name, self.common_device.state, is_dimmable)
        self.common_mode = CommonChangeMode(name, available_modes)

    def turn_on(self):
        self.common_device.turn_on()

    def turn_off(self):
        self.common_device.turn_off()

    def change_color(self, color: str):
        self.common_color.change_color(color)

    def change_brightness(self, value: int):
        self.common_brightness.change_brightness(value)

    def change_mode(self, mode: str):
        self.common_mode.change_mode(mode)

    # If needed, you can add methods to get the current state, color, brightness, and mode
    @property
    def state(self):
        return self.common_device.state

    @property
    def color(self):
        return self.common_color.color

    @property
    def brightness(self):
        return self.common_brightness.brightness

    @property
    def mode(self):
        return self.common_mode.mode


