

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PaginationCoverageMode(str, enum.Enum):
    """
    How pagination is implemented on this connector. Native mode means Apideck is using the pagination parameters of the connector. With virtual pagination, the connector does not support pagination, but Apideck emulates it.
    """

    NATIVE = "native"
    VIRTUAL = "virtual"

    def visit(self, native: typing.Callable[[], T_Result], virtual: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaginationCoverageMode.NATIVE:
            return native()
        if self is PaginationCoverageMode.VIRTUAL:
            return virtual()
