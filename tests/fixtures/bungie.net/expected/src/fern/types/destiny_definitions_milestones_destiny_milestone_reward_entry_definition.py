

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition(UniversalBaseModel):
    """
    The definition of a specific reward, which may be contained in a category of rewards and that has optional information about how it is obtained.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(
            alias="displayProperties",
            description="For us to bother returning this info, we should be able to return some kind of information about why these rewards are grouped together. This is ideally that information. Look at how confident I am that this will always remain true.",
        ),
    ] = None
    """
    For us to bother returning this info, we should be able to return some kind of information about why these rewards are grouped together. This is ideally that information. Look at how confident I am that this will always remain true.
    """

    items: typing.Optional[typing.List[DestinyDestinyItemQuantity]] = pydantic.Field(default=None)
    """
    The items you will get as rewards, and how much of it you'll get.
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    If you want to follow BNet's ordering of these rewards, use this number within a given category to order the rewards. Yeah, I know. I feel dirty too.
    """

    reward_entry_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rewardEntryHash"),
        pydantic.Field(
            alias="rewardEntryHash",
            description="The identifier for this reward entry. Runtime data will refer to reward entries by this hash. Only guaranteed unique within the specific Milestone.",
        ),
    ] = None
    """
    The identifier for this reward entry. Runtime data will refer to reward entries by this hash. Only guaranteed unique within the specific Milestone.
    """

    reward_entry_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rewardEntryIdentifier"),
        pydantic.Field(
            alias="rewardEntryIdentifier",
            description="The string identifier, if you care about it. Only guaranteed unique within the specific Milestone.",
        ),
    ] = None
    """
    The string identifier, if you care about it. Only guaranteed unique within the specific Milestone.
    """

    vendor_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="vendorHash"),
        pydantic.Field(
            alias="vendorHash",
            description="If this reward is redeemed at a Vendor, this is the hash of the Vendor to go to in order to redeem the reward. Use this hash to look up the DestinyVendorDefinition.",
        ),
    ] = None
    """
    If this reward is redeemed at a Vendor, this is the hash of the Vendor to go to in order to redeem the reward. Use this hash to look up the DestinyVendorDefinition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
