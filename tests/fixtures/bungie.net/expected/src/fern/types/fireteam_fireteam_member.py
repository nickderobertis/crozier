

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fireteam_fireteam_user_info_card import FireteamFireteamUserInfoCard
from .user_user_info_card import UserUserInfoCard


class FireteamFireteamMember(UniversalBaseModel):
    bungie_net_user_info: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard], FieldMetadata(alias="bungieNetUserInfo")
    ] = None
    character_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="characterId")] = None
    date_joined: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dateJoined")] = None
    destiny_user_info: typing_extensions.Annotated[
        typing.Optional[FireteamFireteamUserInfoCard], FieldMetadata(alias="destinyUserInfo")
    ] = None
    has_microphone: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="hasMicrophone")] = None
    last_platform_invite_attempt_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastPlatformInviteAttemptDate")
    ] = None
    last_platform_invite_attempt_result: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lastPlatformInviteAttemptResult")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
