

import typing

SessionMetricsMeterName = typing.Union[
    typing.Literal[
        "total_sessions",
        "total_cost_in_usd",
        "total_turns",
        "cost_per_session_in_usd",
        "avg_turns_per_session",
        "min_turns_per_session",
        "max_turns_per_session",
        "median_turns_per_session",
        "min_session_duration_ms",
        "max_session_duration_ms",
        "median_session_duration_ms",
        "p95_session_duration_ms",
    ],
    typing.Any,
]
