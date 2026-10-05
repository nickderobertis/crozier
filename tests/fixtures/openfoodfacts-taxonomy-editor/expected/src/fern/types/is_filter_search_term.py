

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .is_filter_search_term_filter_value import IsFilterSearchTermFilterValue


class IsFilterSearchTerm(UniversalBaseModel):
    filter_value: typing_extensions.Annotated[
        IsFilterSearchTermFilterValue, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
