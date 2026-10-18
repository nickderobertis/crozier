

import typing

from .http_method import HttpMethod
from .undefined import Undefined

WebhookUpdateParamsMethod = typing.Union[HttpMethod, Undefined]
