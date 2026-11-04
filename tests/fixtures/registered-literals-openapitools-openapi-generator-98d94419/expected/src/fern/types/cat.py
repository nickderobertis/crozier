

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cat_hunting_skill import CatHuntingSkill
from .cat_pet_type import CatPetType


class Cat(UniversalBaseModel):
    """
    A pet cat
    """

    pet_type: typing_extensions.Annotated[
        typing.Optional[CatPetType], FieldMetadata(alias="petType"), pydantic.Field(alias="petType")
    ] = None
    hunting_skill: typing_extensions.Annotated[
        CatHuntingSkill,
        FieldMetadata(alias="huntingSkill"),
        pydantic.Field(alias="huntingSkill", description="The measured skill for hunting"),
    ]
    """
    The measured skill for hunting
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
