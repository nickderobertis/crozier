

import typing

AccessTokenRequestGrantType = typing.Union[
    typing.Literal[
        "client_credentials", "private_key_jwt", "tls_client_auth", "urn:ietf:params:oauth:grant-type:device_code"
    ],
    typing.Any,
]
