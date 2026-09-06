

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_operator_numeric_t_float import SearchOperatorNumericTFloat


class SearchConditionNumberSort(UniversalBaseModel):
    number_sort: typing_extensions.Annotated[
        SearchOperatorNumericTFloat, FieldMetadata(alias="numberSort"), pydantic.Field(alias="numberSort")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
