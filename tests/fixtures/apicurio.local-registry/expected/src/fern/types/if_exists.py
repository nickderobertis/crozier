

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IfExists(str, enum.Enum):
    """ """

    FAIL = "FAIL"
    UPDATE = "UPDATE"
    RETURN = "RETURN"
    RETURN_OR_UPDATE = "RETURN_OR_UPDATE"

    def visit(
        self,
        fail: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        return_: typing.Callable[[], T_Result],
        return_or_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IfExists.FAIL:
            return fail()
        if self is IfExists.UPDATE:
            return update()
        if self is IfExists.RETURN:
            return return_()
        if self is IfExists.RETURN_OR_UPDATE:
            return return_or_update()
