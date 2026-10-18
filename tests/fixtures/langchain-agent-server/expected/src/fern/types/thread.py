

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_status import ThreadStatus
from .thread_ttl import ThreadTtl


class Thread(UniversalBaseModel):
    thread_id: str = pydantic.Field()
    """
    The ID of the thread.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The time the thread was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The last time the thread was updated.
    """

    state_updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time the thread state was updated.
    """

    metadata: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The thread metadata.
    """

    config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The thread config.
    """

    status: ThreadStatus = pydantic.Field()
    """
    The status of the thread.
    """

    values: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The current state of the thread.
    """

    interrupts: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The current interrupts of the thread.
    """

    ttl: typing.Optional[ThreadTtl] = pydantic.Field(default=None)
    """
    TTL information if set for this thread. Only present when ?include=ttl is passed.
    """

    extracted: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Extracted values from thread JSONB columns, populated when extract is specified in search request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
