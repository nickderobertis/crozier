

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopDimensionsReportsResponseMetricScope(enum.StrEnum):
    """
    The unit each row's `count` is measured in.
    - `session`: number of sessions attributed to the dimension value.
    - `user`: number of unique users attributed to the dimension value.
    """

    SESSION = "session"
    USER = "user"

    def visit(self, session: typing.Callable[[], T_Result], user: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopDimensionsReportsResponseMetricScope.SESSION:
            return session()
        if self is TopDimensionsReportsResponseMetricScope.USER:
            return user()
