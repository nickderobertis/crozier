

import typing

DeletionRequestGrounds = typing.Union[
    typing.Literal[
        "no_longer_necessary",
        "consent_withdrawn",
        "objection_to_processing",
        "processing_unlawful",
        "legal_compliance",
        "underage_data_subject",
        "unspecified",
    ],
    typing.Any,
]
