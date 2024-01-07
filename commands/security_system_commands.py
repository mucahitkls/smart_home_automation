from base_command import Command
from receivers.security_system import SecuritySystem


class OpenDoorCommand(Command):

    def __init__(self, sec: SecuritySystem):
        self.security = sec

    def execute(self):
        self.security.open_door()

    def undo(self):
        self.security.close_door()


class CloseDoorCommand(Command):

    def __init__(self, sec: SecuritySystem):
        self.security = sec

    def execute(self):
        self.security.close_door()

    def undo(self):
        self.security.open_door()


class LockDoorCommand(Command):

    def __init__(self, sec: SecuritySystem):
        self.security = sec

    def execute(self):
        self.security.lock_door()

    def undo(self):
        self.security.unlock_door()


class UnlockDoorCommand(Command):

    def __init__(self, sec: SecuritySystem):
        self.security = sec

    def execute(self):
        self.security.unlock_door()

    def undo(self):
        self.security.lock_door()