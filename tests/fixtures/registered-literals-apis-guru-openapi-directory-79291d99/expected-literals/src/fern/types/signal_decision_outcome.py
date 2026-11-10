

import typing

SignalDecisionOutcome = typing.Union[
    typing.Literal["APPROVE", "REVIEW", "REJECT", "TAKE_OTHER_RISK_MEASURES", "NOT_EVALUATED"], typing.Any
]
