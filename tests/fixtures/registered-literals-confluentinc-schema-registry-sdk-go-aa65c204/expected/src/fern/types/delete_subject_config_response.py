

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteSubjectConfigResponse(enum.StrEnum):
    NONE = "NONE"
    BACKWARD = "BACKWARD"
    BACKWARD_TRANSITIVE = "BACKWARD_TRANSITIVE"
    FORWARD = "FORWARD"
    FORWARD_TRANSITIVE = "FORWARD_TRANSITIVE"
    FULL = "FULL"
    FULL_TRANSITIVE = "FULL_TRANSITIVE"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        backward: typing.Callable[[], T_Result],
        backward_transitive: typing.Callable[[], T_Result],
        forward: typing.Callable[[], T_Result],
        forward_transitive: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
        full_transitive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeleteSubjectConfigResponse.NONE:
            return none()
        if self is DeleteSubjectConfigResponse.BACKWARD:
            return backward()
        if self is DeleteSubjectConfigResponse.BACKWARD_TRANSITIVE:
            return backward_transitive()
        if self is DeleteSubjectConfigResponse.FORWARD:
            return forward()
        if self is DeleteSubjectConfigResponse.FORWARD_TRANSITIVE:
            return forward_transitive()
        if self is DeleteSubjectConfigResponse.FULL:
            return full()
        if self is DeleteSubjectConfigResponse.FULL_TRANSITIVE:
            return full_transitive()
