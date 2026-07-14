

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UserType(str, enum.Enum):
    """
    The user's type
    """

    NATIVE = "native"
    INTERNAL = "internal"
    EXTERNAL = "external"

    def visit(
        self,
        native: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        external: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserType.NATIVE:
            return native()
        if self is UserType.INTERNAL:
            return internal()
        if self is UserType.EXTERNAL:
            return external()
