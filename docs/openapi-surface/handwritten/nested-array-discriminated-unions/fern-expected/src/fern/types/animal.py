

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Animal_Bird(UniversalBaseModel):
    kind: typing.Literal["bird"] = "bird"
    wingspan: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Animal_Fish(UniversalBaseModel):
    kind: typing.Literal["fish"] = "fish"
    fins: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Animal = typing_extensions.Annotated[typing.Union[Animal_Bird, Animal_Fish], pydantic.Field(discriminator="kind")]
