

import typing

AgentArtifactKind = typing.Union[
    typing.Literal[
        "input_evidence", "specialist_finding", "manager_synthesis", "reviewer_verdict", "weekly_ops_report"
    ],
    typing.Any,
]
