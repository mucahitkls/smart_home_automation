from typing import List, Optional
from utils.logger import logger_setup

logger = logger_setup(__name__)


class Tv:
    def __init__(self, name: str = 'TV-1', max_channels: int = 10000, max_volume: int = 100,
                 available_modes=Optional[List[str]]):

        def get_max_channels(value):
            if isinstance(value, int) and value > 1:
                return value
            return 10000

        def get_max_volume(value):
            if isinstance(value, int) and value > 1:
                return value
            return 100

        self.name = name
        self.state = "off"

        self.channel_history = []
        self.volume_history = []
        self.mode_history = []

        self.min_channel = 1
        self.max_channel = get_max_channels(max_channels)

        self.min_volume = 0
        self.max_volume = get_max_volume(max_volume)
        self.available_modes = self.available_modes = available_modes if available_modes is not None else ['Normal',
                                                                                                           'Cinema',
                                                                                                           'Sports']

        self.channel = 1
        self.volume = 10
        self.mode = 'Normal'

    def turn_on(self):
        self.state = "on"
        logger.info(f"{self.name}: Tv is turned on")

    def turn_off(self):
        self.state = "off"
        logger.info(f"{self.name}: Tv is turned off")

    def change_channel(self, channel: int):
        new_value = max(self.min_channel, min(channel, self.max_channel))
        if self.channel_history and self.channel_history[-1] == new_value:
            logger.warning(f"{self.name}: Tv channel is already {new_value}")
        else:
            self.channel = new_value
            self.channel_history.append(new_value)
            logger.info(f"{self.name}: Tv channel is set to {new_value}")

    def change_volume(self, volume: int):
        new_value = max(self.min_volume, min(volume, self.max_volume))
        if self.volume_history and self.volume_history[-1] == new_value:
            logger.warning(f"{self.name}: Tv volume is already {new_value}")
        else:
            self.volume = new_value
            self.volume_history.append(new_value)
            logger.info(f"{self.name}: Tv volume is set to {new_value}")

    def change_mode(self, mode: str = "Normal"):

        if mode not in self.available_modes:
            logger.error(f"{self.name}: Tv doesn't support mode: {mode}")
            return

        if self.mode != mode:
            self.mode = mode
            self.mode_history.append(mode)
            logger.info(f"{self.name}: Tv mode set to {mode}")
        else:
            logger.info(f"{self.name}: Tv mode is already {mode}")
