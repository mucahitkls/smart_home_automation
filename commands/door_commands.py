from base_command import Command
from receivers.door import Door


class OpenDoorCommand(Command):

    def __init__(self, door: Door):
        self.door = door
        self.previous_state = self.door.state

    def execute(self):
        self.door.open()

    def undo(self):
        if self.previous_state == 'open':
            self.door.close()


class CloseDoorCommand(Command):

    def __init__(self, door: Door):
        self.door = door
        self.previous_state = self.door.state

    def execute(self):
        self.door.close()

    def undo(self):
        if self.previous_state == 'closed':
            self.door.open()


class LockDoorCommand(Command):

    def __init__(self, door: Door):
        self.door = door
        self.previous_state = self.door.state

    def execute(self):
        self.door.lock()

    def undo(self):
        if self.previous_state == 'unlocked':
            self.door.unlock()


class UnlockDoorCommand(Command):

    def __init__(self, door: Door):
        self.door = door
        self.previous_state = self.door.state

    def execute(self):
        self.door.unlock()

    def undo(self):
        if self.previous_state == 'locked':
            self.door.lock()



