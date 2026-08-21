

import typing

from ..core.api_error import ApiError
from ..types.invalid_web_acl_id import InvalidWebAclId


class NetworkAuthenticationRequiredError(ApiError):
    def __init__(self, body: InvalidWebAclId, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=511, headers=headers, body=body)
