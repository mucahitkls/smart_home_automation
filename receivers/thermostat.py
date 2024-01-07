
class Thermostat:
    def __init__(self, name: str, min_temp: int = -10, max_temp: int = 120):
        self.name = name
        self.state = "off"
        self.temperature = 20
        self.min_temp = min_temp
        self.max_temp = max_temp

        self.history = []

    def turn_on(self):
        self.state = "on"
        print(f"{self.name}: Thermostat turned on")

    def turn_off(self):
        self.state = "off"
        print(f"{self.name}: Thermostat turned off")

    def change_temperature(self, value: int):
        new_temp = max(self.min_temp, min(value, self.max_temp))
        if self.history and self.history[-1] == new_temp:
            print(f"{self.name}: Temperature is already set to {new_temp}")
        else:
            self.temperature = new_temp
            self.history.append(self.temperature)
            print(f"{self.name}: Temperature set to : {self.temperature}")
