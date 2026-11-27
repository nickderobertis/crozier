

import typing

SchemaDependencyTypes = typing.Union[
    typing.Literal[
        "container_schema",
        "plate_schema",
        "location_schema",
        "box_schema",
        "run_schema",
        "result_schema",
        "request_schema",
        "entry_schema",
        "workflow_task_schema",
    ],
    typing.Any,
]
