

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .error import Error
from .webhook_get_status import WebhookGetStatus
from .webhook_with_id import WebhookWithId


class WebhookGet(WebhookWithId):
    """
    Describes a Webhook
    """

    error: typing.Optional[Error] = pydantic.Field(default=None)
    """
    Provides more information for the error status, as described by the [Error](#/schemas/error) type
    """

    status: WebhookGetStatus = pydantic.Field()
    """
    Status of the Webhook. `created` indicates the webhook has been successfully registered but is yet to begin sending events or, depending on the service implementation, the worker responsible for sending the events has yet to start. `started` indicates the webhook is active and sending events. `disabled` indicates the webhook has been disabled by a client and is not currently sending events. `error` indicates an error condition has been encountered and the webhook has been disabled by the service instance. More information about the error condition will be indicated by the service instance in the `error` parameter. Service implementations SHOULD implement appropriate retries and only enter the `error` state when absolutely necesary. A webhook in the `error` or `disabled` state may be re-enabled by a client by setting the status to `created`. A webhook in the `created` or `started` state may be disabled by a client by setting the status to `disabled`. Attempting to transition an `error` status to `disabled` SHOULD be rejected.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
