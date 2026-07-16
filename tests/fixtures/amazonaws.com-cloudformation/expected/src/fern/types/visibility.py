

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Visibility(str, enum.Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is Visibility.PUBLIC:
            return public()
        if self is Visibility.PRIVATE:
            return private()
