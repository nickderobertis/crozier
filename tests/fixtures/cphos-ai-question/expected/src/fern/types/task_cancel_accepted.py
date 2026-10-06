

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_cancel_accepted_status import TaskCancelAcceptedStatus


class TaskCancelAccepted(UniversalBaseModel):
    """
    取消请求的受理响应。
    """

    task_id: str
    status: TaskCancelAcceptedStatus = pydantic.Field()
    """
    aborting=正在停止（运行中任务，将在阶段边界终止）；aborted=已立即终止（排队中尚未启动的任务）。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
