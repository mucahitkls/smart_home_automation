from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from db_schemas.device_types import DeviceType, DeviceTypeResponse
from database.database import get_db
from database import crud_device_type
from services import authentication

router = APIRouter(
    prefix='/device_types',
    tags=['device_types'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/', response_model=Optional[List[DeviceTypeResponse]])
async def get_device_types(skip: int, limit: int = 100, db: Session = Depends(get_db)):
    return crud_device_type.get_all_device_types(db=db, skip=skip, limit=limit)


@router.get('/{device_type_id', response_model=Optional[DeviceTypeResponse])
async def get_device_type_by_id(device_type_id: int, db: Session = Depends(get_db)):
    db_device_type = crud_device_type.get_device_type_by_id(db=db, device_type_id=device_type_id)
    if not db_device_type:
        raise HTTPException(status_code=404, detail='Device type not found')
    return db_device_type


@router.post('/', response_model=Optional[DeviceTypeResponse])
async def create_device_type(device_type: DeviceType, db: Session = Depends(get_db)):
    return crud_device_type.create_or_get_device_type(db=db, type_name=device_type.type_name)


@router.put('/{device_type_id', response_model=DeviceTypeResponse)
async def update_device_type(device_type_id: int, device_type: DeviceTypeResponse, db: Session = Depends(get_db)):
    return crud_device_type.update_device_type(db=db, device_type=device_type)


@router.delete('/{device_type_id}')
async def update_device_type(device_type_id: int, db: Session = Depends(get_db)):
    return crud_device_type.delete_device_type(db=db, device_type_id=device_type_id)
