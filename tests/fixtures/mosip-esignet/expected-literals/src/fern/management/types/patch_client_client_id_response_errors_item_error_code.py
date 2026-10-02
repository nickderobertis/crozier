

import typing

PatchClientClientIdResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "invalid_client_id",
        "invalid_client_name",
        "invalid_claim",
        "invalid_acr",
        "invalid_uri",
        "invalid_redirect_uri",
        "invalid_grant_type",
        "invalid_client_auth",
        "invalid_public_key",
        "invalid_additional_config",
    ],
    typing.Any,
]
