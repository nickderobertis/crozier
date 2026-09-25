

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DraftType(enum.StrEnum):
    """
    The type of the draft. Either unaddressed (empty string), `"stream"`,
    or `"private"` (for one-on-one and group direct messages).
    """

    EMPTY = ""
    STREAM = "stream"
    PRIVATE = "private"

    def visit(
        self,
        empty: typing.Callable[[], T_Result],
        stream: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DraftType.EMPTY:
            return empty()
        if self is DraftType.STREAM:
            return stream()
        if self is DraftType.PRIVATE:
            return private()
