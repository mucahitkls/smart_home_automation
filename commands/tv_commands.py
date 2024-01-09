from .base_command import Command
from receivers.tv import Tv
from receivers.exceptions import InvalidModeException
import numbers


class TurnOnTvCommand(Command):
    def __init__(self, tv: Tv):
        self.tv = tv
        self.previous_state = self.tv.state

    def execute(self):
        self.tv.turn_on()

    def undo(self):
        if self.previous_state == 'off':
            self.tv.turn_off()


class TurnOffTvCommand(Command):
    def __init__(self, tv: Tv):
        self.tv = tv
        self.previous_state = self.tv.state

    def execute(self):
        self.tv.turn_off()

    def undo(self):
        if self.previous_state == 'on':
            self.tv.turn_on()


class ChangeChannelCommand(Command):
    def __init__(self, tv: Tv, channel: int):
        self.tv = tv
        self.channel = channel
        self.previous_channel = self.tv.channel

    def execute(self):
        if isinstance(self.channel, numbers.Real) and 1 <= self.channel <= self.tv.max_channel:
            self.tv.change_channel(self.channel)

        else:
            print(f"{self.tv.name}: Invalid channel value, operation failed...")

    def undo(self):
        if self.previous_channel:
            self.tv.change_channel(self.previous_channel)
        else:
            print(f"{self.tv.name}: Tv channel there is nothing to undo...")


class ChangeVolumeCommand(Command):
    def __init__(self, tv: Tv, volume: int):
        self.tv = tv
        self.volume = volume
        self.previous_volume = self.tv.volume

    def execute(self):
        if isinstance(self.volume, numbers.Real) and 0 <= self.volume <= self.tv.max_volume:
            self.tv.change_volume(self.volume)

        else:
            print(f"{self.tv.name}: Invalid volume value, operation failed...")

    def undo(self):
        if self.previous_volume:
            self.tv.change_volume(self.previous_volume)
        else:
            print(f"{self.tv.name}: Tv volume there is nothing to undo...")


class ChangeTVModeCommand(Command):
    def __init__(self, tv: Tv, mode: str):
        self.tv = tv
        self.mode = mode
        self.previous_mode = self.tv.mode

    def execute(self):

        if isinstance(self.mode, str) and self.mode in self.tv.available_modes:
            self.tv.change_mode(self.mode)
        else:
            print(f"{self.tv.name}: Invalid mode value, operation failed...")
            raise InvalidModeException(self.mode, self.tv.available_modes)

    def undo(self):
        if self.previous_mode:
            self.tv.change_mode(self.previous_mode)
        else:
            print(f"{self.tv.name}: Tv there is nothing to undo...")
