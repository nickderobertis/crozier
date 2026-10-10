

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Target_Star(UniversalBaseModel):
    target_class: typing_extensions.Annotated[
        typing.Literal["star"], FieldMetadata(alias="$class"), pydantic.Field(alias="$class")
    ] = "star"
    magnitude: float
    catalog_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Target_Galaxy(UniversalBaseModel):
    target_class: typing_extensions.Annotated[
        typing.Literal["galaxy"], FieldMetadata(alias="$class"), pydantic.Field(alias="$class")
    ] = "galaxy"
    redshift: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Target = typing_extensions.Annotated[
    typing.Union[Target_Star, Target_Galaxy], pydantic.Field(discriminator="target_class")
]
