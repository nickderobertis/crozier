

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Reading_Star(UniversalBaseModel):
    """
    One thing seen through the eyepiece.
    """

    kind: typing.Literal["STAR"] = "STAR"
    magnitude: typing.Optional[float] = None
    constellation: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reading_Comet(UniversalBaseModel):
    """
    One thing seen through the eyepiece.
    """

    kind: typing.Literal["COMET"] = "COMET"
    tail_length: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="tailLength"), pydantic.Field(alias="tailLength")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reading_Meteor(UniversalBaseModel):
    value: typing.Any
    kind: typing.Literal["METEOR"] = "METEOR"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


Reading = typing_extensions.Annotated[
    typing.Union[Reading_Star, Reading_Comet, Reading_Meteor], pydantic.Field(discriminator="kind")
]
