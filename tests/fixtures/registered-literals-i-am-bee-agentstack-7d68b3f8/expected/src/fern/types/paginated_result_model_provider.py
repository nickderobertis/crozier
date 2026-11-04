

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_provider import ModelProvider


class PaginatedResultModelProvider(UniversalBaseModel):
    items: typing.List[ModelProvider]
    total_count: int
    has_more: typing.Optional[bool] = None
    next_page_token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
