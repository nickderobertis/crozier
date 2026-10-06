

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AdminStats(UniversalBaseModel):
    """
    管理端概览统计。
    """

    task_total: int = pydantic.Field()
    """
    任务总数。
    """

    task_status_counts: typing.Optional[typing.Dict[str, int]] = pydantic.Field(default=None)
    """
    按生命周期状态分组的任务计数。
    """

    user_count: int = pydantic.Field()
    """
    用户总数。
    """

    active_token_count: int = pydantic.Field()
    """
    未吊销的 token 数量。
    """

    token_usage_total: int = pydantic.Field()
    """
    历史任务累计 total_tokens 用量。
    """

    api_cost_usd_total: float = pydantic.Field()
    """
    历史任务累计 API 费用（USD）。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
