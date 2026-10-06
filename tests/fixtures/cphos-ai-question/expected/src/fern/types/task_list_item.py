

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskListItem(UniversalBaseModel):
    """
    任务列表项（精简）。
    """

    task_id: str
    user_id: str
    status: str
    mode: typing.Optional[str] = None
    topic: typing.Optional[str] = None
    total_score: typing.Optional[int] = None
    created_at: typing.Optional[str] = None
    finished_at: typing.Optional[str] = None
    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
