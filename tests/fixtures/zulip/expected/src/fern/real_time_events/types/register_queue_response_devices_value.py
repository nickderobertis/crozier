

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseDevicesValue(UniversalBaseModel):
    """
    `{device_id}`: Dictionary containing the details of
    a device with the device ID as the key.
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
    """

    pending_push_token_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID to reference the token provided by FCM/APNs to the device,
    whose registration is in progress to the push bouncer service.
    """

    push_token_last_updated_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for the last time when `pending_push_token_id`
    was set to a new non-null value, in UTC seconds.
    """

    push_registration_error_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the push registration failed, a [Zulip API error
    code](/api/rest-error-handling) indicating the type of
    failure that occurred.
    
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
