

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartImmunizationsSeriesCompletionsRequest(UniversalBaseModel):
    series_name: typing_extensions.Annotated[str, FieldMetadata(alias="SeriesName"), pydantic.Field(alias="SeriesName")]
    is_complete: typing_extensions.Annotated[str, FieldMetadata(alias="IsComplete"), pydantic.Field(alias="IsComplete")]
    comment: typing_extensions.Annotated[str, FieldMetadata(alias="Comment"), pydantic.Field(alias="Comment")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
