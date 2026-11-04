

import typing

ExpenseStatus = typing.Union[
    typing.Literal["DRAFT", "SUBMITTED", "APPROVED", "OUT_OF_POLICY", "VOID", "CANCELED", "SPLIT", "SETTLED"],
    typing.Any,
]
