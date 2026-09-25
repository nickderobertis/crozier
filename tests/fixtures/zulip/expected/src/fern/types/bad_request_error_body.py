

import typing

from .incompatible_parameters_error import IncompatibleParametersError
from .invalid_api_key_error import InvalidApiKeyError
from .missing_argument_error import MissingArgumentError
from .user_not_authorized_error import UserNotAuthorizedError

BadRequestErrorBody = typing.Union[
    InvalidApiKeyError, MissingArgumentError, IncompatibleParametersError, UserNotAuthorizedError
]
