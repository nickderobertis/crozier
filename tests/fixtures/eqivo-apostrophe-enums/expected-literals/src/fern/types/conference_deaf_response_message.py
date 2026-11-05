

import typing

ConferenceDeafResponseMessage = typing.Union[
    typing.Literal[
        "Conference Deaf Executed",
        "ConferenceName Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Deaf Failed -- Conference not found",
    ],
    typing.Any,
]
