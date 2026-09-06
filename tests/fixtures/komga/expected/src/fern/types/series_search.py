

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class SeriesSearch(UniversalBaseModel):
    condition: typing.Optional["SearchConditionSeries"] = None
    full_text_search: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fullTextSearch"), pydantic.Field(alias="fullTextSearch")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .search_condition_all_of_series import SearchConditionAllOfSeries
from .search_condition_any_of_series import SearchConditionAnyOfSeries
from .search_condition_series import SearchConditionSeries

update_forward_refs(
    SeriesSearch,
    SearchConditionAllOfSeries=SearchConditionAllOfSeries,
    SearchConditionAnyOfSeries=SearchConditionAnyOfSeries,
    SearchConditionSeries=SearchConditionSeries,
)
