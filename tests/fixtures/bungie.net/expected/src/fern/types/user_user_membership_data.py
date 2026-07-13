

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_user_info_card import GroupsV2GroupUserInfoCard
from .user_general_user import UserGeneralUser


class UserUserMembershipData(UniversalBaseModel):
    bungie_net_user: typing_extensions.Annotated[
        typing.Optional[UserGeneralUser], FieldMetadata(alias="bungieNetUser")
    ] = None
    destiny_memberships: typing_extensions.Annotated[
        typing.Optional[typing.List[GroupsV2GroupUserInfoCard]], FieldMetadata(alias="destinyMemberships")
    ] = pydantic.Field(default=None)
    """
    this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)
    """

    primary_membership_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="primaryMembershipId")
    ] = pydantic.Field(default=None)
    """
    If this property is populated, it will have the membership ID of the account considered to be "primary" in this user's cross save relationship.
     If null, this user has no cross save relationship, nor primary account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
