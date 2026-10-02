

import typing

PostTokenRequestGrantType = typing.Union[
    typing.Literal[
        "authorization_code",
        "client_credentials",
        "password",
        "refresh_token",
        "urn:ietf:params:oauth:grant-type:token-exchange",
        "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "urn:openid:params:grant-type:ciba",
        "urn:ietf:params:oauth:grant-type:device_code",
    ],
    typing.Any,
]
