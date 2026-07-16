

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TenderCardDetailsStatus(str, enum.Enum):
    """
    Indicates the card transaction's current status.
    """

    AUTHORIZED = "AUTHORIZED"
    CAPTURED = "CAPTURED"
    VOIDED = "VOIDED"
    FAILED = "FAILED"

    def visit(
        self,
        authorized: typing.Callable[[], T_Result],
        captured: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TenderCardDetailsStatus.AUTHORIZED:
            return authorized()
        if self is TenderCardDetailsStatus.CAPTURED:
            return captured()
        if self is TenderCardDetailsStatus.VOIDED:
            return voided()
        if self is TenderCardDetailsStatus.FAILED:
            return failed()
