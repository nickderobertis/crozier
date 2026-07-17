

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObBeneficiaryType1Code(enum.StrEnum):
    """
    Specifies the Beneficiary Type.
    """

    TRUSTED = "Trusted"
    ORDINARY = "Ordinary"

    def visit(self, trusted: typing.Callable[[], T_Result], ordinary: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObBeneficiaryType1Code.TRUSTED:
            return trusted()
        if self is ObBeneficiaryType1Code.ORDINARY:
            return ordinary()
