

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyClassDefinition(UniversalBaseModel):
    """
    Defines a Character Class in Destiny 2. These are types of characters you can play, like Titan, Warlock, and Hunter.
    """

    class_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="classType"),
        pydantic.Field(
            alias="classType",
            description="In Destiny 1, we added a convenience Enumeration for referring to classes. We've kept it, though mostly for posterity. This is the enum value for this definition's class.",
        ),
    ] = None
    """
    In Destiny 1, we added a convenience Enumeration for referring to classes. We've kept it, though mostly for posterity. This is the enum value for this definition's class.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    gendered_class_names: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="genderedClassNames"),
        pydantic.Field(
            alias="genderedClassNames",
            description="A localized string referring to the singular form of the Class's name when referred to in gendered form. Keyed by the DestinyGender.",
        ),
    ] = None
    """
    A localized string referring to the singular form of the Class's name when referred to in gendered form. Keyed by the DestinyGender.
    """

    gendered_class_names_by_gender_hash: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="genderedClassNamesByGenderHash"),
        pydantic.Field(alias="genderedClassNamesByGenderHash"),
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    mentor_vendor_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="mentorVendorHash"),
        pydantic.Field(
            alias="mentorVendorHash",
            description="Mentors don't really mean anything anymore. Don't expect this to be populated.",
        ),
    ] = None
    """
    Mentors don't really mean anything anymore. Don't expect this to be populated.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
