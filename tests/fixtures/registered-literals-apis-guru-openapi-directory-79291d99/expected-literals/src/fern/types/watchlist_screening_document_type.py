

import typing

WatchlistScreeningDocumentType = typing.Union[
    typing.Literal[
        "birth_certificate",
        "drivers_license",
        "immigration_number",
        "military_id",
        "other",
        "passport",
        "personal_identification",
        "ration_card",
        "ssn",
        "student_id",
        "tax_id",
        "travel_document",
        "voter_id",
    ],
    typing.Any,
]
