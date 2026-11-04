

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .status_response_data_connection_type import StatusResponseDataConnectionType
from .status_response_data_state import StatusResponseDataState
from .status_response_data_status import StatusResponseDataStatus


class StatusResponseData(UniversalBaseModel):
    battery_level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Battery level percentage
    """

    battery_temperature: typing.Optional[int] = pydantic.Field(default=None)
    """
    Battery temperature in Celsius
    """

    connection_type: typing.Optional[StatusResponseDataConnectionType] = pydantic.Field(default=None)
    """
    Type of connection used by the device
    """

    firmware_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware version of the device
    """

    last_activity: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp of the last activity from the device
    """

    state: typing.Optional[StatusResponseDataState] = pydantic.Field(default=None)
    """
    Latest state of the device
    """

    status: StatusResponseDataStatus = pydantic.Field()
    """
    Status of a device
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
