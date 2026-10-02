

import typing

MonsterAlignments = typing.Union[
    typing.Literal[
        "chaotic neutral",
        "chaotic evil",
        "chaotic good",
        "lawful neutral",
        "lawful evil",
        "lawful good",
        "neutral",
        "neutral evil",
        "neutral good",
        "any alignment",
        "unaligned",
    ],
    typing.Any,
]
