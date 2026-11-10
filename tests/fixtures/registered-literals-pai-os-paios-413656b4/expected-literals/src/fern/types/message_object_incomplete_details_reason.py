

import typing

MessageObjectIncompleteDetailsReason = typing.Union[
    typing.Literal["content_filter", "max_tokens", "run_cancelled", "run_expired", "run_failed"], typing.Any
]
