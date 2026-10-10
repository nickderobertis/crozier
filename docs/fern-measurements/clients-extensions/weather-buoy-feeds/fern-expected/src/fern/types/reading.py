

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Reading(UniversalBaseModel):
    wind_knots: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="windKnots"), pydantic.Field(alias="windKnots")
    ] = None
    wave_metres: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="waveMetres"), pydantic.Field(alias="waveMetres")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
