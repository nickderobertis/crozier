

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActUpdateRequestReasonCodeSubjectRole(enum.StrEnum):
    REQUESTER = "REQUESTER"
    FULFILLER = "FULFILLER"

    def visit(self, requester: typing.Callable[[], T_Result], fulfiller: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActUpdateRequestReasonCodeSubjectRole.REQUESTER:
            return requester()
        if self is ActUpdateRequestReasonCodeSubjectRole.FULFILLER:
            return fulfiller()
