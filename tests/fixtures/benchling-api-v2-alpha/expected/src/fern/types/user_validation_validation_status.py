

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserValidationValidationStatus(enum.StrEnum):
    """
    Valid values for this enum depend on whether it is used to set a value (e.g., in a POST request), or is a return value for an existing result.
    Acceptable values for setting a status are 'VALID' or 'INVALID'. Possible return values are 'VALID', 'INVALID', or 'PARTIALLY_VALID' (a result will be partially valid if it has some valid fields and some invalid fields).
    """

    VALID = "VALID"
    INVALID = "INVALID"
    PARTIALLY_VALID = "PARTIALLY_VALID"

    def visit(
        self,
        valid: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
        partially_valid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserValidationValidationStatus.VALID:
            return valid()
        if self is UserValidationValidationStatus.INVALID:
            return invalid()
        if self is UserValidationValidationStatus.PARTIALLY_VALID:
            return partially_valid()
