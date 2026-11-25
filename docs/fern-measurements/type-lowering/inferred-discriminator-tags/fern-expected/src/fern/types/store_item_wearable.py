

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreItemWearable_TShirt(UniversalBaseModel):
    """
    A shirt or a coat.
    """

    type: typing.Literal["T-Shirt"] = "T-Shirt"
    slot: typing.Optional[str] = None
    sleeves: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StoreItemWearable_Jacket(UniversalBaseModel):
    """
    A shirt or a coat.
    """

    type: typing.Literal["Jacket"] = "Jacket"
    slot: typing.Optional[str] = None
    lining: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StoreItemWearable = typing_extensions.Annotated[
    typing.Union[StoreItemWearable_TShirt, StoreItemWearable_Jacket], pydantic.Field(discriminator="type")
]
