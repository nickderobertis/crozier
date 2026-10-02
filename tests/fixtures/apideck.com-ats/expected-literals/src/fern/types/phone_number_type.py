

import typing

PhoneNumberType = typing.Union[
    typing.Literal[
        "primary",
        "secondary",
        "home",
        "work",
        "office",
        "mobile",
        "assistant",
        "fax",
        "direct-dial-in",
        "personal",
        "other",
    ],
    typing.Any,
]
