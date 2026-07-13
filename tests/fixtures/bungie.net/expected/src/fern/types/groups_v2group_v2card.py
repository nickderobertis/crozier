

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_v2clan_info import GroupsV2GroupV2ClanInfo


class GroupsV2GroupV2Card(UniversalBaseModel):
    """
    A small infocard of group information, usually used for when a list of groups are returned
    """

    about: typing.Optional[str] = None
    avatar_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="avatarPath")] = None
    capabilities: typing.Optional[int] = None
    clan_info: typing_extensions.Annotated[
        typing.Optional[GroupsV2GroupV2ClanInfo], FieldMetadata(alias="clanInfo")
    ] = None
    creation_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="creationDate")] = None
    group_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupId")] = None
    group_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupType")] = None
    locale: typing.Optional[str] = None
    member_count: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="memberCount")] = None
    membership_option: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipOption")] = None
    motto: typing.Optional[str] = None
    name: typing.Optional[str] = None
    theme: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
