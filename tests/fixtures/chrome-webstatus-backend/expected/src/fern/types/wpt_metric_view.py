

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WptMetricView(enum.StrEnum):
    """
    The desired view of the WPT Data
    """

    TEST_COUNTS = "test_counts"
    SUBTEST_COUNTS = "subtest_counts"

    def visit(
        self, test_counts: typing.Callable[[], T_Result], subtest_counts: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WptMetricView.TEST_COUNTS:
            return test_counts()
        if self is WptMetricView.SUBTEST_COUNTS:
            return subtest_counts()
