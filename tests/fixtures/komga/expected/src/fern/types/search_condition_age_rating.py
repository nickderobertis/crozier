

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_operator_numeric_nullable_integer import SearchOperatorNumericNullableInteger


class SearchConditionAgeRating(UniversalBaseModel):
    age_rating: typing_extensions.Annotated[
        SearchOperatorNumericNullableInteger, FieldMetadata(alias="ageRating"), pydantic.Field(alias="ageRating")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
