from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from db_models.user_and_iot_devices import DeviceTypeModel
from db_schemas.device_types import DeviceType, DeviceTypeResponse
from utils.logger import logger_setup

logger = logger_setup(__name__)


def get_device_type_by_id(db: Session, device_type_id: int) -> Optional[DeviceTypeResponse]:
    try:
        return db.query(DeviceTypeModel).filter(DeviceTypeModel.device_type_id == device_type_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving device type by id {device_type_id}: {e}")
        return None


def get_device_type_by_name(db: Session, type_name: str):
    try:
        return db.query(DeviceTypeModel).filter(DeviceTypeModel.type_name == type_name).first()
    except SQLAlchemyError as e:
        logger.error(f"Error when retrieving device type by name: {type_name}: {e}")
        return None


def create_new_device_type(db: Session, device_type_name: str) -> Optional[DeviceTypeResponse]:
    db_device_type = DeviceTypeModel(type_name=device_type_name)
    try:
        db.add(db_device_type)
        db.commit()
        db.refresh(db_device_type)
        return db_device_type

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error when creating device type by name: {device_type_name}: {e}")
        return None


def update_device_type(db: Session, device_type: DeviceTypeResponse) -> Optional[DeviceTypeResponse]:
    db_device_type = get_device_type_by_id(db, device_type.device_type_id)
    if not db_device_type:
        logger.warning(f"Device type with ID {device_type.device_type_id} not found.")
        return None

    db_device_type.type_name = device_type.type_name
    try:
        db.commit()
        db.refresh(db_device_type)
        return db_device_type
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error updating device type {device_type.device_type_id}: {e}")
        return None


def delete_device_type(db: Session, device_type: DeviceTypeResponse):
    db_device_type = get_device_type_by_id(db=db, device_type_id=device_type.device_type_id)
    if not db_device_type:
        return False
    try:
        db.delete(db_device_type)
        db.commit()
    except SQLAlchemyError as e:
        logger.error(f"Error when deleting device type by name: {device_type.type_name}: {e}")
    finally:
        db.close()
