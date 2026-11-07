

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsGatewayServiceFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    GATEWAY_SERVICE = "gateway_service"

    def visit(self, gateway_service: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsGatewayServiceFilterByFieldOneField.GATEWAY_SERVICE:
            return gateway_service()
