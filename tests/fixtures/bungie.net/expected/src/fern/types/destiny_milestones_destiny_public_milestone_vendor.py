

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyMilestonesDestinyPublicMilestoneVendor(UniversalBaseModel):
    preview_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="previewItemHash"),
        pydantic.Field(
            alias="previewItemHash",
            description="If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST.",
        ),
    ] = None
    """
    If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST.
    """

    vendor_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="vendorHash"),
        pydantic.Field(
            alias="vendorHash",
            description="The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about.",
        ),
    ] = None
    """
    The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
