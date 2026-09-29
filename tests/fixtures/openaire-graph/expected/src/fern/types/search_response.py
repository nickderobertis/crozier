

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_header import SearchHeader


class SearchResponse(UniversalBaseModel):
    header: typing.Optional[SearchHeader] = None
    results: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
