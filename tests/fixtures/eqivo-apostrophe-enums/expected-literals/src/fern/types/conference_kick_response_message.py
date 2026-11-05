

import typing

ConferenceKickResponseMessage = typing.Union[
    typing.Literal[
        "Conference Kick Executed",
        "ConferenceName Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Kick Failed -- Conference not found",
    ],
    typing.Any,
]
