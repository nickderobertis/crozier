

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_operator_string import SearchOperatorString


class SearchConditionTitleSort(UniversalBaseModel):
    title_sort: typing_extensions.Annotated[
        SearchOperatorString, FieldMetadata(alias="titleSort"), pydantic.Field(alias="titleSort")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
