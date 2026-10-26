

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Base(UniversalBaseModel):
    layers: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PotOuterCoat_Matte(Base):
    """
    The coat on the pot's outer wall.
    """

    finish: typing.Literal["matte"] = "matte"
    tooth: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PotOuterCoat_Gloss(Base):
    """
    The coat on the pot's outer wall.
    """

    finish: typing.Literal["gloss"] = "gloss"
    sheen: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PotOuterCoat = typing_extensions.Annotated[
    typing.Union[PotOuterCoat_Matte, PotOuterCoat_Gloss], pydantic.Field(discriminator="finish")
]
