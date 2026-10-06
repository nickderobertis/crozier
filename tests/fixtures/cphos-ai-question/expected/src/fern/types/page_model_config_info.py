

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_config_info import ModelConfigInfo


class PageModelConfigInfo(UniversalBaseModel):
    items: typing.Optional[typing.List[ModelConfigInfo]] = pydantic.Field(default=None)
    """
    当前页数据。
    """

    total: int = pydantic.Field()
    """
    满足过滤条件的总条数（用于分页器）。
    """

    limit: int = pydantic.Field()
    """
    本次请求的分页大小。
    """

    offset: int = pydantic.Field()
    """
    本次请求的偏移量。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
