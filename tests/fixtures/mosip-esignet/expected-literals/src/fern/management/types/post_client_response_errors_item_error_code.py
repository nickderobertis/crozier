

import typing

PostClientResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "duplicate_client_id",
        "invalid_public_key",
        "invalid_input",
        "invalid_client_id",
        "invalid_client_name",
        "invalid_rp_id",
        "invalid_claim",
        "invalid_acr",
        "invalid_uri",
        "invalid_redirect_uri",
        "invalid_grant_type",
        "invalid_client_auth",
    ],
    typing.Any,
]
