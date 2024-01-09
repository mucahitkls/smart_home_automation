from common_classes import CommonDevice, CommonChangeMode, CommonChangeIntegerValue
from typing import Optional, List


class Tv:
    def __init__(self, name: str, color: str, max_channel: int = 10000, max_volume: int = 100,
                 available_modes=Optional[List[str]]):
        def get_max_value(value, return_value):
            if isinstance(value, int) and value > 1:
                return value
            return return_value

        self.common_device = CommonDevice(name)
        self.common_channel = CommonChangeIntegerValue(name, 'channel', 0, get_max_value(max_channel))
        self.common_volume = CommonChangeIntegerValue(name, 'volume', 0, get_max_value(max_volume))
        self.common_mode = CommonChangeMode(name, available_modes)

    def turn_on(self):
        self.common_device.turn_on()

    def turn_off(self):
        self.common_device.turn_off()

    def change_channel(self, channel: int):
        self.common_channel.change_value(value=channel)

    def change_volume(self, volume: int):
        self.common_volume.change_value(value=volume)

    def change_mode(self, mode: str):
        self.common_mode.change_mode(mode=mode)

    @property
    def state(self):
        return self.common_device.state

    @property
    def channel(self):
        return self.common_channel.value

    @property
    def volume(self):
        return self.common_volume.value

    @property
    def mode(self):
        return self.common_mode.mode
