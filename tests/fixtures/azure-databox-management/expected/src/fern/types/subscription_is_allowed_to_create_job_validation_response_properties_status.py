

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus(enum.StrEnum):
    """
    Validation status of subscription permission to create job.
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
        if self is SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus.VALID:
            return valid()
        if self is SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus.INVALID:
            return invalid()
        if self is SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus.SKIPPED:
            return skipped()
