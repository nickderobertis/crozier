

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostTestTypeRequestAction(enum.StrEnum):
    TEST_TYPE = "TestType"

    def visit(self, test_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostTestTypeRequestAction.TEST_TYPE:
            return test_type()
