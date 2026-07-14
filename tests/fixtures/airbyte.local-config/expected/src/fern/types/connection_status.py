

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectionStatus(str, enum.Enum):
    """
    Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    DEPRECATED = "deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionStatus.ACTIVE:
            return active()
        if self is ConnectionStatus.INACTIVE:
            return inactive()
        if self is ConnectionStatus.DEPRECATED:
            return deprecated()
