

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_items_destiny_energy_capacity_entry import DestinyDefinitionsItemsDestinyEnergyCapacityEntry
from .destiny_definitions_items_destiny_energy_cost_entry import DestinyDefinitionsItemsDestinyEnergyCostEntry
from .destiny_definitions_items_destiny_parent_item_override import DestinyDefinitionsItemsDestinyParentItemOverride
from .destiny_definitions_items_destiny_plug_rule_definition import DestinyDefinitionsItemsDestinyPlugRuleDefinition


class DestinyDefinitionsItemsDestinyItemPlugDefinition(UniversalBaseModel):
    """
    If an item is a Plug, its DestinyInventoryItemDefinition.plug property will be populated with an instance of one of these bad boys.
    This gives information about when it can be inserted, what the plug's category is (and thus whether it is compatible with a socket... see DestinySocketTypeDefinition for information about Plug Categories and socket compatibility), whether it is enabled and other Plug info.
    """

    alternate_plug_style: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="alternatePlugStyle")
    ] = pydantic.Field(default=None)
    """
    The alternate plug of the plug: only applies when the item is in states that only the server can know about and control, unfortunately. See AlternateUiPlugLabel for the related label info.
    """

    alternate_ui_plug_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="alternateUiPlugLabel")
    ] = pydantic.Field(default=None)
    """
    If the plug meets certain state requirements, it may have an alternative label applied to it. This is the alternative label that will be applied in such a situation.
    """

    enabled_material_requirement_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="enabledMaterialRequirementHash")
    ] = pydantic.Field(default=None)
    """
    It's not enough for the plug to be inserted. It has to be enabled as well. For it to be enabled, it may require materials. This is the hash identifier for the DestinyMaterialRequirementSetDefinition for those requirements, if there is one.
    """

    enabled_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsItemsDestinyPlugRuleDefinition]],
        FieldMetadata(alias="enabledRules"),
    ] = pydantic.Field(default=None)
    """
    The rules around whether the plug, once inserted, is enabled and providing its benefits.
    The live data DestinyItemPlugComponent.enableFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user.
    """

    energy_capacity: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsItemsDestinyEnergyCapacityEntry], FieldMetadata(alias="energyCapacity")
    ] = pydantic.Field(default=None)
    """
    IF not null, this plug provides Energy capacity to the item in which it is socketed. In Armor 2.0 for example, is implemented in a similar way to Masterworks, where visually it's a single area of the UI being clicked on to "Upgrade" to higher energy levels, but it's actually socketing new plugs.
    """

    energy_cost: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsItemsDestinyEnergyCostEntry], FieldMetadata(alias="energyCost")
    ] = pydantic.Field(default=None)
    """
    IF not null, this plug has an energy cost. This contains the details of that cost.
    """

    insertion_material_requirement_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="insertionMaterialRequirementHash")
    ] = pydantic.Field(default=None)
    """
    If inserting this plug requires materials, this is the hash identifier for looking up the DestinyMaterialRequirementSetDefinition for those requirements.
    """

    insertion_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsItemsDestinyPlugRuleDefinition]],
        FieldMetadata(alias="insertionRules"),
    ] = pydantic.Field(default=None)
    """
    The rules around when this plug can be inserted into a socket, aside from the socket's individual restrictions.
    The live data DestinyItemPlugComponent.insertFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user.
    """

    is_dummy_plug: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isDummyPlug")] = (
        pydantic.Field(default=None)
    )
    """
    If TRUE, this plug is used for UI display purposes only, and doesn't have any interesting effects of its own.
    """

    on_action_recreate_self: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="onActionRecreateSelf")
    ] = pydantic.Field(default=None)
    """
    If you successfully socket the item, this will determine whether or not you get "refunded" on the plug.
    """

    parent_item_override: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsItemsDestinyParentItemOverride], FieldMetadata(alias="parentItemOverride")
    ] = pydantic.Field(default=None)
    """
    Do you ever get the feeling that a system has become so overburdened by edge cases that it probably should have become some other system entirely? So do I!
    In totally unrelated news, Plugs can now override properties of their parent items. This is some of the relevant definition data for those overrides.
    If this is populated, it will have the override data to be applied when this plug is applied to an item.
    """

    plug_availability: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="plugAvailability")] = (
        pydantic.Field(default=None)
    )
    """
    Indicates the rules about when this plug can be used. See the PlugAvailabilityMode enumeration for more information!
    """

    plug_category_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="plugCategoryHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash for the plugCategoryIdentifier. You can use this instead if you wish: I put both in the definition for debugging purposes.
    """

    plug_category_identifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="plugCategoryIdentifier")
    ] = pydantic.Field(default=None)
    """
    The string identifier for the plug's category. Use the socket's DestinySocketTypeDefinition.plugWhitelist to determine whether this plug can be inserted into the socket.
    """

    plug_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="plugStyle")] = None
    preview_item_override_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="previewItemOverrideHash")
    ] = pydantic.Field(default=None)
    """
    In the game, if you're inspecting a plug item directly, this will be the item shown with the plug attached. Look up the DestinyInventoryItemDefinition for this hash for the item.
    """

    ui_plug_label: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uiPlugLabel")] = (
        pydantic.Field(default=None)
    )
    """
    Plugs can have arbitrary, UI-defined identifiers that the UI designers use to determine the style applied to plugs. Unfortunately, we have neither a definitive list of these labels nor advance warning of when new labels might be applied or how that relates to how they get rendered. If you want to, you can refer to known labels to change your own styles: but know that new ones can be created arbitrarily, and we have no way of associating the labels with any specific UI style guidance... you'll have to piece that together on your end. Or do what we do, and just show plugs more generically, without specialized styles.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
