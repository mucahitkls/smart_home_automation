from common_classes import CommonLockableDevice
from receivers_schemas.door_schema import DoorDetails


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
    def device_type(self):
        return self.common_device.device_type

    @property
    def state(self):
        return self.common_device.state

    @property
    def lock_state(self):
        return self.common_device.lock_state

    def get_information(self):
        return DoorDetails(
            device_type=self.device_type,
            name=self.name,
            state=self.state,
            lock_state=self.lock_state
        )
