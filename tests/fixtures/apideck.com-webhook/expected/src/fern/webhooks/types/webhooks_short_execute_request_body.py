

import typing

from ...types.execute_webhook_event_request import ExecuteWebhookEventRequest
from ...types.execute_webhook_events_request import ExecuteWebhookEventsRequest

WebhooksShortExecuteRequestBody = typing.Union[ExecuteWebhookEventRequest, ExecuteWebhookEventsRequest]
