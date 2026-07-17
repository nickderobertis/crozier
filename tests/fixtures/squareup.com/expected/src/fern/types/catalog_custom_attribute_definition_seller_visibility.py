

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogCustomAttributeDefinitionSellerVisibility(enum.StrEnum):
    """
    Defines the visibility of a custom attribute to sellers in Square
    client applications, Square APIs or in Square UIs (including Square Point
    of Sale applications and Square Dashboard).
    """

    SELLER_VISIBILITY_HIDDEN = "SELLER_VISIBILITY_HIDDEN"
    SELLER_VISIBILITY_READ_WRITE_VALUES = "SELLER_VISIBILITY_READ_WRITE_VALUES"

    def visit(
        self,
        seller_visibility_hidden: typing.Callable[[], T_Result],
        seller_visibility_read_write_values: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogCustomAttributeDefinitionSellerVisibility.SELLER_VISIBILITY_HIDDEN:
            return seller_visibility_hidden()
        if self is CatalogCustomAttributeDefinitionSellerVisibility.SELLER_VISIBILITY_READ_WRITE_VALUES:
            return seller_visibility_read_write_values()
