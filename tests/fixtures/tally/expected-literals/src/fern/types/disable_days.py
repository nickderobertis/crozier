

import typing

DisableDays = typing.Union[
    typing.Literal[
        "IN_THE_PAST",
        "IN_THE_FUTURE",
        "MONDAYS",
        "TUESDAYS",
        "WEDNESDAYS",
        "THURSDAYS",
        "FRIDAYS",
        "SATURDAYS",
        "SUNDAYS",
    ],
    typing.Any,
]
