

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .search_result_of_trending_entry import SearchResultOfTrendingEntry


class TrendingTrendingCategory(UniversalBaseModel):
    category_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="categoryId"), pydantic.Field(alias="categoryId")
    ] = None
    category_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="categoryName"), pydantic.Field(alias="categoryName")
    ] = None
    entries: typing.Optional[SearchResultOfTrendingEntry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(TrendingTrendingCategory)
