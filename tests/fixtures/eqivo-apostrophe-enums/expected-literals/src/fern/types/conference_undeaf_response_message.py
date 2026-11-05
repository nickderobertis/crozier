

import typing

ConferenceUndeafResponseMessage = typing.Union[
    typing.Literal[
        "Conference Undeaf Executed",
        "ConferenceName Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Undeaf Failed -- Conference not found",
    ],
    typing.Any,
]
