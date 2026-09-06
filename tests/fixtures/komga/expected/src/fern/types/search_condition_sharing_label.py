

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_operator_equality_nullable_string import SearchOperatorEqualityNullableString


class SearchConditionSharingLabel(UniversalBaseModel):
    sharing_label: typing_extensions.Annotated[
        SearchOperatorEqualityNullableString, FieldMetadata(alias="sharingLabel"), pydantic.Field(alias="sharingLabel")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
