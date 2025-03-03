"""Encryption logic of Bosch thermostat."""
from ..const.ivt import MAGIC_IVT

from .base import BaseEncryption


class IVTEncryption(BaseEncryption):
    """Encryption class."""

    magic = MAGIC_IVT
