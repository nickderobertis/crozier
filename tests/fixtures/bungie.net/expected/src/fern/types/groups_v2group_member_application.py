

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_user_info_card import GroupsV2GroupUserInfoCard
from .user_user_info_card import UserUserInfoCard


class GroupsV2GroupMemberApplication(UniversalBaseModel):
    bungie_net_user_info: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard],
        FieldMetadata(alias="bungieNetUserInfo"),
        pydantic.Field(alias="bungieNetUserInfo"),
    ] = None
    creation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="creationDate"), pydantic.Field(alias="creationDate")
    ] = None
    destiny_user_info: typing_extensions.Annotated[
        typing.Optional[GroupsV2GroupUserInfoCard],
        FieldMetadata(alias="destinyUserInfo"),
        pydantic.Field(alias="destinyUserInfo"),
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    request_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="requestMessage"), pydantic.Field(alias="requestMessage")
    ] = None
    resolve_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="resolveDate"), pydantic.Field(alias="resolveDate")
    ] = None
    resolve_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resolveMessage"), pydantic.Field(alias="resolveMessage")
    ] = None
    resolve_state: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="resolveState"), pydantic.Field(alias="resolveState")
    ] = None
    resolved_by_membership_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="resolvedByMembershipId"),
        pydantic.Field(alias="resolvedByMembershipId"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
