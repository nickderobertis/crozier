

import typing

PutMockserverRetrieveRequestType = typing.Union[
    typing.Literal["logs", "requests", "request_responses", "recorded_expectations", "active_expectations", "metrics"],
    typing.Any,
]
