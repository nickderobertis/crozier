

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_organization_members_invite_users_service_accounts_item import (
    PatchOrganizationMembersInviteUsersServiceAccountsItem,
)


class PatchOrganizationMembersInviteUsers(UniversalBaseModel):
    """
    Users to invite to the organization
    """

    ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Ids of existing users to invite
    """

    emails: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Emails of users to invite
    """

    service_accounts: typing.Optional[typing.List[PatchOrganizationMembersInviteUsersServiceAccountsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Service accounts to create
    """

    send_invite_emails: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, send invite emails to the users who wore actually added
    """

    group_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional list of group ids to add newly-invited users to.
    """

    group_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional list of group names to add newly-invited users to.
    """

    group_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Singular form of group_ids
    """

    group_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Singular form of group_names
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
