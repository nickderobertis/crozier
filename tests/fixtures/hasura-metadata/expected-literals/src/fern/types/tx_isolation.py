

import typing

TxIsolation = typing.Union[typing.Literal["read-committed", "repeatable-read", "serializable"], typing.Any]
