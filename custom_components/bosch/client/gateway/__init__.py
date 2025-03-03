from .ivt import IVTGateway
from ..const.ivt import IVT

def gateway_chooser(device_type=IVT):
    return {
        IVT: IVTGateway,
    }[device_type]
