from database.database import SessionLocal, Base, get_db
from db_models.user_and_iot_devices import Device, DeviceTypeModel, LightAttributes
from database import crud_device_type, crud_device, crud_user

db = SessionLocal()  # Assuming you've already set up your database session

user_id = 1
# Assuming device_type_id for a light is already known
light_device_type_id = crud_device_type.create_or_get_device_type(db, "Light")  # Fetch or define a function to get the correct device_type_id
# Create a generic device entry
new_device = Device(user_id=user_id, device_type_id=light_device_type_id.device_type_id, name="Zort Room Light", state="off")
db.add(new_device)
db.commit()
db.refresh(new_device)

# Now, create specific light attributes
light_attributes = LightAttributes(light_id=new_device.device_id, brightness=50, color="#ERTSFS", mode='Normal', available_modes=['Normal', 'Game'])
db.add(light_attributes)
db.commit()
