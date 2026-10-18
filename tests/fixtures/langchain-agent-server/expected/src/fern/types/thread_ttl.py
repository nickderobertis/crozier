

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_ttl_strategy import ThreadTtlStrategy


class ThreadTtl(UniversalBaseModel):
    """
    TTL information if set for this thread. Only present when ?include=ttl is passed.
    """

    strategy: typing.Optional[ThreadTtlStrategy] = pydantic.Field(default=None)
    """
    The TTL strategy.
    """

    ttl_minutes: typing.Optional[float] = pydantic.Field(default=None)
    """
    The TTL in minutes.
    """

    expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the thread will expire.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
