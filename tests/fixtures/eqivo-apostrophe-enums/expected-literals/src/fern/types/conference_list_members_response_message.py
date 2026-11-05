

import typing

ConferenceListMembersResponseMessage = typing.Union[
    typing.Literal[
        "Conference ListMembers Executed",
        "ConferenceName Parameter must be present",
        "Conference ListMembers Failed to parse result",
        "Conference ListMembers Failed -- Conference not found",
    ],
    typing.Any,
]
