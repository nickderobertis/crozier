

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AddressValidationPropertiesValidationStatus(enum.StrEnum):
    """
    The address validation status.
    """

    VALID = "Valid"
    INVALID = "Invalid"
    AMBIGUOUS = "Ambiguous"

    def visit(
        self,
        valid: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
        ambiguous: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressValidationPropertiesValidationStatus.VALID:
            return valid()
        if self is AddressValidationPropertiesValidationStatus.INVALID:
            return invalid()
        if self is AddressValidationPropertiesValidationStatus.AMBIGUOUS:
            return ambiguous()
