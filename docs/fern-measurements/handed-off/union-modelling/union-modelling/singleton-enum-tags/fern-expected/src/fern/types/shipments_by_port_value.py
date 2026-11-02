

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ShipmentsByPortValue_Road(UniversalBaseModel):
    mode: typing.Literal["road"] = "road"
    plate: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ShipmentsByPortValue_Sea(UniversalBaseModel):
    mode: typing.Literal["sea"] = "sea"
    draft: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ShipmentsByPortValue = typing_extensions.Annotated[
    typing.Union[ShipmentsByPortValue_Road, ShipmentsByPortValue_Sea], pydantic.Field(discriminator="mode")
]
