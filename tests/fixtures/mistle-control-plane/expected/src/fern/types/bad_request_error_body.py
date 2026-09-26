

import typing

from .bad_request_error_body_one import BadRequestErrorBodyOne
from .bad_request_error_body_zero import BadRequestErrorBodyZero

BadRequestErrorBody = typing.Union[BadRequestErrorBodyZero, BadRequestErrorBodyOne]
