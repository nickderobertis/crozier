

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_operator_equality_status import SearchOperatorEqualityStatus


class SearchConditionSeriesStatus(UniversalBaseModel):
    series_status: typing_extensions.Annotated[
        SearchOperatorEqualityStatus, FieldMetadata(alias="seriesStatus"), pydantic.Field(alias="seriesStatus")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
