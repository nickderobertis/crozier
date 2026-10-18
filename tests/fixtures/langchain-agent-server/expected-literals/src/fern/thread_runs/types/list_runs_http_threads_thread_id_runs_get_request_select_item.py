

import typing

ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem = typing.Union[
    typing.Literal[
        "run_id",
        "thread_id",
        "assistant_id",
        "created_at",
        "updated_at",
        "status",
        "metadata",
        "kwargs",
        "multitask_strategy",
        "langsmith_session_name",
    ],
    typing.Any,
]
