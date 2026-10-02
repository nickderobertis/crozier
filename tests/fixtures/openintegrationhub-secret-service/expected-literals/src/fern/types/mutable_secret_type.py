

import typing

MutableSecretType = typing.Union[
    typing.Literal[
        "API_KEY", "OA1_TWO_LEGGED", "OA1_THREE_LEGGED", "OA2_AUTHORIZATION_CODE", "SIMPLE", "MIXED", "SESSION_AUTH"
    ],
    typing.Any,
]
