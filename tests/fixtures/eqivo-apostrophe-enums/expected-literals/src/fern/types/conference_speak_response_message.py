

import typing

ConferenceSpeakResponseMessage = typing.Union[
    typing.Literal[
        "Conference Speak Executed",
        "ConferenceName Parameter must be present",
        "Text Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Speak Failed -- Conference not found",
        "Conference Speak Failed",
    ],
    typing.Any,
]
