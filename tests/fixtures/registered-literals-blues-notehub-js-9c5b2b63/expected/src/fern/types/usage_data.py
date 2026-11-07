

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsageData(UniversalBaseModel):
    billable_bytes_total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total billable bytes (only for packet-based protocols)
    """

    downlink_bytes: typing.Optional[int] = None
    downlink_bytes_billable: typing.Optional[int] = pydantic.Field(default=None)
    """
    Billable downlink bytes (only for packet-based protocols)
    """

    downlink_packets: typing.Optional[int] = pydantic.Field(default=None)
    """
    Downlink packets (only for packet-based protocols)
    """

    period: dt.datetime
    total_bytes: int
    uplink_bytes: typing.Optional[int] = None
    uplink_bytes_billable: typing.Optional[int] = pydantic.Field(default=None)
    """
    Billable uplink bytes (only for packet-based protocols)
    """

    uplink_packets: typing.Optional[int] = pydantic.Field(default=None)
    """
    Uplink packets (only for packet-based protocols)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
