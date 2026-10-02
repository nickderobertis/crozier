

import typing

PostOauthDetailsV3ResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "invalid_client_id",
        "invalid_redirect_uri",
        "invalid_scope",
        "no_acr_registered",
        "invalid_response_type",
        "invalid_display",
        "invalid_prompt",
        "unsupported_pkce_challenge_method",
        "invalid_pkce_challenge",
        "invalid_request",
        "invalid_id_token_hint",
        "use_pkce",
    ],
    typing.Any,
]
