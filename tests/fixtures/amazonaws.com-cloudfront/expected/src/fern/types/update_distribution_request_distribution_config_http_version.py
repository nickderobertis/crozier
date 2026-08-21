

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateDistributionRequestDistributionConfigHttpVersion(enum.StrEnum):
    """
    <p>(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don't support HTTP/2 automatically use an earlier HTTP version.</p> <p>For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).</p> <p>In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization." </p>
    """

    HTTP11 = "http1.1"
    HTTP2 = "http2"

    def visit(self, http11: typing.Callable[[], T_Result], http2: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateDistributionRequestDistributionConfigHttpVersion.HTTP11:
            return http11()
        if self is UpdateDistributionRequestDistributionConfigHttpVersion.HTTP2:
            return http2()
