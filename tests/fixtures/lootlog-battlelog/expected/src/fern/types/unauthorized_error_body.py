

import typing

from .unauthorized_error_body_error import UnauthorizedErrorBodyError
from .unauthorized_error_body_one import UnauthorizedErrorBodyOne

UnauthorizedErrorBody = typing.Union[UnauthorizedErrorBodyError, UnauthorizedErrorBodyOne]
