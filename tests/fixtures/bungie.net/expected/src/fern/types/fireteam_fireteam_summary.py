

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FireteamFireteamSummary(UniversalBaseModel):
    activity_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activityType"), pydantic.Field(alias="activityType")
    ] = None
    alternate_slot_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="alternateSlotCount"), pydantic.Field(alias="alternateSlotCount")
    ] = None
    available_alternate_slot_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="availableAlternateSlotCount"),
        pydantic.Field(alias="availableAlternateSlotCount"),
    ] = None
    available_player_slot_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="availablePlayerSlotCount"),
        pydantic.Field(alias="availablePlayerSlotCount"),
    ] = None
    date_created: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dateCreated"), pydantic.Field(alias="dateCreated")
    ] = None
    date_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dateModified"), pydantic.Field(alias="dateModified")
    ] = None
    date_player_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="datePlayerModified"),
        pydantic.Field(alias="datePlayerModified"),
    ] = None
    fireteam_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="fireteamId"), pydantic.Field(alias="fireteamId")
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    is_immediate: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isImmediate"), pydantic.Field(alias="isImmediate")
    ] = None
    is_public: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPublic"), pydantic.Field(alias="isPublic")
    ] = None
    is_valid: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isValid"), pydantic.Field(alias="isValid")
    ] = None
    locale: typing.Optional[str] = None
    owner_current_guardian_rank_snapshot: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ownerCurrentGuardianRankSnapshot"),
        pydantic.Field(alias="ownerCurrentGuardianRankSnapshot"),
    ] = None
    owner_highest_lifetime_guardian_rank_snapshot: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ownerHighestLifetimeGuardianRankSnapshot"),
        pydantic.Field(alias="ownerHighestLifetimeGuardianRankSnapshot"),
    ] = None
    owner_membership_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ownerMembershipId"), pydantic.Field(alias="ownerMembershipId")
    ] = None
    owner_total_commendation_score_snapshot: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ownerTotalCommendationScoreSnapshot"),
        pydantic.Field(alias="ownerTotalCommendationScoreSnapshot"),
    ] = None
    platform: typing.Optional[int] = None
    player_slot_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="playerSlotCount"), pydantic.Field(alias="playerSlotCount")
    ] = None
    scheduled_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="scheduledTime"), pydantic.Field(alias="scheduledTime")
    ] = None
    title: typing.Optional[str] = None
    title_before_moderation: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="titleBeforeModeration"),
        pydantic.Field(alias="titleBeforeModeration"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
