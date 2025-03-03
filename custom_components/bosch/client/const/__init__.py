"""Constants for the IVT component."""
ABSOLUTE = "absolute"
ACCESS_KEY = "access_key"
ACTIVE_PROGRAM = "activeProgram"
APP_JSON = "application/json"
AUTO = "auto"
BASE_FIRMWARE_VERSION = "versionFirmwarePath"
BINARY = "binary"
BODY_400 = "400Error"
BS = 16
BOSCH_NAME = "boschname"
CONTENT_TYPE = "Content-Type"
CRAWL_SENSORS = "crawlSensors"
CURRENT_TEMP = "current_temp"
DATE = "dateTime"
DAYS = {
    "Mo": "monday",
    "Tu": "tuesday",
    "We": "wednesday",
    "Th": "thursday",
    "Fr": "friday",
    "Sa": "saturday",
    "Su": "sunday",
}
DAYS_INDEXES = [k for k in DAYS.values()]
DAYS_INT = [k for k in DAYS.keys()]
DAYS_INV = [{v: k for k, v in DAYS.items()}]
DB_RECORD = "db_record"
DEEP = "deep"
DEFAULT = "default"
DEFAULT_MIN_TEMP = 0
DEFAULT_MAX_TEMP = 100
DEFAULT_MAX_HC_TEMP = 30
DEFAULT_MIN_HC_TEMP = 5
DEFAULT_STEP = "defaultStep"
DEVICE_CLASS = "device_class"
DHW = "dhw"
DHW_CIRCUITS = "dhwCircuits"
DV = "device"
ECUS_RECORDING = "ecus_recording"
EMS = "EMS"
ENERGY = "energy"
ENERGY_HISTORY = "/energy/history"
ENERGY_HISTORY_ENTRIES = "/energy/historyEntries"
ENERGY_KILO_WATT_HOUR = "kWh"
ENERGY_WATT_HOUR = "Wh"
FIRMWARE_VERSION = "versionFirmware"
FALSE = "false"
GATEWAY = "gateway"
GET = "get"
HA_NAME = "haname"
HA_STATES = "hastates"
HC = "hc"
HEATING_CIRCUITS = "heatingCircuits"
HTTP = "HTTP"
HVAC_ACTION = "hvacAction"
HVAC_HEAT = "heat"
HVAC_OFF = "off"
ID = "id"
INTERVAL = "interval"
K_DAY = "key_day"
K_SETPOINT = "key_setpoint"
K_TIME = "key_time"
LEVELS = "levels"
MANUAL = "manual"
MAX = "max"
MAX_REF = "max_ref"
MAX_VALUE = "maxValue"
MIN = "min"
MIN_REF = "min_ref"
MIN_VALUE = "minValue"
MODE = "mode"
MODE_TO_SETPOINT = "mode_to_setpoint"
MODELS = "models"
NAME = "name"
NUMBER = "number"
OFF = "off"
ON = "on"
OPERATION_MODE = "operation_mode"
PAGINATION = "pagination"
PATH = "path"
PROGRAM = "program"
PUT = "put"
RECORDING = "recording"
RECORDINGS = "recordings"
RECORDERDRES = "recordedResource"
REFERENCES = "references"
REFS = "refs"
REGULAR = "regular"
RESULT = "result"  # to not mismarch with value
REQUEST_TIMEOUT = 6
ROOT_PATHS = [
    "/systemStates",
    "/dhwCircuits",
    "/gateway",
    "/heatingCircuits",
    "/heatSources",
    "/notifications",
    "/system",
    "/solarCircuits",
    "/recordings",
    "/devices",
    "/energy",
    "/events",
    "/programs",
    "/zones",
    "/ecus",
    "/application",
    "/gservice_tariff",
]
SC = "sc"
SCHEDULE = "schedule"
SECOND = "s"
SELECT = "select"
SENSOR = "sensor"
SENSOR_TYPE = "sensorType"
SENSORS = "sensors"
SETPOINT = "setpoint"
SOLAR_CIRCUITS = "solarCircuits"
STATE_CLASS = "state_class"
STATUS = "status"
STEP_SIZE = "step_size"
SWITCH = "switch"
SWITCH = "switch"
SWITCHES = "switches"
SWITCHPROGRAM = "switchprogram"
SWITCHPROGRAM_MODE = "switchProgramMode"
SWITCH_PROGRAMS = "switchPrograms"
SYSTEM_BUS = "systemBus"
TEMP_CELSIUS = "°C"
TIMEOUT = 10
TIMESTAMP = "timestamp"
TRUE = "true"
TURN_OFF = "turn_off"
TURN_ON = "turn_on"
TYPE = "type"
UNITS = "unitOfMeasure"
UUID = "uuid"
URI = "uri"
USED = "used"
USER_AGENT = "User-Agent"
VALUE = "value"
VALUES = "values"
WRITE = "write"
WRITEABLE = "writeable"
WRONG_ENCRYPTION = "WrongEncryption"
XMPP = "XMPP"
ZN = "zn"
ZONES = "zones"

NEFIT = "NEFIT"
PROGRAM_LIST = "programList"
EASYCONTROL = "EASYCONTROL"
DV = "dv"
DEVICES = "devices"
CIRCUIT_TYPES = {
    DHW: DHW_CIRCUITS,
    ZN: ZONES,
    DV: DEVICES,
    HC: HEATING_CIRCUITS,
    SC: SOLAR_CIRCUITS
    }
