

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_profiles_destiny_profile_transitory_current_activity import (
    DestinyComponentsProfilesDestinyProfileTransitoryCurrentActivity,
)
from .destiny_components_profiles_destiny_profile_transitory_joinability import (
    DestinyComponentsProfilesDestinyProfileTransitoryJoinability,
)
from .destiny_components_profiles_destiny_profile_transitory_party_member import (
    DestinyComponentsProfilesDestinyProfileTransitoryPartyMember,
)
from .destiny_components_profiles_destiny_profile_transitory_tracking_entry import (
    DestinyComponentsProfilesDestinyProfileTransitoryTrackingEntry,
)


class DestinyComponentsProfilesDestinyProfileTransitoryComponent(UniversalBaseModel):
    """
    This is an experimental set of data that Bungie considers to be "transitory" - information that may be useful for API users, but that is coming from a non-authoritative data source about information that could potentially change at a more frequent pace than Bungie.net will receive updates about it.
    This information is provided exclusively for convenience should any of it be useful to users: we provide no guarantees to the accuracy or timeliness of data that comes from this source. Know that this data can potentially be out-of-date or even wrong entirely if the user disconnected from the game or suddenly changed their status before we can receive refreshed data.
    """

    current_activity: typing_extensions.Annotated[
        typing.Optional[DestinyComponentsProfilesDestinyProfileTransitoryCurrentActivity],
        FieldMetadata(alias="currentActivity"),
    ] = pydantic.Field(default=None)
    """
    If you are in an activity, this is some transitory info about the activity currently being played.
    """

    joinability: typing.Optional[DestinyComponentsProfilesDestinyProfileTransitoryJoinability] = pydantic.Field(
        default=None
    )
    """
    Information about whether and what might prevent you from joining this person on a fireteam.
    """

    last_orbited_destination_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lastOrbitedDestinationHash")
    ] = pydantic.Field(default=None)
    """
    The hash identifier for the DestinyDestinationDefinition of the last location you were orbiting when in orbit.
    """

    party_members: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyComponentsProfilesDestinyProfileTransitoryPartyMember]],
        FieldMetadata(alias="partyMembers"),
    ] = pydantic.Field(default=None)
    """
    If you have any members currently in your party, this is some (very) bare-bones information about those members.
    """

    tracking: typing.Optional[typing.List[DestinyComponentsProfilesDestinyProfileTransitoryTrackingEntry]] = (
        pydantic.Field(default=None)
    )
    """
    Information about tracked entities.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
