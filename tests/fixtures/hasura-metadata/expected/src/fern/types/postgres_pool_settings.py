

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostgresPoolSettings(UniversalBaseModel):
    """
    https://hasura.io/docs/latest/graphql/core/api-reference/syntax-defs.html#pgpoolsettings
    """

    connection_lifetime: typing.Optional[float] = pydantic.Field(default=None)
    """
    Time from connection creation after which the connection should be destroyed and a new one created. A value of 0 indicates we should never destroy an active connection. If 0 is passed, memory from large query results may not be reclaimed. (default: 600 sec)
    """

    idle_timeout: typing.Optional[float] = pydantic.Field(default=None)
    """
    The idle timeout (in seconds) per connection (default: 180)
    """

    max_connections: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum number of connections to be kept in the pool (default: 50)
    """

    pool_timeout: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum time to wait while acquiring a Postgres connection from the pool, in seconds (default: forever)
    """

    retries: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of retries to perform (default: 1)
    """

    total_max_connections: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total maximum number of connections across all instances (cloud only, default: null)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
