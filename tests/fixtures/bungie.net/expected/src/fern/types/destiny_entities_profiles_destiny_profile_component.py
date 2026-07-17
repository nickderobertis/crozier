

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_user_info_card import UserUserInfoCard


class DestinyEntitiesProfilesDestinyProfileComponent(UniversalBaseModel):
    """
    The most essential summary information about a Profile (in Destiny 1, we called these "Accounts").
    """

    active_event_card_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activeEventCardHash"),
        pydantic.Field(
            alias="activeEventCardHash",
            description="If populated, this is a reference to the event card that is currently active.",
        ),
    ] = None
    """
    If populated, this is a reference to the event card that is currently active.
    """

    character_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="characterIds"),
        pydantic.Field(
            alias="characterIds", description="A list of the character IDs, for further querying on your part."
        ),
    ] = None
    """
    A list of the character IDs, for further querying on your part.
    """

    current_guardian_rank: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentGuardianRank"),
        pydantic.Field(
            alias="currentGuardianRank", description="The 'current' Guardian Rank value, which starts at rank 1."
        ),
    ] = None
    """
    The 'current' Guardian Rank value, which starts at rank 1.
    """

    current_season_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentSeasonHash"),
        pydantic.Field(
            alias="currentSeasonHash",
            description="If populated, this is a reference to the season that is currently active.",
        ),
    ] = None
    """
    If populated, this is a reference to the season that is currently active.
    """

    current_season_reward_power_cap: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentSeasonRewardPowerCap"),
        pydantic.Field(
            alias="currentSeasonRewardPowerCap",
            description="If populated, this is the reward power cap for the current season.",
        ),
    ] = None
    """
    If populated, this is the reward power cap for the current season.
    """

    date_last_played: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dateLastPlayed"),
        pydantic.Field(
            alias="dateLastPlayed", description="The last time the user played with any character on this Profile."
        ),
    ] = None
    """
    The last time the user played with any character on this Profile.
    """

    event_card_hashes_owned: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="eventCardHashesOwned"),
        pydantic.Field(
            alias="eventCardHashesOwned",
            description="A list of hashes for event cards that a profile owns. Unlike most values in versionsOwned, these stay with the profile across all platforms.",
        ),
    ] = None
    """
    A list of hashes for event cards that a profile owns. Unlike most values in versionsOwned, these stay with the profile across all platforms.
    """

    lifetime_highest_guardian_rank: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lifetimeHighestGuardianRank"),
        pydantic.Field(
            alias="lifetimeHighestGuardianRank",
            description="The 'lifetime highest' Guardian Rank value, which starts at rank 1.",
        ),
    ] = None
    """
    The 'lifetime highest' Guardian Rank value, which starts at rank 1.
    """

    season_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="seasonHashes"),
        pydantic.Field(
            alias="seasonHashes",
            description="A list of seasons that this profile owns. Unlike versionsOwned, these stay with the profile across Platforms, and thus will be valid.\r\n It turns out that Stadia Pro subscriptions will give access to seasons but only while playing on Stadia and with an active subscription. So some users (users who have Stadia Pro but choose to play on some other platform) won't see these as available: it will be whatever seasons are available for the platform on which they last played.",
        ),
    ] = None
    """
    A list of seasons that this profile owns. Unlike versionsOwned, these stay with the profile across Platforms, and thus will be valid.
     It turns out that Stadia Pro subscriptions will give access to seasons but only while playing on Stadia and with an active subscription. So some users (users who have Stadia Pro but choose to play on some other platform) won't see these as available: it will be whatever seasons are available for the platform on which they last played.
    """

    user_info: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard],
        FieldMetadata(alias="userInfo"),
        pydantic.Field(
            alias="userInfo",
            description="If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information.",
        ),
    ] = None
    """
    If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information.
    """

    versions_owned: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="versionsOwned"),
        pydantic.Field(
            alias="versionsOwned",
            description="If you want to know what expansions they own, this will contain that data.\r\n IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.\r\n If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be \"good enough.\" Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC.",
        ),
    ] = None
    """
    If you want to know what expansions they own, this will contain that data.
     IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.
     If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be "good enough." Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
