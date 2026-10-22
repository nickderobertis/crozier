

import typing

PutMockserverRetrieveRequestFormat = typing.Union[
    typing.Literal[
        "java",
        "javascript",
        "python",
        "go",
        "csharp",
        "ruby",
        "rust",
        "php",
        "json",
        "log_entries",
        "har",
        "openapi",
        "postman",
        "bruno",
        "curl",
    ],
    typing.Any,
]
