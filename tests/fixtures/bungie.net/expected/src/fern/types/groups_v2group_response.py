

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_member import GroupsV2GroupMember
from .groups_v2group_potential_member import GroupsV2GroupPotentialMember
from .groups_v2group_v2 import GroupsV2GroupV2


class GroupsV2GroupResponse(UniversalBaseModel):
    alliance_status: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="allianceStatus")] = None
    allied_ids: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="alliedIds")] = None
    current_user_member_map: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, GroupsV2GroupMember]], FieldMetadata(alias="currentUserMemberMap")
    ] = pydantic.Field(default=None)
    """
    This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available.
    """

    current_user_memberships_inactive_for_destiny: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="currentUserMembershipsInactiveForDestiny")
    ] = pydantic.Field(default=None)
    """
    A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.
    """

    current_user_potential_member_map: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, GroupsV2GroupPotentialMember]],
        FieldMetadata(alias="currentUserPotentialMemberMap"),
    ] = pydantic.Field(default=None)
    """
    This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once.
    """

    detail: typing.Optional[GroupsV2GroupV2] = None
    founder: typing.Optional[GroupsV2GroupMember] = None
    group_join_invite_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="groupJoinInviteCount")
    ] = None
    parent_group: typing_extensions.Annotated[typing.Optional[GroupsV2GroupV2], FieldMetadata(alias="parentGroup")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
