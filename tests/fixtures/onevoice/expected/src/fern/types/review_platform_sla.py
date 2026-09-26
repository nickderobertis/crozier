

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReviewPlatformSla(UniversalBaseModel):
    platform: str
    median_response_hours: typing_extensions.Annotated[
        float, FieldMetadata(alias="medianResponseHours"), pydantic.Field(alias="medianResponseHours")
    ]
    measured_responses: typing_extensions.Annotated[
        int, FieldMetadata(alias="measuredResponses"), pydantic.Field(alias="measuredResponses")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
