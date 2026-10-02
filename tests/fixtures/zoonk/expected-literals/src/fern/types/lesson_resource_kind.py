

import typing

LessonResourceKind = typing.Union[
    typing.Literal[
        "alphabet",
        "custom",
        "explanation",
        "grammar",
        "listening",
        "practice",
        "quiz",
        "reading",
        "review",
        "translation",
        "tutorial",
        "vocabulary",
    ],
    typing.Any,
]
