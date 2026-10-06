

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskCreated(UniversalBaseModel):
    """
    任务提交后的即时响应。
    """

    task_id: str = pydantic.Field()
    """
    任务标识，用于后续轮询与下载。
    """

    status: str = pydantic.Field()
    """
    任务初始状态。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
