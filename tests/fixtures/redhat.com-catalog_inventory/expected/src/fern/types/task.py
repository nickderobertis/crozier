

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id
from .task_state import TaskState
from .task_status import TaskStatus
from .uuid_ import Uuid


class Task(UniversalBaseModel):
    archived_at: typing.Optional[dt.datetime] = None
    child_task_id: typing.Optional[str] = None
    completed_at: typing.Optional[dt.datetime] = None
    controller_message_id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    id: typing.Optional[Uuid] = None
    input: typing.Optional[typing.Dict[str, typing.Any]] = None
    message: typing.Optional[str] = None
    name: typing.Optional[str] = None
    output: typing.Optional[typing.Dict[str, typing.Any]] = None
    owner: typing.Optional[str] = None
    source_id: typing.Optional[Id] = None
    state: typing.Optional[TaskState] = None
    status: typing.Optional[TaskStatus] = None
    target_source_ref: typing.Optional[str] = None
    target_type: typing.Optional[str] = None
    type: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
