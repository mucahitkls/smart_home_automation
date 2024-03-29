from .common_classes import CommonElectricalDevice, CommonChangeMode, CommonChangeIntegerValue
from typing import Optional, List
from receivers_schemas.tv_schema import TvDetails


class Tv:
    def __init__(self, name: str, max_channel: int = 10000, max_volume: int = 100,
                 available_modes=Optional[List[str]]):
        def get_max_value(value, return_value):
            if isinstance(value, int) and value > 1:
                return value
            return return_value

        self.common_device = CommonElectricalDevice(device_type='TV', name=name)
        self.common_channel = CommonChangeIntegerValue(name, 'channel', 1, get_max_value(max_channel, 10000))
        self.common_volume = CommonChangeIntegerValue(name, 'volume', 0, get_max_value(max_volume, 100))
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
    def device_type(self):
        return self.common_device.device_type

    @property
    def name(self):
        return self.common_device.name

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

    @property
    def available_modes(self):
        return self.common_mode.available_modes

    @property
    def max_channel(self):
        return self.common_channel.max_value

    @property
    def max_volume(self):
        return self.common_volume.max_value

    def get_details(self):

        return TvDetails(
            device_type=self.device_type,
            name=self.name,
            state=self.state,
            current_channel=self.channel,
            current_volume=self.volume,
            current_mode=self.mode,
            max_channel=self.max_channel,
            max_volume=self.max_volume,
            available_modes=self.available_modes
        )
