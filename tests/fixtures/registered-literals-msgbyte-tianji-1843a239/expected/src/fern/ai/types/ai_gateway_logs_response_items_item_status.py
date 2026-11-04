

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AiGatewayLogsResponseItemsItemStatus(enum.StrEnum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AiGatewayLogsResponseItemsItemStatus.PENDING:
            return pending()
        if self is AiGatewayLogsResponseItemsItemStatus.SUCCESS:
            return success()
        if self is AiGatewayLogsResponseItemsItemStatus.FAILED:
            return failed()
