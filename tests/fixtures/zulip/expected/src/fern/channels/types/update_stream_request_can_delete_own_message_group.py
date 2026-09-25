

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_delete_own_message_group_new import UpdateStreamRequestCanDeleteOwnMessageGroupNew
from .update_stream_request_can_delete_own_message_group_old import UpdateStreamRequestCanDeleteOwnMessageGroupOld


class UpdateStreamRequestCanDeleteOwnMessageGroup(UniversalBaseModel):
    """
    The set of users who have permission to delete the messages that they have
    sent in the channel expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Note that a user must [have content access](/help/channel-permissions) to a
    channel in order to delete their own message in the channel.

    Users with permission to delete any message in the channel
    and users present in the organization-level `can_delete_own_message_group` setting
    can always delete their own messages in the channel if they
    [have content access](/help/channel-permissions) to that channel.

    **Changes**: New in Zulip 11.0 (feature level 407). Prior to this
    change, only the users in the organization-level `can_delete_any_message_group`
    and `can_delete_own_message_group` settings were able delete their own messages in
    the organization.
    """

    new: UpdateStreamRequestCanDeleteOwnMessageGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanDeleteOwnMessageGroupOld] = pydantic.Field(default=None)
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
