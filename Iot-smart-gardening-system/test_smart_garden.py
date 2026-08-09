import unittest

from smart_garden import SmartGarden, SensorData


class TestSmartGarden(unittest.TestCase):

    def setUp(self):
        self.garden = SmartGarden()

    def test_pump_turns_on_when_soil_is_dry(self):
        sensors = SensorData(
            soil_moisture=20,
            temperature=25,
            humidity=50,
            light_level=70,
            rain_detected=False
        )

        actuators = self.garden.process_sensor_data(sensors)

        self.assertTrue(actuators.water_pump)

    def test_pump_turns_off_when_soil_is_wet(self):
        sensors = SensorData(
            soil_moisture=80,
            temperature=25,
            humidity=60,
            light_level=70,
            rain_detected=False
        )

        actuators = self.garden.process_sensor_data(sensors)

        self.assertFalse(actuators.water_pump)

    def test_pump_off_when_raining(self):
        sensors = SensorData(
            soil_moisture=20,
            temperature=25,
            humidity=80,
            light_level=70,
            rain_detected=True
        )

        actuators = self.garden.process_sensor_data(sensors)

        self.assertFalse(actuators.water_pump)

    def test_fan_turns_on_at_high_temperature(self):
        sensors = SensorData(
            soil_moisture=60,
            temperature=35,
            humidity=50,
            light_level=70,
            rain_detected=False
        )

        actuators = self.garden.process_sensor_data(sensors)

        self.assertTrue(actuators.cooling_fan)

    def test_fan_off_at_normal_temperature(self):
        sensors = SensorData(
            soil_moisture=60,
            temperature=25,
            humidity=50,
            light_level=70,
            rain_detected=False
        )

        actuators = self.garden.process_sensor_data(sensors)

        self.assertFalse(actuators.cooling_fan)

    def test_grow_light_on_when_light_is_low(self):
        sensors = SensorData(
            soil_moisture=60,
            temperature=25,
            humidity=50,
            light_level=10,
            rain_detected=False
        )

        actuators = self.garden.process_sensor_data(sensors)

        self.assertTrue(actuators.grow_light)

    def test_grow_light_off_when_light_is_high(self):
        sensors = SensorData(
            soil_moisture=60,
            temperature=25,
            humidity=50,
            light_level=80,
            rain_detected=False
        )

        actuators = self.garden.process_sensor_data(sensors)

        self.assertFalse(actuators.grow_light)


if __name__ == "__main__":
    unittest.main()