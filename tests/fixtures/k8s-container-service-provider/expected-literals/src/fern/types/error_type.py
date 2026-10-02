

import typing

ErrorType = typing.Union[
    typing.Literal[
        "https://dcm-project.github.io/problems/invalid-argument",
        "https://dcm-project.github.io/problems/not-found",
        "https://dcm-project.github.io/problems/already-exists",
        "https://dcm-project.github.io/problems/permission-denied",
        "https://dcm-project.github.io/problems/unauthenticated",
        "https://dcm-project.github.io/problems/internal",
        "https://dcm-project.github.io/problems/unavailable",
    ],
    typing.Any,
]
