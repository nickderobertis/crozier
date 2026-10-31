

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkuAvailabilityValidationResponsePropertiesStatus(enum.StrEnum):
    """
    Sku availability validation status.
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
        if self is SkuAvailabilityValidationResponsePropertiesStatus.VALID:
            return valid()
        if self is SkuAvailabilityValidationResponsePropertiesStatus.INVALID:
            return invalid()
        if self is SkuAvailabilityValidationResponsePropertiesStatus.SKIPPED:
            return skipped()
