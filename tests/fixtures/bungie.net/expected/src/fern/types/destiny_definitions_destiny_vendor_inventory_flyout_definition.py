

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_vendor_inventory_flyout_bucket_definition import (
    DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition,
)


class DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition(UniversalBaseModel):
    """
    The definition for an "inventory flyout": a UI screen where we show you part of an otherwise hidden vendor inventory: like the Vault inventory buckets.
    """

    buckets: typing.Optional[typing.List[DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition]] = (
        pydantic.Field(default=None)
    )
    """
    A list of inventory buckets and other metadata to show on the screen.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties", description="The title and other common properties of the flyout."),
    ] = None
    """
    The title and other common properties of the flyout.
    """

    equipment_slot_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="equipmentSlotHash"),
        pydantic.Field(
            alias="equipmentSlotHash",
            description="If this flyout is meant to show you the contents of the player's equipment slot, this is the slot to show.",
        ),
    ] = None
    """
    If this flyout is meant to show you the contents of the player's equipment slot, this is the slot to show.
    """

    flyout_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="flyoutId"),
        pydantic.Field(
            alias="flyoutId", description="An identifier for the flyout, in case anything else needs to refer to them."
        ),
    ] = None
    """
    An identifier for the flyout, in case anything else needs to refer to them.
    """

    locked_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lockedDescription"),
        pydantic.Field(alias="lockedDescription", description="If the flyout is locked, this is the reason why."),
    ] = None
    """
    If the flyout is locked, this is the reason why.
    """

    suppress_newness: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="suppressNewness"),
        pydantic.Field(
            alias="suppressNewness",
            description='If this is true, don\'t show any of the glistening "this is a new item" UI elements, like we show on the inventory items themselves in in-game UI.',
        ),
    ] = None
    """
    If this is true, don't show any of the glistening "this is a new item" UI elements, like we show on the inventory items themselves in in-game UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
