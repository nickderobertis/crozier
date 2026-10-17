

import typing

from .undefined import Undefined
from .webhook_update_params import WebhookUpdateParams

AgentUpdateParamsWebhook = typing.Union[str, WebhookUpdateParams, Undefined]
