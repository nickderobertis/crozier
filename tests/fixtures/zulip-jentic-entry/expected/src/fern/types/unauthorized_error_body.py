

import typing

from .realm_deactivated_error import RealmDeactivatedError
from .user_deactivated_error import UserDeactivatedError

UnauthorizedErrorBody = typing.Union[UserDeactivatedError, RealmDeactivatedError]
