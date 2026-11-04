

import typing

from .error import Error
from .rate_limit_error import RateLimitError

TooManyRequestsErrorBody = typing.Union[Error, RateLimitError]
