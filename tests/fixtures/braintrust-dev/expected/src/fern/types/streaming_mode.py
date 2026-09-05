

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamingMode(enum.StrEnum):
    """
    The mode format of the returned value (defaults to 'auto')
    """

    AUTO = "auto"
    PARALLEL = "parallel"
    JSON = "json"
    TEXT = "text"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        parallel: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StreamingMode.AUTO:
            return auto()
        if self is StreamingMode.PARALLEL:
            return parallel()
        if self is StreamingMode.JSON:
            return json()
        if self is StreamingMode.TEXT:
            return text()
