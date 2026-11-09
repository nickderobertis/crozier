

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cellular_usage import CellularUsage
from .contact import Contact
from .device_tower_info import DeviceTowerInfo
from .dfu_env import DfuEnv
from .location import Location


class Device(UniversalBaseModel):
    best_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The best ID for the device, preference for the serial number over device UID
    """

    best_location: typing.Optional[Location] = None
    cellular_usage: typing.Optional[CellularUsage] = None
    contact: typing.Optional[Contact] = None
    dfu: typing.Optional[DfuEnv] = None
    disabled: typing.Optional[bool] = None
    firmware_host: typing.Optional[str] = None
    firmware_notecard: typing.Optional[str] = None
    fleet_uids: typing.List[str]
    gps_location: typing.Optional[Location] = None
    last_activity: typing.Optional[dt.datetime] = None
    product_uid: str
    provisioned: dt.datetime
    serial_number: typing.Optional[str] = None
    sku: typing.Optional[str] = None
    temperature: float
    tower_info: typing.Optional[DeviceTowerInfo] = None
    tower_location: typing.Optional[Location] = None
    triangulated_location: typing.Optional[Location] = None
    uid: str
    voltage: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
