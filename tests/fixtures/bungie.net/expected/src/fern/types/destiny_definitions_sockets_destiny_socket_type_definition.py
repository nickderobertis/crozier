

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_sockets_destiny_insert_plug_action_definition import (
    DestinyDefinitionsSocketsDestinyInsertPlugActionDefinition,
)
from .destiny_definitions_sockets_destiny_plug_whitelist_entry_definition import (
    DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition,
)
from .destiny_definitions_sockets_destiny_socket_type_scalar_material_requirement_entry import (
    DestinyDefinitionsSocketsDestinySocketTypeScalarMaterialRequirementEntry,
)


class DestinyDefinitionsSocketsDestinySocketTypeDefinition(UniversalBaseModel):
    """
    All Sockets have a "Type": a set of common properties that determine when the socket allows Plugs to be inserted, what Categories of Plugs can be inserted, and whether the socket is even visible at all given the current game/character/account state.
    See DestinyInventoryItemDefinition for more information about Socketed items and Plugs.
    """

    always_randomize_sockets: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="alwaysRandomizeSockets")
    ] = None
    avoid_duplicates_on_initialization: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="avoidDuplicatesOnInitialization")
    ] = None
    currency_scalars: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsSocketsDestinySocketTypeScalarMaterialRequirementEntry]],
        FieldMetadata(alias="currencyScalars"),
    ] = None
    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = pydantic.Field(default=None)
    """
    There are fields for this display data, but they appear to be unpopulated as of now. I am not sure where in the UI these would show if they even were populated, but I will continue to return this data in case it becomes useful.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    hide_duplicate_reusable_plugs: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hideDuplicateReusablePlugs")
    ] = None
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    insert_action: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsSocketsDestinyInsertPlugActionDefinition], FieldMetadata(alias="insertAction")
    ] = pydantic.Field(default=None)
    """
    Defines what happens when a plug is inserted into sockets of this type.
    """

    is_preview_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isPreviewEnabled")] = (
        None
    )
    overrides_ui_appearance: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="overridesUiAppearance")
    ] = pydantic.Field(default=None)
    """
    This property indicates if the socket type determines whether Emblem icons and nameplates should be overridden by the inserted plug item's icon and nameplate.
    """

    plug_whitelist: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition]],
        FieldMetadata(alias="plugWhitelist"),
    ] = pydantic.Field(default=None)
    """
    A list of Plug "Categories" that are allowed to be plugged into sockets of this type.
    These should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.
    If the plug's category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    socket_category_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="socketCategoryHash")
    ] = None
    visibility: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sometimes a socket isn't visible. These are some of the conditions under which sockets of this type are not visible. Unfortunately, the truth of visibility is much, much more complex. Best to rely on the live data for whether the socket is visible and enabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
