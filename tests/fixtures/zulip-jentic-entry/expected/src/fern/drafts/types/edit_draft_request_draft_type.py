

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EditDraftRequestDraftType(enum.StrEnum):
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
        if self is EditDraftRequestDraftType.EMPTY:
            return empty()
        if self is EditDraftRequestDraftType.STREAM:
            return stream()
        if self is EditDraftRequestDraftType.PRIVATE:
            return private()
