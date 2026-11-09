

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsApiProductFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    API_PRODUCT = "api_product"

    def visit(self, api_product: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsApiProductFilterByFieldOneField.API_PRODUCT:
            return api_product()
