

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .checkpoint_config import CheckpointConfig
from .interrupt import Interrupt
from .thread_state_values import ThreadStateValues


class ThreadState(UniversalBaseModel):
    values: ThreadStateValues
    next: typing.List[str]
    tasks: typing.Optional[typing.List["ThreadStateTasksItem"]] = None
    checkpoint: CheckpointConfig
    metadata: typing.Dict[str, typing.Any]
    created_at: str
    parent_checkpoint: typing.Optional[typing.Dict[str, typing.Any]] = None
    interrupts: typing.Optional[typing.List[Interrupt]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .thread_state_tasks_item import ThreadStateTasksItem

update_forward_refs(ThreadState, ThreadStateTasksItem=ThreadStateTasksItem)
