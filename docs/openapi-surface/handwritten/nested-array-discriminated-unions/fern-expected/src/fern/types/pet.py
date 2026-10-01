

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Pet_Cat(UniversalBaseModel):
    kind: typing.Literal["cat"] = "cat"
    lives: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Pet_Dog(UniversalBaseModel):
    kind: typing.Literal["dog"] = "dog"
    breed: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Pet = typing_extensions.Annotated[typing.Union[Pet_Cat, Pet_Dog], pydantic.Field(discriminator="kind")]
