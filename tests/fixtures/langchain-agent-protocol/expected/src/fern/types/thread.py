

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message import Message
from .thread_status import ThreadStatus


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

    metadata: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The thread metadata.
    """

    status: ThreadStatus = pydantic.Field()
    """
    The status of the thread.
    """

    values: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The current state of the thread.
    """

    messages: typing.Optional[typing.List[Message]] = pydantic.Field(default=None)
    """
    The current Messages of the thread. If messages are contained in Thread.values, implementations should remove them from values when returning messages. When this key isn't present it means the thread/agent doesn't support messages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
