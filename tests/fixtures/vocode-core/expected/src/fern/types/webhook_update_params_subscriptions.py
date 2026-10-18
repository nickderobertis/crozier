

import typing

from .event_type import EventType
from .undefined import Undefined

WebhookUpdateParamsSubscriptions = typing.Union[typing.List[EventType], Undefined]
