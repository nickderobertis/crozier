

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemEightEvent(enum.StrEnum):
    TEST_RESULT = "testResult"

    def visit(self, test_result: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemEightEvent.TEST_RESULT:
            return test_result()
