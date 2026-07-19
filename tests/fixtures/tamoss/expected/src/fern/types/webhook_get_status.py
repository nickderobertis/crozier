

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookGetStatus(enum.StrEnum):
    """
    Status of the Webhook. `created` indicates the webhook has been successfully registered but is yet to begin sending events or, depending on the service implementation, the worker responsible for sending the events has yet to start. `started` indicates the webhook is active and sending events. `disabled` indicates the webhook has been disabled by a client and is not currently sending events. `error` indicates an error condition has been encountered and the webhook has been disabled by the service instance. More information about the error condition will be indicated by the service instance in the `error` parameter. Service implementations SHOULD implement appropriate retries and only enter the `error` state when absolutely necesary. A webhook in the `error` or `disabled` state may be re-enabled by a client by setting the status to `created`. A webhook in the `created` or `started` state may be disabled by a client by setting the status to `disabled`. Attempting to transition an `error` status to `disabled` SHOULD be rejected.
    """

    CREATED = "created"
    STARTED = "started"
    DISABLED = "disabled"
    ERROR = "error"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookGetStatus.CREATED:
            return created()
        if self is WebhookGetStatus.STARTED:
            return started()
        if self is WebhookGetStatus.DISABLED:
            return disabled()
        if self is WebhookGetStatus.ERROR:
            return error()
