

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateStatefulIfNotExists(enum.StrEnum):
    """
    How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).
    """

    CREATE = "create"
    REJECT = "reject"

    def visit(self, create: typing.Callable[[], T_Result], reject: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunCreateStatefulIfNotExists.CREATE:
            return create()
        if self is RunCreateStatefulIfNotExists.REJECT:
            return reject()
