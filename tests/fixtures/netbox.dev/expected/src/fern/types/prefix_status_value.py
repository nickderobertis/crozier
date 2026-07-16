

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PrefixStatusValue(str, enum.Enum):
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
        if self is PrefixStatusValue.CONTAINER:
            return container()
        if self is PrefixStatusValue.ACTIVE:
            return active()
        if self is PrefixStatusValue.RESERVED:
            return reserved()
        if self is PrefixStatusValue.DEPRECATED:
            return deprecated()
