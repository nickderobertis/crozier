

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_user_info_card import GroupsV2GroupUserInfoCard
from .user_user_info_card import UserUserInfoCard


class GroupsV2GroupBan(UniversalBaseModel):
    bungie_net_user_info: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard], FieldMetadata(alias="bungieNetUserInfo")
    ] = None
    comment: typing.Optional[str] = None
    created_by: typing_extensions.Annotated[typing.Optional[UserUserInfoCard], FieldMetadata(alias="createdBy")] = None
    date_banned: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dateBanned")] = None
    date_expires: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dateExpires")] = None
    destiny_user_info: typing_extensions.Annotated[
        typing.Optional[GroupsV2GroupUserInfoCard], FieldMetadata(alias="destinyUserInfo")
    ] = None
    group_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupId")] = None
    last_modified_by: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard], FieldMetadata(alias="lastModifiedBy")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
