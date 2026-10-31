

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus(enum.StrEnum):
    """
    Create order limit validation status.
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
        if self is CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus.VALID:
            return valid()
        if self is CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus.INVALID:
            return invalid()
        if self is CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus.SKIPPED:
            return skipped()
