

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Base(UniversalBaseModel):
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Pet_Cat(Base):
    pet_type: typing_extensions.Annotated[
        typing.Literal["cat"], FieldMetadata(alias="petType"), pydantic.Field(alias="petType")
    ] = "cat"
    indoor: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Pet_Dog(Base):
    pet_type: typing_extensions.Annotated[
        typing.Literal["dog"], FieldMetadata(alias="petType"), pydantic.Field(alias="petType")
    ] = "dog"
    breed: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Pet = typing_extensions.Annotated[typing.Union[Pet_Cat, Pet_Dog], pydantic.Field(discriminator="pet_type")]
