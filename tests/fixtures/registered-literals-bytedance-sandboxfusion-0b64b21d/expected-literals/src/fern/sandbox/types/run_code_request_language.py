

import typing

RunCodeRequestLanguage = typing.Union[
    typing.Literal[
        "python",
        "cpp",
        "nodejs",
        "go",
        "go_test",
        "java",
        "php",
        "csharp",
        "bash",
        "typescript",
        "sql",
        "rust",
        "cuda",
        "lua",
        "R",
        "perl",
        "D_ut",
        "ruby",
        "scala",
        "julia",
        "pytest",
        "junit",
        "kotlin_script",
        "jest",
        "verilog",
        "python_gpu",
        "lean",
        "swift",
        "racket",
    ],
    typing.Any,
]
