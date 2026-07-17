

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsProfilesDestinyProfileTransitoryPartyMember(UniversalBaseModel):
    """
    This is some bare minimum information about a party member in a Fireteam. Unfortunately, without great computational expense on our side we can only get at the data contained here. I'd like to give you a character ID for example, but we don't have it. But we do have these three pieces of information. May they help you on your quest to show meaningful data about current Fireteams.
    Notably, we don't and can't feasibly return info on characters. If you can, try to use just the data below for your UI and purposes. Only hit us with further queries if you absolutely must know the character ID of the currently playing character. Pretty please with sugar on top.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="The player's last known display name."),
    ] = None
    """
    The player's last known display name.
    """

    emblem_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="emblemHash"),
        pydantic.Field(
            alias="emblemHash",
            description="The identifier for the DestinyInventoryItemDefinition of the player's emblem.",
        ),
    ] = None
    """
    The identifier for the DestinyInventoryItemDefinition of the player's emblem.
    """

    membership_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipId"),
        pydantic.Field(alias="membershipId", description="The Membership ID that matches the party member."),
    ] = None
    """
    The Membership ID that matches the party member.
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    A Flags Enumeration value indicating the states that the player is in relevant to being on a fireteam.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
