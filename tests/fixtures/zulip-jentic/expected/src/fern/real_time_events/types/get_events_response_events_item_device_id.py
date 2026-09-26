

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_device_id_op import GetEventsResponseEventsItemDeviceIdOp
from .get_events_response_events_item_device_id_type import GetEventsResponseEventsItemDeviceIdType


class GetEventsResponseEventsItemDeviceId(UniversalBaseModel):
    """
    Event sent to a user's clients when the metadata in the
    `devices` dictionary for the user changes.

    Helps clients to live-update the `devices` dictionary
    returned in [`POST /register`](/api/register-queue) response.

    Besides `id`, `type`, `op`, and `device_id`, all other fields
    are optional. Only fields whose values needs to be updated are
    included in the event.

    **Changes**: New in Zulip 12.0 (feature level 468).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemDeviceIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemDeviceIdOp] = None
    device_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the registered device whose metadata changed.
    """

    push_key_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID to reference the encryption key used to encrypt
    push notifications sent to the device.
    """

    push_token_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID to reference the token provided by FCM/APNs to the device,
    which is registered to the push bouncer service.
    
    A `null` value means the referenced token expired.
    """

    pending_push_token_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID to reference the token provided by FCM/APNs to the device,
    whose registration is in progress to the push bouncer service.
    
    A `null` value means the pending registration succeeded.
    """

    push_token_last_updated_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for the last time when `pending_push_token_id`
    was set to a new non-null value, in UTC seconds.
    """

    push_registration_error_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the push registration failed, a [Zulip API error code](/api/rest-error-handling)
    indicating the type of failure that occurred.
    
    The following error codes have recommended client behavior:
    
    - `"INVALID_BOUNCER_PUBLIC_KEY"` - Inform the user to update app.
    - `"REQUEST_EXPIRED` - Retry with a fresh payload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
