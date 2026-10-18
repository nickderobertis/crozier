

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RealtimeConfigResponseOutput(UniversalBaseModel):
    private_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to only allow private channels
    """

    connection_pool: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets connection pool size for Realtime Authorization
    """

    postgres_changes_pool: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets connection pool size used to create Postgres Changes subscriptions
    """

    max_concurrent_users: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets maximum number of concurrent users rate limit
    """

    max_events_per_second: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets maximum number of events per second rate per channel limit
    """

    max_bytes_per_second: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets maximum number of bytes per second rate per channel limit
    """

    max_channels_per_client: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets maximum number of channels per client rate limit
    """

    max_joins_per_second: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets maximum number of joins per second rate limit
    """

    max_presence_events_per_second: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets maximum number of presence events per second rate limit
    """

    max_payload_size_in_kb: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sets maximum number of payload size in KB rate limit
    """

    suspend: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Disables the Realtime service for this project when true. Set to false to re-enable it.
    """

    presence_enabled: bool = pydantic.Field()
    """
    Whether to enable presence
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
