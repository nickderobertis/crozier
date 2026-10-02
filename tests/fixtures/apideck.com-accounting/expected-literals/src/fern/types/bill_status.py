

import typing

BillStatus = typing.Union[
    typing.Literal["draft", "submitted", "authorised", "partially_paid", "paid", "void", "credit", "deleted"],
    typing.Any,
]
