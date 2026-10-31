

import typing

from ...types.api_key_auth import ApiKeyAuth
from ...types.general_auth import GeneralAuth

SetUserAuthRequestAuthData = typing.Union[ApiKeyAuth, GeneralAuth]
