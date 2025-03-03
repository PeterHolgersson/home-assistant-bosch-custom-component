"""Connector."""
from .http import HttpConnector

from ..const import HTTP

def connector_ivt_chooser(session_type):
    """Default connector HTTP."""
    return HttpConnector

__all__ = [
    "HttpConnector",
]
