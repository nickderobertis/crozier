

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tart_order import TartOrder


class Pastry_Tart(UniversalBaseModel):
    value: TartOrder
    kind: typing.Literal["tart"] = "tart"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class Pastry_Croissant(UniversalBaseModel):
    kind: typing.Literal["croissant"] = "croissant"
    butter: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Pastry = typing_extensions.Annotated[typing.Union[Pastry_Tart, Pastry_Croissant], pydantic.Field(discriminator="kind")]
