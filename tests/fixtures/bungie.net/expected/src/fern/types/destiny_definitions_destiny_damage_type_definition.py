

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_misc_destiny_color import DestinyMiscDestinyColor


class DestinyDefinitionsDestinyDamageTypeDefinition(UniversalBaseModel):
    """
    All damage types that are possible in the game are defined here, along with localized info and icons as needed.
    """

    color: typing.Optional[DestinyMiscDestinyColor] = pydantic.Field(default=None)
    """
    A color associated with the damage type. The displayProperties icon is tinted with a color close to this.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties", description="The description of the damage type, icon etc..."),
    ] = None
    """
    The description of the damage type, icon etc...
    """

    enum_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="enumValue"),
        pydantic.Field(
            alias="enumValue",
            description="We have an enumeration for damage types for quick reference. This is the current definition's damage type enum value.",
        ),
    ] = None
    """
    We have an enumeration for damage types for quick reference. This is the current definition's damage type enum value.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    show_icon: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="showIcon"),
        pydantic.Field(
            alias="showIcon",
            description="If TRUE, the game shows this damage type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.",
        ),
    ] = None
    """
    If TRUE, the game shows this damage type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.
    """

    transparent_icon_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transparentIconPath"),
        pydantic.Field(
            alias="transparentIconPath", description="A variant of the icon that is transparent and colorless."
        ),
    ] = None
    """
    A variant of the icon that is transparent and colorless.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
