

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsApiProductVersionFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    API_PRODUCT_VERSION = "api_product_version"

    def visit(self, api_product_version: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsApiProductVersionFilterByFieldOneField.API_PRODUCT_VERSION:
            return api_product_version()
