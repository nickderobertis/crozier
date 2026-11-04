

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dog_pet_type import DogPetType


class Dog(UniversalBaseModel):
    """
    A pet dog
    """

    pet_type: typing_extensions.Annotated[
        typing.Optional[DogPetType], FieldMetadata(alias="petType"), pydantic.Field(alias="petType")
    ] = None
    pack_size: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="packSize"),
        pydantic.Field(alias="packSize", description="the size of the pack the dog is from"),
    ]
    """
    the size of the pack the dog is from
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
