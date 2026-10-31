

import typing

TokenRequestGrantType = typing.Union[
    typing.Literal["urn:ietf:params:oauth:grant-type:device_code", "urn:ietf:params:oauth:grant-type:token-exchange"],
    typing.Any,
]
