

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtelExporterConfigProtocol(enum.StrEnum):
    """
    The transport protocol
    Possible protocol to use with OTLP. Currently, only http/protobuf is supported.
    """

    HTTP_PROTOBUF = "http/protobuf"

    def visit(self, http_protobuf: typing.Callable[[], T_Result]) -> T_Result:
        if self is OtelExporterConfigProtocol.HTTP_PROTOBUF:
            return http_protobuf()
