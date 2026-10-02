

import typing

TriggerRule = typing.Union[
    typing.Literal[
        "all_success",
        "all_failed",
        "all_done",
        "one_success",
        "one_failed",
        "none_failed",
        "none_skipped",
        "none_failed_or_skipped",
        "none_failed_min_one_success",
        "dummy",
    ],
    typing.Any,
]
