

import typing

ConferenceMuteResponseMessage = typing.Union[
    typing.Literal[
        "Conference Mute Executed",
        "ConferenceName Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Mute Failed -- Conference not found",
    ],
    typing.Any,
]
