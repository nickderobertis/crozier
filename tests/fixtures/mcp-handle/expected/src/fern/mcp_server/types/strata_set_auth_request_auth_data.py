

import typing

from ...types.api_key_auth import ApiKeyAuth
from ...types.general_auth import GeneralAuth

StrataSetAuthRequestAuthData = typing.Union[ApiKeyAuth, GeneralAuth]
