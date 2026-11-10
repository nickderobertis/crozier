

import typing

LoanAccountSubtype = typing.Union[
    typing.Literal[
        "auto",
        "business",
        "commercial",
        "construction",
        "consumer",
        "home equity",
        "loan",
        "mortgage",
        "line of credit",
        "student",
        "other",
        "all",
    ],
    typing.Any,
]
