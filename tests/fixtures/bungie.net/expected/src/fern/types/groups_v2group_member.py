

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_user_info_card import GroupsV2GroupUserInfoCard
from .user_user_info_card import UserUserInfoCard


class GroupsV2GroupMember(UniversalBaseModel):
    bungie_net_user_info: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard], FieldMetadata(alias="bungieNetUserInfo")
    ] = None
    destiny_user_info: typing_extensions.Annotated[
        typing.Optional[GroupsV2GroupUserInfoCard], FieldMetadata(alias="destinyUserInfo")
    ] = None
    group_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupId")] = None
    is_online: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isOnline")] = None
    join_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="joinDate")] = None
    last_online_status_change: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lastOnlineStatusChange")
    ] = None
    member_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="memberType")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
