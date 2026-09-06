

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DefenderEntry(UniversalBaseModel):
    id: typing.Optional[str] = None
    ip: typing.Optional[str] = None
    score: typing.Optional[int] = pydantic.Field(default=None)
    """
    the score increases whenever a violation is detected, such as an attempt to log in using an incorrect password or invalid username. If the score exceeds the configured threshold, the IP is banned. Omitted for banned IPs
    """

    ban_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    date time until the IP is banned. For already banned hosts, the ban time is increased each time a new violation is detected. Omitted if the IP is not banned
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
