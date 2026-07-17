

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsLoadoutsDestinyLoadoutConstantsDefinition(UniversalBaseModel):
    black_icon_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="blackIconImagePath"),
        pydantic.Field(
            alias="blackIconImagePath", description="This is a color-inverted version of the whiteIconImagePath."
        ),
    ] = None
    """
    This is a color-inverted version of the whiteIconImagePath.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
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

    loadout_color_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="loadoutColorHashes"),
        pydantic.Field(
            alias="loadoutColorHashes",
            description="A list of the loadout color hashes in index order, for convenience.",
        ),
    ] = None
    """
    A list of the loadout color hashes in index order, for convenience.
    """

    loadout_count_per_character: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="loadoutCountPerCharacter"),
        pydantic.Field(
            alias="loadoutCountPerCharacter",
            description="The maximum number of loadouts available to each character. The loadouts component API response can return fewer loadouts than this, as more loadouts are unlocked by reaching higher Guardian Ranks.",
        ),
    ] = None
    """
    The maximum number of loadouts available to each character. The loadouts component API response can return fewer loadouts than this, as more loadouts are unlocked by reaching higher Guardian Ranks.
    """

    loadout_icon_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="loadoutIconHashes"),
        pydantic.Field(
            alias="loadoutIconHashes", description="A list of the loadout icon hashes in index order, for convenience."
        ),
    ] = None
    """
    A list of the loadout icon hashes in index order, for convenience.
    """

    loadout_name_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="loadoutNameHashes"),
        pydantic.Field(
            alias="loadoutNameHashes", description="A list of the loadout name hashes in index order, for convenience."
        ),
    ] = None
    """
    A list of the loadout name hashes in index order, for convenience.
    """

    loadout_preview_filter_out_socket_category_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="loadoutPreviewFilterOutSocketCategoryHashes"),
        pydantic.Field(
            alias="loadoutPreviewFilterOutSocketCategoryHashes",
            description="A list of the socket category hashes to be filtered out of loadout item preview displays.",
        ),
    ] = None
    """
    A list of the socket category hashes to be filtered out of loadout item preview displays.
    """

    loadout_preview_filter_out_socket_type_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="loadoutPreviewFilterOutSocketTypeHashes"),
        pydantic.Field(
            alias="loadoutPreviewFilterOutSocketTypeHashes",
            description="A list of the socket type hashes to be filtered out of loadout item preview displays.",
        ),
    ] = None
    """
    A list of the socket type hashes to be filtered out of loadout item preview displays.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    white_icon_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="whiteIconImagePath"),
        pydantic.Field(
            alias="whiteIconImagePath",
            description="This is the same icon as the one in the display properties, offered here as well with a more descriptive name.",
        ),
    ] = None
    """
    This is the same icon as the one in the display properties, offered here as well with a more descriptive name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
