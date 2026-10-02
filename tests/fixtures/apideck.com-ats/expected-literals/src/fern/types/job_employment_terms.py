

import typing

JobEmploymentTerms = typing.Union[
    typing.Literal[
        "full-time",
        "part-time",
        "internship",
        "contractor",
        "employee",
        "freelance",
        "temp",
        "seasonal",
        "volunteer",
        "other",
    ],
    typing.Any,
]
