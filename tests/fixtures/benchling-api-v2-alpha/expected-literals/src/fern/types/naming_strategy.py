

import typing

NamingStrategy = typing.Union[
    typing.Literal[
        "NEW_IDS",
        "IDS_FROM_NAMES",
        "DELETE_NAMES",
        "SET_FROM_NAME_PARTS",
        "REPLACE_NAMES_FROM_PARTS",
        "KEEP_NAMES",
        "REPLACE_ID_AND_NAME_FROM_PARTS",
    ],
    typing.Any,
]
