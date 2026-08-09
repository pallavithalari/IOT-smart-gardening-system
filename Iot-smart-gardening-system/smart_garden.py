from dataclasses import dataclass
from config import (
    SOIL_DRY_THRESHOLD,
    SOIL_WET_THRESHOLD,
    TEMPERATURE_HIGH,
    LIGHT_LOW_THRESHOLD
)


@dataclass
class SensorData:
    soil_moisture: float
    temperature: float
    humidity: float
    light_level: float
    rain_detected: bool


@dataclass
class ActuatorState:
    water_pump: bool = False
    cooling_fan: bool = False
    grow_light: bool = False


class SmartGarden:
    """
    IoT Smart Gardening Controller.

    Sensors:
        - Soil moisture
        - Temperature
        - Humidity
        - Light level
        - Rain sensor

    Actuators:
        - Water pump
        - Cooling fan
        - Grow light
    """

    def __init__(self):
        self.actuators = ActuatorState()

    def process_sensor_data(self, sensors: SensorData):
        """
        Decide actuator states based on sensor readings.
        """

        # Watering logic
        # Do not water when rain is detected.
        if (
            sensors.soil_moisture < SOIL_DRY_THRESHOLD
            and not sensors.rain_detected
        ):
            self.actuators.water_pump = True
        else:
            self.actuators.water_pump = False

        # Cooling logic
        if sensors.temperature > TEMPERATURE_HIGH:
            self.actuators.cooling_fan = True
        else:
            self.actuators.cooling_fan = False

        # Grow light logic
        if sensors.light_level < LIGHT_LOW_THRESHOLD:
            self.actuators.grow_light = True
        else:
            self.actuators.grow_light = False

        return self.actuators

    def get_status(self):
        return {
            "water_pump": self.actuators.water_pump,
            "cooling_fan": self.actuators.cooling_fan,
            "grow_light": self.actuators.grow_light
        }


def print_system_status(sensors, actuators):
    print("\n========== SMART GARDEN ==========")

    print(f"Soil Moisture : {sensors.soil_moisture:.1f}%")
    print(f"Temperature   : {sensors.temperature:.1f} C")
    print(f"Humidity      : {sensors.humidity:.1f}%")
    print(f"Light Level   : {sensors.light_level:.1f}%")
    print(
        f"Rain Detected : "
        f"{'YES' if sensors.rain_detected else 'NO'}"
    )

    print("\nActuators:")

    print(
        f"Water Pump    : "
        f"{'ON' if actuators.water_pump else 'OFF'}"
    )

    print(
        f"Cooling Fan   : "
        f"{'ON' if actuators.cooling_fan else 'OFF'}"
    )

    print(
        f"Grow Light    : "
        f"{'ON' if actuators.grow_light else 'OFF'}"
    )

    print("==================================")