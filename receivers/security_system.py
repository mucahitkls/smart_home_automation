from utils.logger import logger_setup

logger = logger_setup(__name__)


class SecuritySystem:
    def __init__(self, name: str):
        self.name = name if isinstance(name, str) else "Unnamed Security System"
        self.state = "closed"
        self.lock_state = "locked"

    def open_door(self):
        if self.lock_state == "locked":
            logger.info(f"{self.name}: Cannot open door; it is locked.")
            return
        if self.state == "closed":
            self.state = "open"
            logger.info(f"{self.name}: Door opened")
            return
        logger.info(f"{self.name}: Door is already open")

    def close_door(self):
        if self.state == "open":
            self.state = "closed"
            logger.info(f"{self.name}: Door closed")
            return
        logger.info(f"{self.name}: Door is already closed")

    def lock_door(self):
        if self.state == "open":
            logger.info(f"{self.name}: Cannot lock the door; it is open.")
            return
        if self.lock_state == "unlocked":
            self.lock_state = "locked"
            logger.info(f"{self.name}: Door locked")
            return
        logger.info(f"{self.name}: Door is already locked")

    def unlock_door(self):
        if self.lock_state == "locked":
            self.lock_state = "unlocked"
            logger.info(f"{self.name}: Door unlocked")
            return
        logger.info(f"{self.name}: Door is already unlocked")

    def get_status(self):
        return {"name": self.name, "door_state": self.state, "lock_state": self.lock_state}
