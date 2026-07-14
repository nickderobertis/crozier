

import typing

from ...types.resolve_webhook_event_request import ResolveWebhookEventRequest
from ...types.resolve_webhook_events_request import ResolveWebhookEventsRequest

WebhooksResolveRequestBody = typing.Union[ResolveWebhookEventRequest, ResolveWebhookEventsRequest]
