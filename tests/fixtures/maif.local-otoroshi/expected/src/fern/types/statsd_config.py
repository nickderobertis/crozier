

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StatsdConfig(UniversalBaseModel):
    """
    The configuration for statsd metrics push
    """

    datadog: bool = pydantic.Field()
    """
    Datadog agent
    """

    host: str = pydantic.Field()
    """
    The host of the StatsD agent
    """

    port: int = pydantic.Field()
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
