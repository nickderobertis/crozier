

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PrefixStatusLabel(str, enum.Enum):
    CONTAINER = "Container"
    ACTIVE = "Active"
    RESERVED = "Reserved"
    DEPRECATED = "Deprecated"

    def visit(
        self,
        container: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PrefixStatusLabel.CONTAINER:
            return container()
        if self is PrefixStatusLabel.ACTIVE:
            return active()
        if self is PrefixStatusLabel.RESERVED:
            return reserved()
        if self is PrefixStatusLabel.DEPRECATED:
            return deprecated()
