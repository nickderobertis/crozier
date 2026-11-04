

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebsiteGetLighthouseReportResponseItemsItemStatus(enum.StrEnum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebsiteGetLighthouseReportResponseItemsItemStatus.PENDING:
            return pending()
        if self is WebsiteGetLighthouseReportResponseItemsItemStatus.SUCCESS:
            return success()
        if self is WebsiteGetLighthouseReportResponseItemsItemStatus.FAILED:
            return failed()
