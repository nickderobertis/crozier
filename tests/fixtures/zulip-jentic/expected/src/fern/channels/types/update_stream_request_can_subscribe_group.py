

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_subscribe_group_new import UpdateStreamRequestCanSubscribeGroupNew
from .update_stream_request_can_subscribe_group_old import UpdateStreamRequestCanSubscribeGroupOld


class UpdateStreamRequestCanSubscribeGroup(UniversalBaseModel):
    """
    The set of users who have permission to subscribe themselves to this channel
    expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Everyone, excluding guests, can subscribe to any public channel
    irrespective of this setting.

    Users in this group can subscribe to a private channel as well.

    Note that a user must [have content access](/help/channel-permissions)
    to a channel and permission to administer the channel in order to
    modify this setting.

    **Changes**: New in Zulip 10.0 (feature level 357).
    """

    new: UpdateStreamRequestCanSubscribeGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanSubscribeGroupOld] = pydantic.Field(default=None)
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
