

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_seventy_data import GetEventsResponseEventsItemSeventyData
from .get_events_response_events_item_seventy_op import GetEventsResponseEventsItemSeventyOp
from .get_events_response_events_item_seventy_type import GetEventsResponseEventsItemSeventyType


class GetEventsResponseEventsItemSeventy(UniversalBaseModel):
    """
    The more general of two event types that may be used when
    sending an event to all users in a Zulip organization when
    the configuration of the organization (realm) has changed.

    Unlike the simpler [realm/update](#realm-update) event format, this
    event type supports multiple properties being changed in a
    single event.

    This event is also sent when deactivating or reactivating a user
    for settings set to anonymous user groups which the user is direct
    member of. When deactivating the user, event is only sent to users
    who cannot access the deactivated user.

    **Changes**: Starting with Zulip 10.0 (feature level 303), this
    event can also be sent when deactivating or reactivating a user.

    In Zulip 7.0 (feature level 163), the realm setting
    `email_address_visibility` was removed. It was replaced by a [user
    setting](/api/update-settings#parameter-email_address_visibility) with
    a [realm user default][user-defaults], with the encoding of different
    values preserved. Clients can support all versions by supporting the
    current API and treating every user as having the realm's
    `email_address_visibility` value.

    [user-defaults]: /api/update-realm-user-settings-defaults#parameter-email_address_visibility
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSeventyType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSeventyOp] = None
    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    Always `"default"`. Present for backwards-compatibility with older
    clients that predate the `update_dict` event style.
    
    **Deprecated** and will be removed in a future release.
    """

    data: typing.Optional[GetEventsResponseEventsItemSeventyData] = pydantic.Field(default=None)
    """
    An object containing the properties that have changed.
    
    **Changes**: In Zulip 10.0 (feature level 316), `edit_topic_policy`
    property was removed and replaced by `can_move_messages_between_topics_group`
    realm setting.
    
    In Zulip 7.0 (feature level 183), the
    `community_topic_editing_limit_seconds` property was removed.
    It was documented as potentially returned as a changed property
    in this event, but in fact it was only ever returned in the
    [`POST /register`](/api/register-queue) response.
    
    Before Zulip 6.0 (feature level 150), on changing any of
    `allow_message_editing`, `message_content_edit_limit_seconds`, or
    `edit_topic_policy` settings, this object included all the three settings
    irrespective of which of these settings were changed. Now, a separate event
    is sent for each changed setting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
