

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritablePrefixStatus(str, enum.Enum):
    """
    Operational status of this prefix
    """

    CONTAINER = "container"
    ACTIVE = "active"
    RESERVED = "reserved"
    DEPRECATED = "deprecated"

    def visit(
        self,
        container: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritablePrefixStatus.CONTAINER:
            return container()
        if self is WritablePrefixStatus.ACTIVE:
            return active()
        if self is WritablePrefixStatus.RESERVED:
            return reserved()
        if self is WritablePrefixStatus.DEPRECATED:
            return deprecated()
