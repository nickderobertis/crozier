

import typing

TaskforceObjectPhase = typing.Union[
    typing.Literal[
        "pre-mq-activation",
        "pre-launch",
        "pending-starter",
        "condor-submit",
        "pending-stopper",
        "condor-rm",
        "condor-complete",
    ],
    typing.Any,
]
