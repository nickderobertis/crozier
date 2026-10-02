

import typing

ProfilingMode = typing.Union[
    typing.Literal[
        "oncpu", "offcpu", "object_alloc", "object_usage", "virtual_alloc", "physical_alloc", "physical_usage"
    ],
    typing.Any,
]
