""" Bosch Thermostat Number Entities."""

from __future__ import annotations
from homeassistant.components.number import NumberEntity
from .bosch_entity import BoschEntity
from bosch_thermostat_client.const import GATEWAY, NUMBER
from homeassistant.helpers.dispatcher import async_dispatcher_send
from .const import (
    CIRCUITS,
    CIRCUITS_SENSOR_NAMES,
    DOMAIN,
    SIGNAL_BOSCH,
    SIGNAL_NUMBER,
    UUID,
)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Bosch Water heater from a config entry."""
    uuid = config_entry.data[UUID]
    data = hass.data[DOMAIN][uuid]
    enabled_switches = config_entry.data.get(NUMBER, [])
    data_number = []
    for switch in data[GATEWAY].number_switches:
        data_number.append(
            BoschNumber(
                hass=hass,
                uuid=uuid,
                bosch_object=switch,
                gateway=data[GATEWAY],
                name=switch.name,
                attr_uri=switch.attr_id,
                domain_name="Switches",
                is_enabled=switch.attr_id in enabled_switches,
            )
        )
    for circ_type in CIRCUITS:
        circuits = data[GATEWAY].get_circuits(circ_type)
        for circuit in circuits:
            for switch in circuit.number_switches:
                data_number.append(
                    CircuitNumber(
                        hass=hass,
                        uuid=uuid,
                        bosch_object=switch,
                        gateway=data[GATEWAY],
                        name=switch.name,
                        attr_uri=switch.attr_id,
                        domain_name=circuit.name,
                        circuit_type=circ_type,
                        is_enabled=switch.attr_id in enabled_switches,
                    )
                )
    data[NUMBER] = data_number
    async_add_entities(data[NUMBER])
    async_dispatcher_send(hass, SIGNAL_BOSCH)
    return True


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Bosch Thermostat Platform."""
    pass


class BoschNumber(BoschEntity, NumberEntity):
    """Bosch number class represents HA Number entity."""

    signal = SIGNAL_NUMBER

    def __init__(
        self,
        hass,
        uuid,
        bosch_object,
        gateway,
        name,
        attr_uri,
        domain_name,
        circuit_type=None,
        is_enabled=False,
    ):
        """Set up device and add update callback to get data from websocket."""
        super().__init__(
            hass=hass, uuid=uuid, bosch_object=bosch_object, gateway=gateway
        )
        self._domain_name = domain_name
        self._name = name
        self._attr_uri = attr_uri
        self._state = bosch_object.state
        self._update_init = True
        self._unique_id = self._domain_name + self._name + self._uuid
        self._attrs = {}
        self._circuit_type = circuit_type
        self._is_enabled = is_enabled

    @property
    def device_name(self):
        return "Bosch switches"

    @property
    def _domain_identifier(self):
        return {(DOMAIN, self._domain_name + self._uuid)}

    @property
    def min_value(self) -> float:
        """Return the minimum value."""
        if self._bosch_object.min_value is None:
            return 0
        return float(self._bosch_object.min_value)

    @property
    def max_value(self) -> float:
        """Return the maximum value."""
        if self._bosch_object.max_value is None:
            return 255
        return float(self._bosch_object.max_value)

    @property
    def value(self) -> float | None:
        """Return the entity value."""
        if self._bosch_object.state is None:
            return None
        return float(self._bosch_object.state)

    @property
    def unit_of_measurement(self) -> str | None:
        """Return the unit of measurement of this entity, if any."""
        if self._bosch_object.unit_of_measurement is None:
            return None
        return str(self._bosch_object.unit_of_measurement)

    def update(self):
        """Update state of device."""
        pass

    async def async_set_value(self, value: float) -> None:
        """Set new value."""
        await self._bosch_object.set_value(value)

    @property
    def entity_registry_enabled_default(self):
        """Return if the entity should be enabled when first added to the entity registry."""
        return self._is_enabled


class CircuitNumber(BoschNumber):
    """Representation of a Bosch circuit number."""

    @property
    def device_name(self):
        return CIRCUITS_SENSOR_NAMES[self._circuit_type] + " " + self._domain_name
