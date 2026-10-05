

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Telescope_Reflector(UniversalBaseModel):
    variety: typing.Literal["reflector"] = "reflector"
    aperture_mm: int
    serial: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Telescope_Refractor(UniversalBaseModel):
    variety: typing.Literal["refractor"] = "refractor"
    focal_mm: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Telescope = typing_extensions.Annotated[
    typing.Union[Telescope_Reflector, Telescope_Refractor], pydantic.Field(discriminator="variety")
]
