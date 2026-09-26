

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseCrossRealmBotsItem(UniversalBaseModel):
    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of the user.
    """

    delivery_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's real email address. This value will be `null` if you cannot
    access user's real email address. For bot users, this field is always
    set to the real email of the bot, because bot users always have
    `email_address_visibility` set to everyone.
    
    **Changes**: Prior to Zulip 7.0 (feature level 163), this field was
    present only when `email_address_visibility` was restricted and you had
    access to the user's real email. As of this feature level, this field
    is always present, including the case when `email_address_visibility`
    is set to everyone (and therefore not restricted).
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Zulip API email address of the user or bot.
    
    If you do not have permission to view the email address of the target user,
    this will be a fake email address that is usable for the Zulip API but nothing else.
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the user or bot, used for all display purposes.
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
    """

    is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the user account has been deactivated.
    """

    is_owner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the user is an organization owner.
    If true, `is_admin` will also be true.
    
    **Changes**: New in Zulip 3.0 (feature level 8).
    """

    is_admin: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the user is an organization administrator.
    """

    is_guest: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the user is a guest user.
    """

    is_bot: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the user is a bot or full account.
    """

    is_system_bot: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user is a system bot. System bots are special
    bot user accounts that are managed by the system, rather than
    the organization's administrators.
    
    **Changes**: This field was called `is_cross_realm_bot`
    before Zulip 5.0 (feature level 83).
    """

    bot_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer describing the type of bot:
    
    - `null` if the user isn't a bot.
    - `1` for a `Generic` bot.
    - `2` for an `Incoming webhook` bot.
    - `3` for an `Outgoing webhook` bot.
    - `4` for an `Embedded` bot.
    """

    bot_owner_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    If the user is a bot (i.e. `is_bot` is true), then `bot_owner_id`
    is the user ID of the bot's owner (usually, whoever created the bot).
    
    Will be `null` for legacy bots that do not have an owner.
    
    **Changes**: New in Zulip 3.0 (feature level 1). In previous
    versions, there was a `bot_owner` field containing the email
    address of the bot's owner.
    """

    role: typing.Optional[int] = pydantic.Field(default=None)
    """
    [Organization-level role](/api/roles-and-permissions) of the user.
    Possible values are:
    
    - 100 = Organization owner
    - 200 = Organization administrator
    - 300 = Organization moderator
    - 400 = Member
    - 600 = Guest
    
    **Changes**: New in Zulip 4.0 (feature level 59).
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IANA identifier of the user's [profile time zone](/help/change-your-timezone),
    which is used primarily to display the user's local time to other users.
    """

    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for the user's avatar.
    
    Will be `null` if the `client_gravatar`
    query parameter was set to `true`, the current user has access to
    this user's real email address, and this user's avatar is hosted by
    the Gravatar provider (i.e. this user has never uploaded an avatar).
    
    **Changes**: Before Zulip 7.0 (feature level 163), access to a
    user's real email address was a realm-level setting. As of this
    feature level, `email_address_visibility` is a user setting.
    
    In Zulip 3.0 (feature level 18), if the client has the
    `user_avatar_url_field_optional` capability, this will be missing at
    the server's sole discretion.
    """

    avatar_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version for the user's avatar. Used for cache-busting requests
    for the user's avatar. Clients generally shouldn't need to use this;
    most avatar URLs sent by Zulip will already end with `?v={avatar_version}`.
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

    is_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the user has been permanently
    deleted. Deleted users are a subset of deactivated users
    (`is_active=false`) who have had their account data removed.
    
    This field is only present when `true`.
    
    **Changes**: New in Zulip 12.0 (feature level 490).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
