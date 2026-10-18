

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItemUserDefinedObjectsInInternalSchemasObjTypeZero(
    enum.StrEnum
):
    TABLE = "table"

    def visit(self, table: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ProjectUpgradeEligibilityResponseOutputValidationErrorsItemUserDefinedObjectsInInternalSchemasObjTypeZero.TABLE
        ):
            return table()
