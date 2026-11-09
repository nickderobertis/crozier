

import typing

ConferenceHangupResponseMessage = typing.Union[
    typing.Literal[
        "Conference Hangup Executed",
        "ConferenceName Parameter must be present",
        "MemberID Parameter must be present",
        "Conference Hangup Failed -- Conference not found",
    ],
    typing.Any,
]
