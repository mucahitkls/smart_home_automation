import unittest
from commands.tv_commands import ChangeTVModeCommand
from receivers.tv import Tv
from receivers.exceptions import InvalidModeException


class TestChangeTvModeCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.tv = Tv("Test TV", available_modes=['Normal', 'Movie', 'Game'])
        self.command = ChangeTVModeCommand(self.tv, 'Movie')

    def test_execute_valid_mode(self):
        self.command.execute()
        self.assertEquals(self.tv.mode, 'Movie')

    def test_execute_invalid_mode(self):
        self.command = ChangeTVModeCommand(self.tv, 'Invalid')
        with self.assertRaises(InvalidModeException):
            self.command.execute()
