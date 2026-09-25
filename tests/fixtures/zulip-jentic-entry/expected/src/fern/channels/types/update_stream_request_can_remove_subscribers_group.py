

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_remove_subscribers_group_new import UpdateStreamRequestCanRemoveSubscribersGroupNew
from .update_stream_request_can_remove_subscribers_group_old import UpdateStreamRequestCanRemoveSubscribersGroupOld


class UpdateStreamRequestCanRemoveSubscribersGroup(UniversalBaseModel):
    """
    The set of users who have permission to unsubscribe others from this
    channel expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Organization administrators can unsubscribe others from a channel as though
    they were in this group without being explicitly listed here.

    Note that a user must have metadata access to a channel and permission
    to administer the channel in order to modify this setting.

    **Changes**: Prior to Zulip 10.0 (feature level 349), channel administrators
    could not unsubscribe other users if they were not an organization
    administrator or part of `can_remove_subscribers_group`. Realm administrators
    were not allowed to unsubscribe other users from a private channel if they
    were not subscribed to that channel.

    Prior to Zulip 10.0 (feature level 320), this value was always the integer
    ID of a system group.

    Before Zulip 8.0 (feature level 197), the `can_remove_subscribers_group`
    setting was named `can_remove_subscribers_group_id`.

    New in Zulip 7.0 (feature level 161).
    """

    new: UpdateStreamRequestCanRemoveSubscribersGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanRemoveSubscribersGroupOld] = pydantic.Field(default=None)
    """
    The expected current [group-setting value](/api/group-setting-values)
    for who has this permission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
