

import typing

ObBalanceType1Code = typing.Union[
    typing.Literal[
        "ClosingAvailable",
        "ClosingBooked",
        "ClosingCleared",
        "Expected",
        "ForwardAvailable",
        "Information",
        "InterimAvailable",
        "InterimBooked",
        "InterimCleared",
        "OpeningAvailable",
        "OpeningBooked",
        "OpeningCleared",
        "PreviouslyClosedBooked",
    ],
    typing.Any,
]
