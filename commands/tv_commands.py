from base_command import Command
from receivers.tv import Tv
import numbers


class TurnOnTvCommand(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

    def undo(self):
        self.tv.turn_off()


class TurnOffTvCommand(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

    def undo(self):
        self.tv.turn_on()


class ChangeChannelCommand(Command):
    def __init__(self, tv: Tv, channel: int):
        self.tv = tv
        self.channel = channel

    def execute(self):
        if isinstance(self.channel, numbers.Real) and self.tv.min_channel <= self.channel <= self.tv.max_channel:
            self.tv.change_channel(self.channel)

        else:
            print(f"{self.tv.name}: Invalid channel value, operation failed...")

    def undo(self):
        if self.tv.channel_history:
            last_value = self.tv.channel_history.pop()
            self.tv.change_channel(last_value)
        else:
            print(f"{self.tv.name}: Tv channel there is nothing to undo...")


class ChangeVolumeCommand(Command):
    def __init__(self, tv: Tv, volume: int):
        self.tv = tv
        self.volume = volume

    def execute(self):
        if isinstance(self.volume, numbers.Real) and self.tv.min_volume <= self.volume <= self.tv.max_volume:
            self.tv.change_volume(self.volume)

        else:
            print(f"{self.tv.name}: Invalid volume value, operation failed...")

    def undo(self):
        if self.tv.volume_history:
            last_value = self.tv.volume_history.pop()
            self.tv.change_volume(last_value)
        else:
            print(f"{self.tv.name}: Tv volume there is nothing to undo...")


class ChangeTVModeCommand(Command):
    def __init__(self, tv: Tv, mode: str):
        self.tv = tv
        self.mode = mode

    def execute(self):

        if isinstance(self.mode, str) and self.mode in self.tv.available_modes:
            self.tv.change_mode(self.mode)
        else:
            print(f"{self.tv.name}: Invalid mode value, operation failed...")

    def undo(self):
        if self.tv.mode_history:
            last_value = self.tv.mode_history.pop()
            self.tv.change_mode(last_value)
        else:
            print(f"{self.tv.name}: Tv there is nothing to undo...")

