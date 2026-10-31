

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EtcdKeyRotationStatusFailureReason(enum.StrEnum):
    """
    A bounded reason without keys, arbitrary error strings, or secret identifiers.
    """

    OPERATION_FAILED = "operation_failed"
    CANCELED = "canceled"

    def visit(
        self, operation_failed: typing.Callable[[], T_Result], canceled: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is EtcdKeyRotationStatusFailureReason.OPERATION_FAILED:
            return operation_failed()
        if self is EtcdKeyRotationStatusFailureReason.CANCELED:
            return canceled()
