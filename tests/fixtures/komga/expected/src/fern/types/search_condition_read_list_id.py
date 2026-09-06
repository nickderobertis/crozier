

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_operator_equality_string import SearchOperatorEqualityString


class SearchConditionReadListId(UniversalBaseModel):
    read_list_id: typing_extensions.Annotated[
        SearchOperatorEqualityString, FieldMetadata(alias="readListId"), pydantic.Field(alias="readListId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
