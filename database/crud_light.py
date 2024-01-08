from sqlalchemy.orm import Session
from typing import Optional
from db_models import user_and_iot_devices
from db_schemas import device_types, devices
from utils.logger import logger_setup

logger = logger_setup(__name__)

def get_light_by_id(db: Session, light_id: int ) -> Optional[]
