

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Assignment_Fungible(UniversalBaseModel):
    type: typing.Literal["Fungible"] = "Fungible"
    value: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Assignment_NonFungible(UniversalBaseModel):
    type: typing.Literal["NonFungible"] = "NonFungible"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Assignment_InflationRight(UniversalBaseModel):
    type: typing.Literal["InflationRight"] = "InflationRight"
    value: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Assignment_Any(UniversalBaseModel):
    type: typing.Literal["Any"] = "Any"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Assignment = typing_extensions.Annotated[
    typing.Union[Assignment_Fungible, Assignment_NonFungible, Assignment_InflationRight, Assignment_Any],
    pydantic.Field(discriminator="type"),
]
