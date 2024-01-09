class InvalidColorException(Exception):
    def __init__(self, color, message='Invalid color code provided'):
        self.color = color
        self.message = f'{message}: {color}'
        super().__init__(self.message)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"


class InvalidModeException(Exception):
    def __init__(self, mode, available_modes, message='Invalid mode provided'):
        self.mode = mode
        self.available_modes = available_modes
        self.message = f'{message}: {mode}'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}'


class InvalidValueException(Exception):
    def __init__(self, value, max_value, message='Invalid value provided'):
        self.value = value
        self.max_value = max_value
        self.message = f'{message}: {value}. Value should be between 0 and {max_value}'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}'


class NoUndoFoundException(Exception):
    def __init__(self, thing, message="No undo operation is found"):
        self.thing = thing
        self.message = f'{message} : {self.thing.name}'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}'


class NotDimmableDevice(Exception):
    def __init__(self, thing, message="Device is not dimmable"):
        self.thing = thing
        self.message = f'{message} : {self.thing.name}'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}'
