

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinationRedisConfig(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Redis connection URL (redis://host:port)
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    Redis host (default: localhost)
    """

    port: typing.Optional[float] = pydantic.Field(default=None)
    """
    Redis port (default: 6379)
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Redis password
    """

    db: typing.Optional[float] = pydantic.Field(default=None)
    """
    Redis database number (default: 0)
    """

    tls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable TLS
    """

    key_prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prefix for all Redis keys (default: empty)
    """

    batch_size: typing.Optional[float] = pydantic.Field(default=None)
    """
    Records to buffer before flushing via pipeline
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
