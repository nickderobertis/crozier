

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_result import ApiResult
from .search_header import SearchHeader


class ResearchProductsSearchResponseV2(UniversalBaseModel):
    header: typing.Optional[SearchHeader] = None
    results: typing.Optional[typing.List[ApiResult]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
