

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class SearchConditionAllOfBook(UniversalBaseModel):
    all_of: typing_extensions.Annotated[
        typing.List["SearchConditionBook"], FieldMetadata(alias="allOf"), pydantic.Field(alias="allOf")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .search_condition_any_of_book import SearchConditionAnyOfBook
from .search_condition_book import SearchConditionBook

update_forward_refs(
    SearchConditionAllOfBook, SearchConditionAnyOfBook=SearchConditionAnyOfBook, SearchConditionBook=SearchConditionBook
)
