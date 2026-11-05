

import typing

ConferencePlayResponseMessage = typing.Union[
    typing.Literal[
        "Conference Play Executed",
        "ConferenceName Parameter must be present",
        "FilePath Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Play Failed -- Conference not found",
        "Conference Play Failed",
    ],
    typing.Any,
]
