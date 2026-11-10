

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .get_scores_response_data_numeric import GetScoresResponseDataNumeric
from .get_scores_response_data_zero_data_type import GetScoresResponseDataZeroDataType


class GetScoresResponseDataZero(GetScoresResponseDataNumeric):
    data_type: typing_extensions.Annotated[
        GetScoresResponseDataZeroDataType, FieldMetadata(alias="dataType"), pydantic.Field(alias="dataType")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
