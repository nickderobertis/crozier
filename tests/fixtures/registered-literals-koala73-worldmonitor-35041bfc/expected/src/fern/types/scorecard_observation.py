

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScorecardObservation(UniversalBaseModel):
    name: str
    value: float
    year: int
    unit: str
    source: str
    indicator_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="indicatorCode"), pydantic.Field(alias="indicatorCode")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
