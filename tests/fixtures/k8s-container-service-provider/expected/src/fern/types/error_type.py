

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorType(enum.StrEnum):
    """
    URI reference identifying the error type
    """

    INVALIDARGUMENT = "https://dcm-project.github.io/problems/invalid-argument"
    NOTFOUND = "https://dcm-project.github.io/problems/not-found"
    ALREADYEXISTS = "https://dcm-project.github.io/problems/already-exists"
    PERMISSIONDENIED = "https://dcm-project.github.io/problems/permission-denied"
    UNAUTHENTICATED = "https://dcm-project.github.io/problems/unauthenticated"
    INTERNAL = "https://dcm-project.github.io/problems/internal"
    UNAVAILABLE = "https://dcm-project.github.io/problems/unavailable"

    def visit(
        self,
        invalidargument: typing.Callable[[], T_Result],
        notfound: typing.Callable[[], T_Result],
        alreadyexists: typing.Callable[[], T_Result],
        permissiondenied: typing.Callable[[], T_Result],
        unauthenticated: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorType.INVALIDARGUMENT:
            return invalidargument()
        if self is ErrorType.NOTFOUND:
            return notfound()
        if self is ErrorType.ALREADYEXISTS:
            return alreadyexists()
        if self is ErrorType.PERMISSIONDENIED:
            return permissiondenied()
        if self is ErrorType.UNAUTHENTICATED:
            return unauthenticated()
        if self is ErrorType.INTERNAL:
            return internal()
        if self is ErrorType.UNAVAILABLE:
            return unavailable()
