

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsageSessionsData(UniversalBaseModel):
    device: typing.Optional[str] = None
    first_sync_sessions: int = pydantic.Field()
    """
    Number of first sync sessions in this period
    """

    fleet: typing.Optional[str] = None
    period: dt.datetime
    sessions: int
    sessions_by_transport: typing.Optional[typing.Dict[str, int]] = pydantic.Field(default=None)
    """
    Count of sessions grouped by transport type prefix (e.g. cell, wifi, ntn, lorawan)
    """

    tls_sessions: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of TLS sessions in this period
    """

    total_bytes: int
    total_devices: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
