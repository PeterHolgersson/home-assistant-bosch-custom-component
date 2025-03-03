"""Constants for the IVT component."""
from . import (
    USER_AGENT,
    CONTENT_TYPE,
    APP_JSON,
    HC,
    HEATING_CIRCUITS,
    DHW,
    DHW_CIRCUITS,
    SC,
    SOLAR_CIRCUITS,
)

# Assign variables
KEEP_ALIVE = "keep-alive"
TELEHEATER = "TeleHeater"

ALLOWED_VALUES = "allowedValues"
CAN = "CAN"
CURRENT_SETPOINT = "currentSetpoint"
CIRCUIT_TYPES = {HC: HEATING_CIRCUITS, DHW: DHW_CIRCUITS, SC: SOLAR_CIRCUITS}
CONNECTION = "Connection"
DAYOFWEEK = "dayOfWeek"
MAGIC_IVT = bytearray.fromhex(
    "867845e97c4e29dce522b9a7d3a3e07b152bffadddbed7f5ffd842e9895ad1e4"
)

HTTP_HEADER = {USER_AGENT: TELEHEATER, CONNECTION: KEEP_ALIVE, CONTENT_TYPE: APP_JSON}
INVALID = "invalid"
IVT = "IVT"
IVT_MBLAN = "IVT_MBLAN"
MBLAN = "mblan"
NSC_ICOM_GATEWAY = "NSC_ICOM_GATEWAY"
RC300_RC200 = "RC300_RC200"
READ = "read"
SETPOINT_PROP = "setpointProperty"
STATE = "state"
SWITCH_POINTS = "switchPoints"
# SYSTEM_BRAND = "brand"
SYSTEM_INFO = "systemInfo"
# SYSTEM_TYPE = "systemType"
TEMP = "temp"
TIME = "time"
WRITE = "write"
