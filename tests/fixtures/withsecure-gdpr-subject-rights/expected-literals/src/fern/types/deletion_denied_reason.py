

import typing

DeletionDeniedReason = typing.Union[
    typing.Literal[
        "freedom_of_expression",
        "legal_obligation",
        "public_health_interest",
        "archival",
        "legal_claims",
        "no_personal_data_to_delete",
        "no_grounds_for_deletion_request",
    ],
    typing.Any,
]
