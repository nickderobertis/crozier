

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_operator_equality_media_profile import SearchOperatorEqualityMediaProfile


class SearchConditionMediaProfile(UniversalBaseModel):
    media_profile: typing_extensions.Annotated[
        SearchOperatorEqualityMediaProfile, FieldMetadata(alias="mediaProfile"), pydantic.Field(alias="mediaProfile")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
