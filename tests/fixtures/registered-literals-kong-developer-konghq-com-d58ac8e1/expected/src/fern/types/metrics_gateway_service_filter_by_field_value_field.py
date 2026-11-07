

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsGatewayServiceFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    GATEWAY_SERVICE = "gateway_service"

    def visit(self, gateway_service: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsGatewayServiceFilterByFieldValueField.GATEWAY_SERVICE:
            return gateway_service()
