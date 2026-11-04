

import typing

from .bad_request_error_body_error_code import BadRequestErrorBodyErrorCode
from .error_extended import ErrorExtended

BadRequestErrorBody = typing.Union[ErrorExtended, BadRequestErrorBodyErrorCode]
