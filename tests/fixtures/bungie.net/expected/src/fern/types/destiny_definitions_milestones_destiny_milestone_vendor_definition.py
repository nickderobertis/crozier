

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsMilestonesDestinyMilestoneVendorDefinition(UniversalBaseModel):
    """
    If the Milestone or a component has vendors whose inventories could/should be displayed that are relevant to it, this will return the vendor in question.
    It also contains information we need to determine whether that vendor is actually relevant at the moment, given the user's current state.
    """

    vendor_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorHash")] = pydantic.Field(
        default=None
    )
    """
    The hash of the vendor whose wares should be shown as associated with the Milestone.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
