

import typing

RunType = typing.Union[
    typing.Literal[
        "task_v1", "task_v2", "task_v3", "workflow_run", "openai_cua", "anthropic_cua", "ui_tars", "yutori_navigator"
    ],
    typing.Any,
]
