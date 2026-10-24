

import typing

MissionEventResourceType = typing.Union[
    typing.Literal["agent_run", "agent_task", "report_sync", "job", "daily_ops_run", "proposal", "proposal_execution"],
    typing.Any,
]
