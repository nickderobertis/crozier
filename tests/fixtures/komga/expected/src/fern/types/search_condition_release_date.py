

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class SearchConditionReleaseDate(UniversalBaseModel):
    release_date: typing_extensions.Annotated[
        "SearchOperatorDate", FieldMetadata(alias="releaseDate"), pydantic.Field(alias="releaseDate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .search_operator_date import SearchOperatorDate
from .search_operator_is_not_null import SearchOperatorIsNotNull
from .search_operator_is_null import SearchOperatorIsNull

update_forward_refs(
    SearchConditionReleaseDate,
    SearchOperatorDate=SearchOperatorDate,
    SearchOperatorIsNotNull=SearchOperatorIsNotNull,
    SearchOperatorIsNull=SearchOperatorIsNull,
)
