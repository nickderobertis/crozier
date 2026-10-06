

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .progress_event import ProgressEvent


class TaskProgress(UniversalBaseModel):
    """
    任务的节点级进度（阶段事件时间线）。
    """

    task_id: str
    status: str = pydantic.Field()
    """
    任务生命周期状态。
    """

    phase: typing.Optional[str] = pydantic.Field(default=None)
    """
    当前 / 最近所处的阶段名。
    """

    events: typing.Optional[typing.List[ProgressEvent]] = pydantic.Field(default=None)
    """
    按序排列的阶段事件时间线。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
