# 🌱 IoT Smart Gardening System

An IoT-based Smart Gardening System implemented in Python.

The system monitors environmental conditions such as soil moisture, temperature, humidity, light intensity, and rain. Based on these readings, it automatically controls a water pump, cooling fan, and grow light.

This repository includes a complete software simulation and automated test bench, allowing the project to be demonstrated without physical IoT hardware.

---

## Features

* 🌱 Soil moisture monitoring
* 💧 Automatic irrigation control
* 🌡️ Temperature monitoring
* 🌀 Automatic cooling fan control
* ☀️ Light-level monitoring
* 💡 Automatic grow-light control
* 🌧️ Rain detection
* 🧪 Automated Python test bench
* 🖥️ Console-based simulation
* 📁 GitHub-ready project structure
* 🔌 Easy to adapt to Raspberry Pi or ESP32

---

## System Architecture

```text
             ┌─────────────────────┐
             │   Sensors           │
             │                     │
             │ Soil Moisture       │
             │ Temperature         │
             │ Humidity             │
             │ Light Level          │
             │ Rain Sensor          │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Smart Garden        │
             │ Controller          │
             │                     │
             │ Python Decision     │
             │ Logic               │
             └──────────┬──────────┘
                        │
            ┌───────────┼───────────┐
            │           │           │
            ▼           ▼           ▼
        ┌───────┐   ┌───────┐   ┌──────────┐
        │ Pump  │   │ Fan   │   │ Grow     │
        │       │   │       │   │ Light    │
        └───────┘   └───────┘   └──────────┘
```

---

## Control Logic

### Water Pump

The pump is switched ON when:

```text
Soil moisture < 35%
AND
Rain is not detected
```

Otherwise, the pump remains OFF.

### Cooling Fan

The cooling fan is switched ON when:

```text
Temperature > 32°C
```

Otherwise, it remains OFF.

### Grow Light

The grow light is switched ON when:

```text
Light level < 30%
```

Otherwise, it remains OFF.

---

## Project Structure

```text
iot-smart-gardening/
│
├── README.md
├── requirements.txt
├── config.py
├── smart_garden.py
├── run_demo.py
├── test_smart_garden.py
│
└── output/
    └── sample_output.txt
```

---

## Software Requirements

* Python 3.9 or newer
* Git
* Any code editor such as VS Code

No external Python libraries are required for the basic simulation.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/iot-smart-gardening.git
```

Enter the project directory:

```bash
cd iot-smart-gardening
```

---

## Run the Simulation

Run:

```bash
python run_demo.py
```

The program simulates different environmental conditions and displays the corresponding actuator states.

Example:

```text
TEST CASE: Dry Soil

Soil Moisture : 20.0%
Temperature   : 25.0 C
Humidity      : 60.0%
Light Level   : 70.0%
Rain Detected : NO

Water Pump    : ON
Cooling Fan   : OFF
Grow Light    : OFF
```

---

## Run the Test Bench

The project includes automated unit tests.

Run:

```bash
python -m unittest test_smart_garden.py -v
```

Expected result:

```text
test_fan_off_at_normal_temperature ... ok
test_fan_turns_on_at_high_temperature ... ok
test_grow_light_off_when_light_is_high ... ok
test_grow_light_on_when_light_is_low ... ok
test_pump_off_when_raining ... ok
test_pump_turns_off_when_soil_is_wet ... ok
test_pump_turns_on_when_soil_is_dry ... ok

----------------------------------------------------------------------
Ran 7 tests

OK
```

---

## Test Cases

| Test | Condition           | Expected Result |
| ---- | ------------------- | --------------- |
| 1    | Soil moisture = 20% | Pump ON         |
| 2    | Soil moisture = 80% | Pump OFF        |
| 3    | Dry soil + rain     | Pump OFF        |
| 4    | Temperature = 35°C  | Fan ON          |
| 5    | Temperature = 25°C  | Fan OFF         |
| 6    | Light = 10%         | Grow Light ON   |
| 7    | Light = 80%         | Grow Light OFF  |

---

## Hardware Version

The software can be extended to real IoT hardware.

Possible hardware:

* ESP32
* Raspberry Pi
* Soil moisture sensor
* DHT11/DHT22 temperature and humidity sensor
* LDR/light sensor
* Rain sensor
* Relay module
* DC water pump
* Cooling fan
* LED/grow light

A possible hardware architecture is:

```text
Soil Moisture Sensor ─┐
DHT11/DHT22 ───────────┤
LDR ───────────────────┤
Rain Sensor ───────────┤
                       ▼
                    ESP32
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Relay         Relay        Relay
          │            │            │
          ▼            ▼            ▼
      Water Pump      Fan       Grow Light
```

For a real installation, pumps and other loads should be driven through appropriately rated relay/MOSFET driver circuits rather than directly from GPIO pins.

---

## Future IoT Features

The project can be expanded with:

1. MQTT communication
2. ESP32 sensor nodes
3. Raspberry Pi gateway
4. Web dashboard
5. Mobile application
6. Cloud data storage
7. Historical sensor graphs
8. Email/notification alerts
9. Weather API integration
10. Automatic watering schedules
11. Multiple garden zones
12. Database logging

---

## Example Future MQTT Architecture

```text
                 Internet / Wi-Fi
                       │
                       ▼
                ┌─────────────┐
                │ MQTT Broker │
                └──────┬──────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        ESP32 Sensor        Python Server
             │                   │
             ▼                   ▼
       Garden Sensors       Web Dashboard
             │
             ▼
        Relay Control
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
     Pump   Fan   Light
```

---

## Educational Objectives

This project demonstrates:

* Python programming
* Object-oriented programming
* Sensor data processing
* Conditional control logic
* IoT system architecture
* Automated testing
* Simulation
* Hardware/software integration concepts

---

## License

This project is intended for educational and academic use. You may modify and extend it for your own projects.

---

## Author

**Your Name**

IoT Smart Gardening System
Python | IoT | Automation | Sensor Monitoring
