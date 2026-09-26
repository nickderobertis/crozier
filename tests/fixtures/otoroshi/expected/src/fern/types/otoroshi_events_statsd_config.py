

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OtoroshiEventsStatsdConfig(UniversalBaseModel):
    """
    Settings for connection to a statsd agent
    """

    datadog: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Datadog agent
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    The host of the StatsD agent
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    The port of the StatsD agent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
