

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostTestTypeRequestAction(str, enum.Enum):
    TEST_TYPE = "TestType"

    def visit(self, test_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostTestTypeRequestAction.TEST_TYPE:
            return test_type()
