

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataDestinationDetailsValidationResponsePropertiesStatus(enum.StrEnum):
    """
    Data destination details validation status.
    """

    VALID = "Valid"
    INVALID = "Invalid"
    SKIPPED = "Skipped"

    def visit(
        self,
        valid: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataDestinationDetailsValidationResponsePropertiesStatus.VALID:
            return valid()
        if self is DataDestinationDetailsValidationResponsePropertiesStatus.INVALID:
            return invalid()
        if self is DataDestinationDetailsValidationResponsePropertiesStatus.SKIPPED:
            return skipped()
