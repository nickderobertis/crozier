

import typing

BadRequestErrorBodyError = typing.Union[
    typing.Literal[
        "invalid_request",
        "invalid_client_id",
        "invalid_redirect_uri",
        "invalid_scope",
        "invalid_acr",
        "invalid_response_type",
        "invalid_display",
        "invalid_prompt",
    ],
    typing.Any,
]
