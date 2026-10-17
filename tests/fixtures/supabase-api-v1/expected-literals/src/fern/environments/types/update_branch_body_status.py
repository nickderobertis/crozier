

import typing

UpdateBranchBodyStatus = typing.Union[
    typing.Literal[
        "CREATING_PROJECT",
        "RUNNING_MIGRATIONS",
        "MIGRATIONS_PASSED",
        "MIGRATIONS_FAILED",
        "FUNCTIONS_DEPLOYED",
        "FUNCTIONS_FAILED",
    ],
    typing.Any,
]
