

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceUsage(UniversalBaseModel):
    bytes_rcvd: typing.Optional[int] = None
    bytes_rcvd_secondary: typing.Optional[int] = None
    bytes_sent: typing.Optional[int] = None
    bytes_sent_secondary: typing.Optional[int] = None
    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Duration in seconds
    """

    notes_rcvd: typing.Optional[int] = None
    notes_sent: typing.Optional[int] = None
    sessions_tcp: typing.Optional[int] = None
    sessions_tls: typing.Optional[int] = None
    since: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
