

import typing

PilotWorkerStatusName = typing.Union[
    typing.Literal["scheduler", "job_worker", "report_worker", "daily_scheduler", "daily_worker", "proposal_worker"],
    typing.Any,
]
