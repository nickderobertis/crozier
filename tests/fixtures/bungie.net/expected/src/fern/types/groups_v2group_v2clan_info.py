

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2clan_banner import GroupsV2ClanBanner


class GroupsV2GroupV2ClanInfo(UniversalBaseModel):
    """
    This contract contains clan-specific group information. It does not include any investment data.
    """

    clan_banner_data: typing_extensions.Annotated[
        typing.Optional[GroupsV2ClanBanner], FieldMetadata(alias="clanBannerData")
    ] = None
    clan_callsign: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="clanCallsign")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
