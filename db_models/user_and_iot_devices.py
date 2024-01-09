from database.database import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    status = Column(String(20), default='active')
    privileges = Column(String(20), default='regular')
    devices = relationship('Device', back_populates='owner')


class DeviceTypeModel(Base):
    __tablename__ = 'device_types'
    device_type_id = Column(Integer, primary_key=True)
    type_name = Column(String(50), unique=True, nullable=False)
    devices = relationship('Device', back_populates='device_type')


class Device(Base):
    __tablename__ = 'devices'
    device_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    device_type_id = Column(Integer, ForeignKey('device_types.device_type_id'))
    name = Column(String(50))
    state = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    owner = relationship("User", back_populates='devices')
    device_type = relationship('DeviceType', back_populates='devices')
    light_attributes = relationship('LightAttributes', back_populates='device', uselist=False)
    thermostat_attributes = relationship('ThermostatAttributes', back_populates='device', uselist=False)
    tv_attributes = relationship('TvAttributes', back_populates='device', uselist=False)
    door_attributes = relationship('DoorAttributes', back_populates='device', uselist=False)


class LightAttributes(Base):
    __tablename__ = 'light_attributes'
    light_id = Column(Integer, ForeignKey('devices.device_id'), primary_key=True)
    color = Column(String(50))
    brightness = Column(Integer)
    mode = Column(String(50))
    available_modes = Column(JSON)
    device = relationship('Device', back_populates='light_attributes')


class ThermostatAttributes(Base):
    __tablename__ = 'thermostat_attributes'
    thermostat_id = Column(Integer, ForeignKey('devices.device_id'), primary_key=True)
    current_temperature = Column(Integer)
    min_temperature = Column(Integer)
    max_temperature = Column(Integer)
    mode = Column(String(50))
    available_modes = Column(JSON)
    device = relationship('Device', back_populates='thermostat_attributes')


class TvAttributes(Base):
    __tablename__ = 'tv_attributes'
    tv_id = Column(Integer, ForeignKey('devices.device_id'), primary_key=True)
    current_channel = Column(Integer)
    current_volume = Column(Integer)
    current_mode = Column(String(50)),
    max_channel = Column(Integer)
    max_volume = Column(Integer)
    available_modes = Column(JSON)
    device = relationship('Device', back_populates='tv_attributes')


class DoorAttributes(Base):
    __tablename__ = 'door_attributes'
    door_id = Column(Integer, ForeignKey('devices.device_id'), primary_key=True)
    lock_state = Column(String(50))
    device = relationship('Device', back_populates='door_attributes')


Base.metadata.create_all(engine)
