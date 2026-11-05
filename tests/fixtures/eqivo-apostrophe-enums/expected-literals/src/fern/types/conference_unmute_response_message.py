

import typing

ConferenceUnmuteResponseMessage = typing.Union[
    typing.Literal[
        "Conference Unmute Executed",
        "ConferenceName Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Unmute Failed -- Conference not found",
    ],
    typing.Any,
]
