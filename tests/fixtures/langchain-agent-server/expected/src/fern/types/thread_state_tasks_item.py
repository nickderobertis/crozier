

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .checkpoint_config import CheckpointConfig
from .interrupt import Interrupt


class ThreadStateTasksItem(UniversalBaseModel):
    id: str
    name: str
    error: typing.Optional[str] = None
    interrupts: typing.Optional[typing.List[Interrupt]] = None
    checkpoint: typing.Optional[CheckpointConfig] = None
    state: typing.Optional["ThreadState"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .thread_state import ThreadState

update_forward_refs(ThreadStateTasksItem, ThreadState=ThreadState)
