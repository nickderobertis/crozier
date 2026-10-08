

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectV1ConnectorOffsetsMetadata(UniversalBaseModel):
    """
    Metadata of the connector offset.
    """

    observed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the offsets were observed. The time is in UTC, ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
