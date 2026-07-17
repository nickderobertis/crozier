

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_public_milestone_challenge_activity import (
    DestinyMilestonesDestinyPublicMilestoneChallengeActivity,
)
from .destiny_milestones_destiny_public_milestone_quest import DestinyMilestonesDestinyPublicMilestoneQuest
from .destiny_milestones_destiny_public_milestone_vendor import DestinyMilestonesDestinyPublicMilestoneVendor


class DestinyMilestonesDestinyPublicMilestone(UniversalBaseModel):
    """
    Information about milestones, presented in a character state-agnostic manner. Combine this data with DestinyMilestoneDefinition to get a full picture of the milestone, which is basically a checklist of things to do in the game. Think of this as GetPublicAdvisors 3.0, for those who used the Destiny 1 API.
    """

    activities: typing.Optional[typing.List[DestinyMilestonesDestinyPublicMilestoneChallengeActivity]] = None
    available_quests: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyMilestonesDestinyPublicMilestoneQuest]],
        FieldMetadata(alias="availableQuests"),
        pydantic.Field(
            alias="availableQuests",
            description="A milestone not need have even a single quest, but if there are active quests they will be returned here.",
        ),
    ] = None
    """
    A milestone not need have even a single quest, but if there are active quests they will be returned here.
    """

    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="endDate"),
        pydantic.Field(
            alias="endDate", description="If known, this is the date when the Milestone will expire/recycle/end."
        ),
    ] = None
    """
    If known, this is the date when the Milestone will expire/recycle/end.
    """

    milestone_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="milestoneHash"),
        pydantic.Field(
            alias="milestoneHash",
            description="The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone.",
        ),
    ] = None
    """
    The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone.
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information.
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startDate"),
        pydantic.Field(
            alias="startDate", description="If known, this is the date when the Milestone started/became active."
        ),
    ] = None
    """
    If known, this is the date when the Milestone started/became active.
    """

    vendor_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="vendorHashes"),
        pydantic.Field(
            alias="vendorHashes",
            description='Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant.\r\nDeprecated, already, for the sake of the new "vendors" property that has more data. What was I thinking.',
        ),
    ] = None
    """
    Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant.
    Deprecated, already, for the sake of the new "vendors" property that has more data. What was I thinking.
    """

    vendors: typing.Optional[typing.List[DestinyMilestonesDestinyPublicMilestoneVendor]] = pydantic.Field(default=None)
    """
    This is why we can't have nice things. This is the ordered list of vendors to be shown that relate to this milestone, potentially along with other interesting data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
