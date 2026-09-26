

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.profile_data import ProfileData


class GetOwnUserResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for the requesting user's avatar.
    
    **Changes**: New in Zulip 2.1.0.
    """

    avatar_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version for the requesting user's avatar. Used for cache-busting requests
    for the user's avatar. Clients generally shouldn't need to use this;
    most avatar URLs sent by Zulip will already end with `?v={avatar_version}`.
    
    **Changes**: New in Zulip 3.0 (feature level 10).
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Zulip API email of the requesting user.
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the requesting user.
    """

    is_admin: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating if the requesting user is an admin.
    """

    is_owner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating if the requesting user is
    an organization owner.
    
    **Changes**: New in Zulip 3.0 (feature level 8).
    """

    role: typing.Optional[int] = pydantic.Field(default=None)
    """
    [Organization-level role](/api/roles-and-permissions) of
    the requesting user.
    Possible values are:
    
    - 100 = Organization owner
    - 200 = Organization administrator
    - 300 = Organization moderator
    - 400 = Member
    - 600 = Guest
    
    **Changes**: New in Zulip 4.0 (feature level 59).
    """

    is_guest: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating if the requesting user is a guest.
    
    **Changes**: New in Zulip 3.0 (feature level 10).
    """

    is_bot: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating if the requesting user is a bot.
    """

    is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the requesting user account
    has been deactivated.
    
    **Changes**: New in Zulip 3.0 (feature level 10).
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IANA identifier of the requesting user's [profile time zone](/help/change-your-timezone),
    which is used primarily to display the user's local time to other users.
    
    **Changes**: New in Zulip 3.0 (feature level 10).
    """

    date_joined: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the user joined. For users imported from other
    applications and users created via the API, this is set to the
    account creation time until the user logs in for the first time,
    after which it is updated to that login time.
    
    For imported users, clients can use the `is_imported_stub` flag
    to determine how to display this field: when `is_imported_stub`
    is `true`, the user has not yet logged in and this value is the
    account creation time during import; when `is_imported_stub` is
    `false`, this value reflects when the user first logged in.
    
    **Changes**: Starting with Zulip 12.0 (feature level 475),
    this field is updated when an imported stub user or a user created
    via the API logs in for the first time.
    
    New in Zulip 3.0 (feature level 10).
    """

    max_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The integer ID of the last message received by the requesting
    user's account.
    
    **Deprecated**. We plan to remove this in favor of recommending
    using `GET /messages` with `"anchor": "newest"`.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user's ID.
    """

    delivery_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The requesting user's real email address.
    
    **Changes**: Prior to Zulip 7.0 (feature level 163), this field was
    present only when `email_address_visibility` was restricted and the
    requesting user had permission to access realm users' emails. As of
    this feature level, this field is always present.
    """

    is_imported_stub: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether this user object is a stub account imported from
    another chat system. Stub accounts are used to represent the senders
    for imported messages. Stub accounts can be converted to regular Zulip
    accounts when the user starts using Zulip, preserving that imported
    user's message history.
    
    **Changes**: New in Zulip 12.0 (feature level 433).
    """

    profile_data: typing.Optional[ProfileData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
