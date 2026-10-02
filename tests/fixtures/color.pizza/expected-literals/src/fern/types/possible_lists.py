

import typing

PossibleLists = typing.Union[
    typing.Literal[
        "default",
        "bestOf",
        "wikipedia",
        "french",
        "ridgway",
        "risograph",
        "basic",
        "chineseTraditional",
        "html",
        "japaneseTraditional",
        "leCorbusier",
        "nbsIscc",
        "ntc",
        "osxcrayons",
        "ral",
        "sanzoWadaI",
        "thesaurus",
        "werner",
        "windows",
        "x11",
        "xkcd",
    ],
    typing.Any,
]
