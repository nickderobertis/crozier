

import typing

MissionEventEventType = typing.Union[
    typing.Literal[
        "agent_run.created",
        "agent_run.status_changed",
        "agent_task.created",
        "agent_task.status_changed",
        "report_sync.created",
        "report_sync.status_changed",
        "job.created",
        "job.status_changed",
        "daily_ops_run.created",
        "daily_ops_run.status_changed",
        "proposal.created",
        "proposal.status_changed",
        "proposal_execution.created",
        "proposal_execution.status_changed",
    ],
    typing.Any,
]
