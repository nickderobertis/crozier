

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Instrument_Lens(UniversalBaseModel):
    optics_kind: typing_extensions.Annotated[
        typing.Literal["lens"], FieldMetadata(alias="optics"), pydantic.Field(alias="optics")
    ] = "lens"
    aperture_mm: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Instrument_Mirror(UniversalBaseModel):
    optics_kind: typing_extensions.Annotated[
        typing.Literal["mirror"], FieldMetadata(alias="optics"), pydantic.Field(alias="optics")
    ] = "mirror"
    focal_ratio: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Instrument = typing_extensions.Annotated[
    typing.Union[Instrument_Lens, Instrument_Mirror], pydantic.Field(discriminator="optics_kind")
]
