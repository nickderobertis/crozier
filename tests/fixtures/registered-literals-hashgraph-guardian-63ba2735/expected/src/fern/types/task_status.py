

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_status_statuses_item import TaskStatusStatusesItem


class TaskStatus(UniversalBaseModel):
    date: typing.Optional[str] = None
    name: typing.Optional[str] = None
    statuses: typing.Optional[typing.List[TaskStatusStatusesItem]] = None
    result: typing.Optional[typing.Dict[str, typing.Any]] = None
    error: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
