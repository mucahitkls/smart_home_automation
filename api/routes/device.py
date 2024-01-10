from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
import db_models.user_and_iot_devices as device_models
import db_schemas.devices as device_schemas
from database.database import get_db
from database import crud_device
from services import authentication

router = APIRouter(
    prefix='/device',
    tags=['device'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/', response_model=Optional[List[device_schemas.Device]])
async def get_device(skip: int, limit: int = 100, db: Session = Depends(get_db)):
    return crud_device.get_devices(db=db, skip=skip, limit=limit)


@router.get('/{device_id', response_model=Optional[device_schemas.Device])
async def get_device_by_id(device_id: int, db: Session = Depends(get_db)):
    db_device = crud_device.get_device_by_id(db=db, device_id=device_id)
    if not db_device:
        raise HTTPException(status_code=404, detail='Device type not found')
    return db_device


@router.post('/lights', response_model=Optional[device_schemas.LightAttributesInDB])
async def create_new_lights(user_id: int, light_name: str, light: device_schemas.LightAttributesCreate,
                            db: Session = Depends(get_db)):
    return crud_device.create_new_light_device(db=db, light_name=light_name, light=light)


@router.post('/tvs', response_model=Optional[device_schemas.TvAttributesInDB])
async def create_new_tvs(user_id: int, tv_name: str, tv: device_schemas.TvAttributesCreate,
                         db: Session = Depends(get_db)):
    return crud_device.create_new_tv_device(db=db, tv_name=tv_name, tv=tv)


@router.post('/thermostats', response_model=Optional[device_schemas.ThermostatAttributesCreate])
async def create_new_thermostat_device(user_id: int, thermostat_name: str,
                                       thermostat: device_schemas.ThermostatAttributesCreate,
                                       db: Session = Depends(get_db)):
    return crud_device.create_new_thermostat_device(db=db, thermostat_name=thermostat_name, thermostat=thermostat)


@router.post('/doors', response_model=Optional[device_schemas.DoorAttributesInDB])
async def create_new_thermostat_device(user_id: int, door_name: str,
                                       door: device_schemas.DoorAttributesCreate,
                                       db: Session = Depends(get_db)):
    return crud_device.create_new_door_device(db=db, door_name=door_name, door=door)


@router.put('/{device_id', response_model=device_schemas.Device)
async def update_device(device_id: int, device: device_schemas.Device, db: Session = Depends(get_db)):
    return crud_device.update_device(db=db, device=device)


@router.delete('/{device_id}')
async def update_device(device_id: int, db: Session = Depends(get_db)):
    return crud_device.delete_device(db=db, device_id=device_id)
