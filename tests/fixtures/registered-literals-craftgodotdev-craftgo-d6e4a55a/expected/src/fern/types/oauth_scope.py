

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    CATALOG_READ = "catalog:read"
    """
    Read catalog data
    """

    ORDERS_WRITE = "orders:write"
    """
    Create and modify orders
    """

    def visit(
        self, catalog_read: typing.Callable[[], T_Result], orders_write: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is OauthScope.CATALOG_READ:
            return catalog_read()
        if self is OauthScope.ORDERS_WRITE:
            return orders_write()
