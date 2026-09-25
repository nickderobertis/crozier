

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Invite(UniversalBaseModel):
    """
    A dictionary containing details about an [invitation](/help/invite-new-users).
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the invitation.
    
    Note that email invitations and reusable invitation links are stored
    in different database tables on the server, so each ID is guaranteed
    to be unique in combination with the boolean value of `is_multiuse`,
    e.g. there can only be one invitation with `id: 1` and `is_multiuse:
    true`.
    """

    invited_by_user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The [user ID](/api/get-user) of the user who created the invitation.
    
    **Changes**: New in Zulip 3.0 (feature level 22), replacing the `ref`
    field which contained the Zulip display email address of the user who
    created the invitation.
    """

    invited: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the invitation was created, in UTC seconds.
    """

    expiry_date: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the invitation will expire, in UTC seconds.
    If `null`, the invitation never expires.
    """

    invited_as: typing.Optional[int] = pydantic.Field(default=None)
    """
    The [organization-level role](/api/roles-and-permissions) of the user that
    is created when the invitation is accepted.
    Possible values are:
    
    - 100 = Organization owner
    - 200 = Organization administrator
    - 300 = Organization moderator
    - 400 = Member
    - 600 = Guest
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address the invitation was sent to. This will not be present when
    `is_multiuse` is `true` (i.e. the invitation is a reusable invitation link).
    """

    notify_referrer_on_join: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating whether the referrer has opted to receive a direct
    message from [notification bot](/help/configure-automated-notices) when a user
    account is created using this invitation.
    
    **Changes**: New in Zulip 9.0 (feature level 267). Previously,
    referrers always received such direct messages.
    """

    link_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the reusable invitation link. This will not be present when
    `is_multiuse` is `false` (i.e. the invitation is an email invitation).
    """

    is_multiuse: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the [invitation](/help/invite-new-users) is a
    reusable invitation link or an email invitation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
