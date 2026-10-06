

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_status_status import TaskStatusStatus


class TaskStatus(UniversalBaseModel):
    """
    任务状态与摘要。
    """

    task_id: str
    user_id: str
    status: TaskStatusStatus = pydantic.Field()
    """
    任务生命周期状态。
    """

    phase: typing.Optional[str] = pydantic.Field(default=None)
    """
    当前 / 最近所处的工作流阶段名（如 REVIEWING / FORMATTING）。
    """

    mode: typing.Optional[str] = None
    topic: typing.Optional[str] = None
    total_score: typing.Optional[int] = None
    created_at: typing.Optional[str] = None
    finished_at: typing.Optional[str] = None
    error: typing.Optional[str] = None
    summary: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    完成后的摘要：仲裁裁决、重试计数、token 用量、API 费用、产物清单等。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
