

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DistributionSummaryHttpVersion(enum.StrEnum):
    """
    Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is <code>http2</code>. Viewers that don't support <code>HTTP/2</code> will automatically use an earlier version.
    """

    HTTP11 = "http1.1"
    HTTP2 = "http2"

    def visit(self, http11: typing.Callable[[], T_Result], http2: typing.Callable[[], T_Result]) -> T_Result:
        if self is DistributionSummaryHttpVersion.HTTP11:
            return http11()
        if self is DistributionSummaryHttpVersion.HTTP2:
            return http2()
