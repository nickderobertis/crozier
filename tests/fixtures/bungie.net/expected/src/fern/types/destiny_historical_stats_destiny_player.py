

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_user_info_card import UserUserInfoCard


class DestinyHistoricalStatsDestinyPlayer(UniversalBaseModel):
    bungie_net_user_info: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard], FieldMetadata(alias="bungieNetUserInfo")
    ] = pydantic.Field(default=None)
    """
    Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account.
    """

    character_class: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="characterClass")] = (
        pydantic.Field(default=None)
    )
    """
    Class of the character if applicable and available.
    """

    character_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="characterLevel")] = (
        pydantic.Field(default=None)
    )
    """
    Level of the character if available. Zero if it is not available.
    """

    clan_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="clanName")] = pydantic.Field(
        default=None
    )
    """
    Current clan name for the player. This value may be null or an empty string if the user does not have a clan.
    """

    clan_tag: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="clanTag")] = pydantic.Field(
        default=None
    )
    """
    Current clan tag for the player. This value may be null or an empty string if the user does not have a clan.
    """

    class_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="classHash")] = None
    destiny_user_info: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard], FieldMetadata(alias="destinyUserInfo")
    ] = pydantic.Field(default=None)
    """
    Details about the player as they are known in game (platform display name, Destiny emblem)
    """

    emblem_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="emblemHash")] = pydantic.Field(
        default=None
    )
    """
    If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it).
    """

    gender_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="genderHash")] = None
    light_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="lightLevel")] = pydantic.Field(
        default=None
    )
    """
    Light Level of the character if available. Zero if it is not available.
    """

    race_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="raceHash")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
