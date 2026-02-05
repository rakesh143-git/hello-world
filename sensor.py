sensor_data = [
    ("Sensor_A", "Field_1", "Temperature", "Celsius"),
    ("Sensor_B", "Field_2", "Humidity", "%"),
    ("Sensor_C", "Field_3", "Soil Moisture", "%"),
    ("Sensor_D", "Field_4", "Temperature", "Celsius"),
    ("Sensor_E", "Field_5", "Humidity", "%")
]
for sensor in sensor_data:
    print(sensor)
sensor_type_count = {}
for _, _, sensor_type, _ in sensor_data:
    sensor_type_count[sensor_type] = sensor_type_count.get(sensor_type, 0) + 1
print("\nSensor Type Count:")
for k, v in sensor_type_count.items():
    print(f"{k}: {v}")
temperature_sensors = [s for s in sensor_data if s[2] == "Temperature"]
print("\nTemperature Sensors:")
for t in temperature_sensors:
    print(t)
units = set(s[3] for s in sensor_data)
print("\nUnits Used:", units)
