from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import crud_device_type
from db_models.user_and_iot_devices import Device, LightAttributes
from db_schemas import device_types, devices
from typing import Optional
from utils.logger import logger_setup

logger = logger_setup(__name__)


def get_device_by_id(db: Session, device_id: int) -> Optional[devices.Device]:
    try:
        return db.query(Device).filter(Device.device_id == device_id).first()

    except SQLAlchemyError as e:
        logger.error(f"Error retrieving device by id: {device_id}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error retrieving device by id: {device_id}: {e}")
    return None


def get_device_by_name(db: Session, device_name: str) -> Optional[devices.Device]:
    try:
        return db.query(Device).filter(Device.name == device_name).first()
    except SQLAlchemyError as e:
        logger.error(f"Error when retrieving device by name: {device_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error when retrieving device by name: {device_name}: {e}")
    return None


def create_new_light_device(db: Session, user_id: int, device_type_name: str, device_name: str, state: str, brightness: int = 0 , mode: str = 'normal') -> Optional[
    devices.Device]:
    try:
        new_device_type = crud_device_type.create_new_device_type(db=db, device_type_name=device_type_name)
        new_device = Device(
            user_id=user_id,
            device_type_id=new_device_type.device_type_id,
            name=device_name,
            state=state
        )
        db.add(new_device)
        db.commit()
        db.refresh(new_device)
        light_attributes = LightAttributes(brightness=0, color="white", mode="normal", device=new_device)
        db.add(light_attributes)

        db.commit()
        db.refresh(new_device)
        return new_device

    except SQLAlchemyError as e:
        logger.error(f"Error when creating device by name: {device_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error when creating device by name: {device_name}: {e}")
    return None
