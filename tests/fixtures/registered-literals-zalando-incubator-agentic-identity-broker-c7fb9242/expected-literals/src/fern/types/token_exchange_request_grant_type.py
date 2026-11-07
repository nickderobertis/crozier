

import typing

TokenExchangeRequestGrantType = typing.Union[
    typing.Literal["urn:ietf:params:oauth:grant-type:token-exchange", "authorization_code", "client_credentials"],
    typing.Any,
]
