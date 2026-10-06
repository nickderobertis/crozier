

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .elevation import Elevation


class Stake(UniversalBaseModel):
    melt: float
    drift: typing.Optional[float] = None
    whole_metres: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="wholeMetres"), pydantic.Field(alias="wholeMetres")
    ] = None
    firn: typing.Optional[typing.Any] = None
    density: typing.Optional[typing.Any] = None
    segment: typing.Optional[typing.Any] = None
    epoch: typing.Optional[typing.Any] = None
    buried: typing.Optional[typing.Any] = None
    mass: typing.Optional[typing.Any] = None
    elevation: typing.Optional[Elevation] = None
    layers: typing.Optional[typing.List[float]] = None
    bands: typing.Optional[typing.Dict[str, float]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
