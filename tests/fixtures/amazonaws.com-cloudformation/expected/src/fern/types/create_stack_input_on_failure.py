

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateStackInputOnFailure(enum.StrEnum):
    """
    <p>Determines what action will be taken if stack creation fails. This must be one of: <code>DO_NOTHING</code>, <code>ROLLBACK</code>, or <code>DELETE</code>. You can specify either <code>OnFailure</code> or <code>DisableRollback</code>, but not both.</p> <p>Default: <code>ROLLBACK</code> </p>
    """

    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"
    DELETE = "DELETE"

    def visit(
        self,
        do_nothing: typing.Callable[[], T_Result],
        rollback: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateStackInputOnFailure.DO_NOTHING:
            return do_nothing()
        if self is CreateStackInputOnFailure.ROLLBACK:
            return rollback()
        if self is CreateStackInputOnFailure.DELETE:
            return delete()
