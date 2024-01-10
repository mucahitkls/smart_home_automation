from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import crud_device_type
import db_models.user_and_iot_devices as device_models
import db_schemas.devices as device_schemas
from typing import Optional, List
from utils.logger import logger_setup

logger = logger_setup(__name__)


def get_device_by_id(db: Session, device_id: int) -> Optional[device_schemas.Device]:
    try:
        return db.query(device_models.Device).filter(device_models.Device.device_id == device_id).first()

    except SQLAlchemyError as e:
        logger.error(f"Error retrieving device by id: {device_id}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error retrieving device by id: {device_id}: {e}")
    return None


def get_device_by_name(db: Session, device_name: str) -> Optional[device_schemas.Device]:
    try:
        return db.query(device_models.Device).filter(device_models.Device.name == device_name).first()
    except SQLAlchemyError as e:
        logger.error(f"Error when retrieving device by name: {device_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error when retrieving device by name: {device_name}: {e}")
    return None


def get_devices(db: Session, skip: int = 0, limit: int = 100):
    try:
        devices = db.query(device_models.Device).offset(skip=skip).limit(limit=limit).all()
        return devices
    except SQLAlchemyError as e:
        logger.error(f'Error when retrieving devices: {e}')
    except Exception as e:
        logger.error(f'Error when retrieving devices: {e}')
    return None


def create_new_light_device(db: Session, user_id: int, light_name: str, light: device_schemas.LightAttributesCreate) -> Optional[
    device_schemas.Device]:
    try:
        new_device_type = crud_device_type.create_new_device_type(db=db, device_type_name='Light')
        new_device = device_models.Device(
            user_id=user_id,
            device_type_id=new_device_type.device_type_id,
            name=light_name,
            state='off'
        )
        db.add(new_device)
        db.commit()
        db.refresh(new_device)
        light_attributes = device_models.LightAttributes(brightness=light.brightness, color=light.color, mode=light.mode, device=new_device)
        db.add(light_attributes)

        db.commit()
        db.refresh(new_device)
        return new_device

    except SQLAlchemyError as e:
        logger.error(f"Error when creating device by name: {light_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error when creating device by name: {light_name}: {e}")
    return None


def create_new_tv_device(db: Session, user_id: int, tv_name: str, tv: device_schemas.TvAttributesCreate) -> Optional[device_schemas.Device]:
    try:
        new_device_type = crud_device_type.create_new_device_type(db=db, device_type_name='Tv')
        new_device = device_models.Device(
            user_id=user_id,
            device_type_id=new_device_type.device_type_id,
            name=tv_name,
            state='off'
        )
        db.add(new_device)
        db.commit()
        db.refresh(new_device)

        tv_attributes = device_models.TvAttributes(
            current_channel=tv.current_channel,
            current_volume=tv.current_volume,
            current_mode=tv.current_mode,
            available_modes=tv.available_modes,
            device=new_device
        )
        db.add(tv_attributes)
        db.commit()
        db.refresh(new_device)

        return new_device

    except SQLAlchemyError as e:
        logger.error(f"Error when creating TV device by name: {tv_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error when creating TV device by name: {tv_name}: {e}")
    return None


def create_new_thermostat_device(db: Session, user_id: int, thermostat_name: str, thermostat: device_schemas.ThermostatAttributesCreate) -> Optional[device_schemas.Device]:
    try:
        new_device_type = crud_device_type.create_new_device_type(db=db, device_type_name='Thermostat')
        new_device = device_models.Device(
            user_id=user_id,
            device_type_id=new_device_type.device_type_id,
            name=thermostat_name,
            state='off'
        )
        db.add(new_device)
        db.commit()
        db.refresh(new_device)

        thermostat_attributes = device_models.ThermostatAttributes(
            current_temperature=thermostat.current_temperature,
            mode=thermostat.mode,
            available_modes=thermostat.available_modes,
            device=new_device
        )
        db.add(thermostat_attributes)
        db.commit()
        db.refresh(new_device)

        return new_device

    except SQLAlchemyError as e:
        logger.error(f"Error when creating Thermostat device by name: {thermostat_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error when creating Thermostat device by name: {thermostat_name}: {e}")
    return None


def create_new_door_device(db: Session, user_id: int, door_name: str, door: device_schemas.DoorAttributesCreate):
    try:
        new_device_type = crud_device_type.create_new_device_type(db=db, device_type_name='Door')
        new_device = device_models.Device(
            user_id=user_id,
            device_type_id=new_device_type.device_type_id,
            name=door_name,
            state='closed'
        )
        db.add(new_device)
        db.commit()
        db.refresh(new_device)

        door_attributes = device_models.DoorAttributes(
            lock_state=door.lock_state,
            device=new_device
        )
        db.add(door_attributes)
        db.commit()
        db.refresh(new_device)
        return new_device

    except SQLAlchemyError as e:
        logger.error(f"Error when creating Thermostat device by name: {door_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error when creating Thermostat device by name: {door_name}: {e}")
    return None


def update_device_by_id(db: Session, device: device_schemas.Device):
    try:
        device_to_update = db.query(device_models.Device).filter_by(device_id=device.device_id).first()
        if device_to_update:
            # Update fields only if they are different to minimize unnecessary writes
            if device_to_update.device_type_id != device.device_type_id:
                device_to_update.device_type_id = device.device_type_id
            if device_to_update.name != device.name:
                device_to_update.name = device.name
            if device_to_update.state != device.state:
                device_to_update.state = device.state

            db.commit()
        else:
            logger.warning(f'Device with id {device.device_id} not found.')

    except SQLAlchemyError as e:
        db.rollback()  # Rollback in case of SQLAlchemy errors
        logger.error(f'Error when updating device by id {device.device_id}: {e}')

    except Exception as e:
        logger.error(f'Unexpected error when updating device by id {device.device_id}: {e}')


def delete_device(db: Session, device_id: int):
    try:
        device_to_delete = db.query(device_models.Device).filter_by(device_id=device_id).first()
        if device_to_delete:
            db.delete(device_to_delete)
            db.commit()
        else:
            logger.warning(f'Device with id {device_id} not found.')
            return False

    except SQLAlchemyError as e:
        db.rollback()  # Rollback in case of SQLAlchemy errors
        logger.error(f'Error when deleting device by id {device_id}: {e}')
        return False

    except Exception as e:
        logger.error(f'Unexpected error when deleting device by id {device_id}: {e}')
        return False

    return True
