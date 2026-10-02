

import typing

PostDomainsResponseState = typing.Union[
    typing.Literal[
        "extra_records", "not_registered", "configured", "not_configured", "registration_pending", "not_verified"
    ],
    typing.Any,
]
