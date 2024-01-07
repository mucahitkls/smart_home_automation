from core.invoker import Invoker
from receivers.light import Light
from commands.light_commands import TurnOnLightCommand, TurnOffLightCommand, ChangeBrightnessCommand

my_invoker = Invoker()

living_room_light = Light(name="Living Room", dimmable=True, max_brightness=100)

turn_on_light_command = TurnOnLightCommand(living_room_light)
dimm_light_command = ChangeBrightnessCommand(living_room_light, 80)

my_invoker.execute_command(turn_on_light_command)
my_invoker.execute_command(dimm_light_command)


