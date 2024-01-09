db = Session()  # Assuming you've already set up your database session

# Assuming device_type_id for a light is already known
light_device_type_id = get_device_type_id(db, "light")  # Fetch or define a function to get the correct device_type_id

# Create a generic device entry
new_device = Device(user_id=user_id, device_type_id=light_device_type_id, name="Living Room Light", state="off")
db.add(new_device)
db.commit()
db.refresh(new_device)

# Now, create specific light attributes
light_attributes = LightAttributes(device_id=new_device.device_id, brightness=50, color="warm white")
db.add(light_attributes)
db.commit()
