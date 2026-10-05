

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ObservatoryInstrumentsItem_Imaging(UniversalBaseModel):
    stage: typing.Literal["imaging"] = "imaging"
    pixels: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ObservatoryInstrumentsItem_Spectroscopy(UniversalBaseModel):
    stage: typing.Literal["spectroscopy"] = "spectroscopy"
    resolution: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ObservatoryInstrumentsItem = typing_extensions.Annotated[
    typing.Union[ObservatoryInstrumentsItem_Imaging, ObservatoryInstrumentsItem_Spectroscopy],
    pydantic.Field(discriminator="stage"),
]
