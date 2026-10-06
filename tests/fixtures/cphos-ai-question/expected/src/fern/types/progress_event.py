

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .progress_event_status import ProgressEventStatus


class ProgressEvent(UniversalBaseModel):
    """
    单条阶段进度事件。
    """

    seq: int = pydantic.Field()
    """
    任务内单调递增的事件序号。
    """

    phase: str = pydantic.Field()
    """
    阶段名（Phase.name，如 REVIEWING）。
    """

    phase_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    阶段的中文显示标签。
    """

    occurrence_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    同一阶段同一次执行的稳定标识（running/completed 共享），形如 'REVIEWING#2'，供前端无序配对，无需依赖事件顺序。
    """

    round: typing.Optional[int] = pydantic.Field(default=None)
    """
    重试轮次（从 1 起），由状态机总重试计数推导，便于前端按轮分组。
    """

    status: ProgressEventStatus = pydantic.Field()
    """
    running=进入该阶段；completed=该阶段产出就绪。
    """

    output: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    completed 事件携带的结构化阶段产出快照（已按阶段类型格式化，非模型原始输出）。
    """

    created_at: str = pydantic.Field()
    """
    事件时间戳。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
