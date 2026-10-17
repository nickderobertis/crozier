

import typing

OAuthTokenBodyGrantType = typing.Union[
    typing.Literal["authorization_code", "refresh_token", "urn:ietf:params:oauth:grant-type:jwt-bearer"], typing.Any
]
