class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        self.history.append(command)
        command.execute()

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
