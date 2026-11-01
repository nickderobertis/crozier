

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UploadMode(enum.StrEnum):
    """
    The transport that an upload uses.
    """

    SERVICE_PROXIED = "service_proxied"
    DIRECT_PUT = "direct_put"
    DIRECT_MULTIPART = "direct_multipart"

    def visit(
        self,
        service_proxied: typing.Callable[[], T_Result],
        direct_put: typing.Callable[[], T_Result],
        direct_multipart: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UploadMode.SERVICE_PROXIED:
            return service_proxied()
        if self is UploadMode.DIRECT_PUT:
            return direct_put()
        if self is UploadMode.DIRECT_MULTIPART:
            return direct_multipart()
