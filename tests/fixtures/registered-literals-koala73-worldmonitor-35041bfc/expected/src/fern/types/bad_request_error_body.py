

import typing

from .jmespath_projection_error import JmespathProjectionError
from .validation_error import ValidationError

BadRequestErrorBody = typing.Union[ValidationError, JmespathProjectionError]
