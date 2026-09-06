

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiModelsPermissionDataRequired(enum.StrEnum):
    """
    Indicates if data is required or optional
    """

    YES = "Yes"
    NO = "No"
    OPTIONAL = "Optional"

    def visit(
        self,
        yes: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApiModelsPermissionDataRequired.YES:
            return yes()
        if self is ApiModelsPermissionDataRequired.NO:
            return no()
        if self is ApiModelsPermissionDataRequired.OPTIONAL:
            return optional()
