

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RawProfile(UniversalBaseModel):
    container_hostname: typing.Optional[str] = None
    container_id: typing.Optional[str] = None
    container_qos: typing.Optional[str] = None
    container_type: typing.Optional[str] = None
    hostname: str
    profile: typing.Any
    profile_type: str
    region: str
    started_timestamp: dt.datetime = pydantic.Field()
    """
    UTC timestamp emitted with nine fractional digits.
    """

    uploaded_timestamp: dt.datetime = pydantic.Field()
    """
    UTC timestamp emitted with nine fractional digits.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
