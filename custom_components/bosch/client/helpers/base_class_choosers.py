"""Helpers to Choose Main class"""
from ..const import IVT
from ..gateway import IVTGateway


def gateway_chooser(device_type=IVT):
    return IVTGateway
   