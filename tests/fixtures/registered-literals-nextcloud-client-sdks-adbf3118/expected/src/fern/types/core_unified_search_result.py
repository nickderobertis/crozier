

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .core_unified_search_result_cursor import CoreUnifiedSearchResultCursor
from .core_unified_search_result_entry import CoreUnifiedSearchResultEntry


class CoreUnifiedSearchResult(UniversalBaseModel):
    name: str
    is_paginated: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isPaginated"), pydantic.Field(alias="isPaginated")
    ]
    entries: typing.List[CoreUnifiedSearchResultEntry]
    cursor: typing.Optional[CoreUnifiedSearchResultCursor] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
