

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Base(UniversalBaseModel):
    layers: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RecoatPotRequestCoat_Matte(Base):
    """
    The fresh coat to apply.
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


class RecoatPotRequestCoat_Gloss(Base):
    """
    The fresh coat to apply.
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


RecoatPotRequestCoat = typing_extensions.Annotated[
    typing.Union[RecoatPotRequestCoat_Matte, RecoatPotRequestCoat_Gloss], pydantic.Field(discriminator="finish")
]
