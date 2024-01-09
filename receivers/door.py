from common_classes import CommonLockableDevice


class Door:
    def __init__(self, name: str):
        self.common_device = CommonLockableDevice(device_type='Door', name=name)

    def open(self):
        self.common_device.open()

    def close(self):
        self.common_device.close()

    def lock(self):
        self.common_device.lock()

    def unlock(self):
        self.common_device.unlock()

    @property
    def name(self):
        return self.common_device.name

    @property
    def state(self):
        return self.common_device.state

    @property
    def lock_state(self):
        return self.common_device.lock_state


my_light = Door("Front Door")
print(my_light.state)
my_light.unlock()
my_light.open()
print(my_light.state)
