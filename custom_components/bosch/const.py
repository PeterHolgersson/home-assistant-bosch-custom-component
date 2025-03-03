"""Constants for the bosch component."""
from datetime import timedelta

import voluptuous as vol
from .client.const import DHW, HC, SC, ZN
from .client.const import DV
from homeassistant.const import UnitOfEnergy, UnitOfTemperature, UnitOfTime

# Assign variables
VALUE = "value"
START = "start"
STOP = "stop"

ACCESS_KEY = "access_key"
ACCESS_TOKEN = "access_token"
BINARY_SENSOR = "binary_sensor"

BOSCH_GATEWAY_ENTRY = "BoschGatewayEntry"
BOSCH_STATE = "bosch_state"
CHARGE = "charge"
CIRCUITS = [DHW, HC, SC, ZN, DV]

CIRCUITS_SENSOR_NAMES = {
    DHW: "Water heater",
    HC: "Heating circuit",
    SC: "Solar circuit",
    ZN: "Zone circuit",
    DV: "Device",
}
CLIMATE = "climate"
CONF_DEVICE_TYPE = "device_type"
CONF_PROTOCOL = "http_xmpp"

DEFAULT_MIN_TEMP = 0
DEFAULT_MAX_TEMP = 100

DOMAIN = "bosch"
FW_INTERVAL = "fw_interval"
FIRMWARE_SCAN_INTERVAL = timedelta(hours=4)

GATEWAY = "gateway"
INTERVAL = "interval"
LAST_RESET = "last_reset"
MINS = "mins"
NOTIFICATION_ID = "bosch_notification"
RECORDING_INTERVAL = "recording_interval"
RECORDING_SERVICE_UPDATE = "update_recordings_sensor"

SCAN_INTERVAL = timedelta(seconds=60)
SCAN_SENSOR_INTERVAL = timedelta(seconds=120)
SENSORS = "sensors"
SERVICE_CHARGE_SCHEMA = {vol.Optional(VALUE): vol.In([START, STOP])}
SERVICE_CHARGE_START = "set_dhw_charge"
SERVICE_DEBUG = "debug_scan"
SERVICE_GET = "send_custom_get"
SERVICE_MOVE_OLD_DATA = "move_old_statistic_data"
SERVICE_PUT_FLOAT = "send_custom_put_float"
SERVICE_PUT_STRING = "send_custom_put_string"
SERVICE_UPDATE = "update_thermostat"

SIGNAL_BINARY_SENSOR_UPDATE_BOSCH = "bosch_binarysensor_update"
SIGNAL_BOSCH = "bosch_signal"
SIGNAL_CLIMATE_UPDATE_BOSCH = "bosch_climate_update"
SIGNAL_DHW_UPDATE_BOSCH = "bosch_dhw_update"
SIGNAL_ENERGY_UPDATE_BOSCH = "bosch_energy_update"
SIGNAL_NUMBER = "bosch_number_update"
SIGNAL_SELECT = "bosch_select_update"
SIGNAL_SENSOR_UPDATE_BOSCH = "bosch_sensor_update"
SIGNAL_RECORDING_UPDATE_BOSCH = "bosch_recording_update"
SIGNAL_SOLAR_UPDATE_BOSCH = "bosch_solar_update"
SIGNAL_SWITCH = "bosch_switch_update"

SOLAR = "solar"
SWITCH = "switch"
SWITCHPOINT = "switchPoint"
UUID = "uuid"


UNITS_CONVERTER = {
    "C": UnitOfTemperature.CELSIUS,
    UnitOfTemperature.CELSIUS: UnitOfTemperature.CELSIUS,
    "F": UnitOfTemperature.FAHRENHEIT,
    UnitOfTemperature.FAHRENHEIT: UnitOfTemperature.FAHRENHEIT,
    "%": "%",
    "l/min": "l/min",
    "l/h": "l/h",
    "kg/l": "kg/l",
    "mins": UnitOfTime.MINUTES,
    UnitOfTime.MINUTES: UnitOfTime.MINUTES,
    "kW": "kW",
    "kWh": UnitOfEnergy.KILO_WATT_HOUR,
    "Wh": "Wh",
    "Pascal": "Pascal",
    "bar": "bar",
    "µA": "µA",
    "s" : UnitOfTime.SECONDS,
    UnitOfTime.SECONDS: UnitOfTime.SECONDS,
    " ": None,
}
WATER_HEATER = "water_heater"
