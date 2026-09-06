

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListProductsResponseItemsItemProductFieldDataEcProductType(enum.StrEnum):
    """
    <a href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product types.</a> Enums reflect the following values in order: Physical, Digital, Service, Advanced"
    """

    FF42FEE0113744F693A764E3431A9CC2 = "ff42fee0113744f693a764e3431a9cc2"
    F22027DB68002190AEF89A4A2B7AC8A1 = "f22027db68002190aef89a4a2b7ac8a1"
    C599E43B1A1C34D5A323AEDF75D3ADF6 = "c599e43b1a1c34d5a323aedf75d3adf6"
    B6CCC1830DB4B1BABEB06A9AC5F6DD76 = "b6ccc1830db4b1babeb06a9ac5f6dd76"

    def visit(
        self,
        ff42fee0113744f693a764e3431a9cc2: typing.Callable[[], T_Result],
        f22027db68002190aef89a4a2b7ac8a1: typing.Callable[[], T_Result],
        c599e43b1a1c34d5a323aedf75d3adf6: typing.Callable[[], T_Result],
        b6ccc1830db4b1babeb06a9ac5f6dd76: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListProductsResponseItemsItemProductFieldDataEcProductType.FF42FEE0113744F693A764E3431A9CC2:
            return ff42fee0113744f693a764e3431a9cc2()
        if self is ListProductsResponseItemsItemProductFieldDataEcProductType.F22027DB68002190AEF89A4A2B7AC8A1:
            return f22027db68002190aef89a4a2b7ac8a1()
        if self is ListProductsResponseItemsItemProductFieldDataEcProductType.C599E43B1A1C34D5A323AEDF75D3ADF6:
            return c599e43b1a1c34d5a323aedf75d3adf6()
        if self is ListProductsResponseItemsItemProductFieldDataEcProductType.B6CCC1830DB4B1BABEB06A9AC5F6DD76:
            return b6ccc1830db4b1babeb06a9ac5f6dd76()
