

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Shipment_Road(UniversalBaseModel):
    mode: typing.Literal["road"] = "road"
    plate: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Shipment_Rail(UniversalBaseModel):
    mode: typing.Literal["rail"] = "rail"
    wagons: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Shipment_Sea(UniversalBaseModel):
    mode: typing.Literal["sea"] = "sea"
    hull: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Shipment = typing_extensions.Annotated[
    typing.Union[Shipment_Road, Shipment_Rail, Shipment_Sea], pydantic.Field(discriminator="mode")
]
