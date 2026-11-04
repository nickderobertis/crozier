

import typing

TokenizerType = typing.Union[
    typing.Literal[
        "AsciiAlphabetic",
        "UnicodeAlphanumeric",
        "UnicodeAlphanumericFolded",
        "Whitespace",
        "WhitespaceLowercase",
        "UnicodeAlphanumericZH",
    ],
    typing.Any,
]
