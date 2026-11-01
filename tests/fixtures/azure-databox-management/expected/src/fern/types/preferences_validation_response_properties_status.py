

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreferencesValidationResponsePropertiesStatus(enum.StrEnum):
    """
    Validation status of requested data center and transport.
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
        if self is PreferencesValidationResponsePropertiesStatus.VALID:
            return valid()
        if self is PreferencesValidationResponsePropertiesStatus.INVALID:
            return invalid()
        if self is PreferencesValidationResponsePropertiesStatus.SKIPPED:
            return skipped()
