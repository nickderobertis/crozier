

import typing

PostOauthClientRequestRequestAuthContextRefsItem = typing.Union[
    typing.Literal[
        "mosip:idp:acr:static-code",
        "mosip:idp:acr:generated-code",
        "mosip:idp:acr:linked-wallet",
        "mosip:idp:acr:biometrics",
        "mosip:idp:acr:knowledge",
        "mosip:idp:acr:id-token",
        "mosip:idp:acr:password",
    ],
    typing.Any,
]
