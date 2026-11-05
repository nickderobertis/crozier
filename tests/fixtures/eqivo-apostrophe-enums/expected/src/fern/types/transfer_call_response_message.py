

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferCallResponseMessage(enum.StrEnum):
    """
    Response message
    """

    TRANSFER_CALL_EXECUTED = "Transfer Call Executed"
    CALL_UUID_PARAMETER_MUST_BE_PRESENT = "CallUUID Parameter must be present"
    URL_PARAMETER_MUST_BE_PRESENT = "Url Parameter must be present"
    URL_IS_NOT_VALID = "Url is not Valid"
    TRANSFER_CALL_FAILED_CALL_NOT_FOUND = "Transfer Call Failed -- Call not found"
    TRANSFER_CALL_FAILED = "Transfer Call Failed"

    def visit(
        self,
        transfer_call_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_must_be_present: typing.Callable[[], T_Result],
        url_parameter_must_be_present: typing.Callable[[], T_Result],
        url_is_not_valid: typing.Callable[[], T_Result],
        transfer_call_failed_call_not_found: typing.Callable[[], T_Result],
        transfer_call_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferCallResponseMessage.TRANSFER_CALL_EXECUTED:
            return transfer_call_executed()
        if self is TransferCallResponseMessage.CALL_UUID_PARAMETER_MUST_BE_PRESENT:
            return call_uuid_parameter_must_be_present()
        if self is TransferCallResponseMessage.URL_PARAMETER_MUST_BE_PRESENT:
            return url_parameter_must_be_present()
        if self is TransferCallResponseMessage.URL_IS_NOT_VALID:
            return url_is_not_valid()
        if self is TransferCallResponseMessage.TRANSFER_CALL_FAILED_CALL_NOT_FOUND:
            return transfer_call_failed_call_not_found()
        if self is TransferCallResponseMessage.TRANSFER_CALL_FAILED:
            return transfer_call_failed()
