

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_progression import DestinyDestinyProgression
from .groups_v2clan_banner import GroupsV2ClanBanner


class GroupsV2GroupV2ClanInfoAndInvestment(UniversalBaseModel):
    """
    The same as GroupV2ClanInfo, but includes any investment data.
    """

    clan_banner_data: typing_extensions.Annotated[
        typing.Optional[GroupsV2ClanBanner], FieldMetadata(alias="clanBannerData")
    ] = None
    clan_callsign: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="clanCallsign")] = None
    d2clan_progressions: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyDestinyProgression]], FieldMetadata(alias="d2ClanProgressions")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
