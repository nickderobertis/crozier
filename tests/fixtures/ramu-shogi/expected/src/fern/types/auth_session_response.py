

import typing

from .auth_session_response_one import AuthSessionResponseOne
from .auth_session_response_zero import AuthSessionResponseZero

AuthSessionResponse = typing.Union[AuthSessionResponseZero, AuthSessionResponseOne]
