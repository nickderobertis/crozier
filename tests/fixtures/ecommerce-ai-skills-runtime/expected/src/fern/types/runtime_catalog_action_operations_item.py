

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuntimeCatalogActionOperationsItem(enum.StrEnum):
    SHOPIFY_SYNC_PRODUCTS = "shopify.sync_products"
    AMAZON_SPAPI_IMPORT_REPORT = "amazon_spapi.import_report"

    def visit(
        self,
        shopify_sync_products: typing.Callable[[], T_Result],
        amazon_spapi_import_report: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuntimeCatalogActionOperationsItem.SHOPIFY_SYNC_PRODUCTS:
            return shopify_sync_products()
        if self is RuntimeCatalogActionOperationsItem.AMAZON_SPAPI_IMPORT_REPORT:
            return amazon_spapi_import_report()
