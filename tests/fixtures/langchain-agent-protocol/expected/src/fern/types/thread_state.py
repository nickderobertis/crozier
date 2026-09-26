

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message import Message
from .thread_checkpoint import ThreadCheckpoint


class ThreadState(UniversalBaseModel):
    checkpoint: ThreadCheckpoint = pydantic.Field()
    """
    The identifier for this checkpoint.
    """

    values: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The current state of the thread.
    """

    messages: typing.Optional[typing.List[Message]] = pydantic.Field(default=None)
    """
    The current messages of the thread. This key isn't present for agents that don't support messages.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The checkpoint metadata.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
