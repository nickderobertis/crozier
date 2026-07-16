

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetTestTypeRequestAction(enum.StrEnum):
    TEST_TYPE = "TestType"

    def visit(self, test_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTestTypeRequestAction.TEST_TYPE:
            return test_type()
