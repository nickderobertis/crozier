

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OnFailure(str, enum.Enum):
    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"
    DELETE = "DELETE"

    def visit(
        self,
        do_nothing: typing.Callable[[], T_Result],
        rollback: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OnFailure.DO_NOTHING:
            return do_nothing()
        if self is OnFailure.ROLLBACK:
            return rollback()
        if self is OnFailure.DELETE:
            return delete()
