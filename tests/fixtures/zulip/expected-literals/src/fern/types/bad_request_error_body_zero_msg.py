

import typing

BadRequestErrorBodyZeroMsg = typing.Union[
    typing.Literal[
        "Your organization has turned off message editing",
        "You don't have permission to edit this message",
        "The time limit for editing this message has past",
        "Nothing to change",
        "Topic can't be empty",
    ],
    typing.Any,
]
