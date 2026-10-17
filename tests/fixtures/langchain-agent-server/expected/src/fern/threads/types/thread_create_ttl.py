

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_create_ttl_strategy import ThreadCreateTtlStrategy


class ThreadCreateTtl(UniversalBaseModel):
    """
    The time-to-live for the thread.
    """

    strategy: typing.Optional[ThreadCreateTtlStrategy] = pydantic.Field(default=None)
    """
    The TTL strategy. 'delete' removes the entire thread. 'keep_latest' prunes old checkpoints but keeps the thread and its latest state.
    """

    ttl: typing.Optional[float] = pydantic.Field(default=None)
    """
    The time-to-live in minutes from now until thread should be swept.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
