

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserDetail(UniversalBaseModel):
    """
    用户详情（含 token 数与任务数统计）。
    """

    user_id: str
    label: typing.Optional[str] = None
    created_at: str
    token_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    该用户未吊销的 token 数量。
    """

    task_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    该用户的任务总数。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
