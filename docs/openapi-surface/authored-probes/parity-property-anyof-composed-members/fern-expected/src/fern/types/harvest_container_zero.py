

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HarvestContainerZero_Crate(UniversalBaseModel):
    kind: typing.Literal["crate"] = "crate"
    weight_kg: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class HarvestContainerZero_Basket(UniversalBaseModel):
    kind: typing.Literal["basket"] = "basket"
    handles: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


HarvestContainerZero = typing_extensions.Annotated[
    typing.Union[HarvestContainerZero_Crate, HarvestContainerZero_Basket], pydantic.Field(discriminator="kind")
]
