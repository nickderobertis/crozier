

import typing

from ...types.user_login_id import UserLoginId
from .logout_request_login_id_one import LogoutRequestLoginIdOne

LogoutRequestLoginId = typing.Union[UserLoginId, LogoutRequestLoginIdOne]
