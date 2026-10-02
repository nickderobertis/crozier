

import typing

HrisEventType = typing.Union[
    typing.Literal[
        "*",
        "hris.employee.created",
        "hris.employee.updated",
        "hris.employee.deleted",
        "hris.company.created",
        "hris.company.updated",
        "hris.company.deleted",
    ],
    typing.Any,
]
