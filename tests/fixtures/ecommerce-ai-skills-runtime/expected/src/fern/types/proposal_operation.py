

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProposalOperation(enum.StrEnum):
    HUMAN_REVIEW = "human.review"
    SHOPIFY_SYNC_PRODUCTS = "shopify.sync_products"
    AMAZON_SPAPI_IMPORT_REPORT = "amazon_spapi.import_report"
    AMAZON_ADS_CAMPAIGN_UPDATE = "amazon_ads.campaign_update"

    def visit(
        self,
        human_review: typing.Callable[[], T_Result],
        shopify_sync_products: typing.Callable[[], T_Result],
        amazon_spapi_import_report: typing.Callable[[], T_Result],
        amazon_ads_campaign_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProposalOperation.HUMAN_REVIEW:
            return human_review()
        if self is ProposalOperation.SHOPIFY_SYNC_PRODUCTS:
            return shopify_sync_products()
        if self is ProposalOperation.AMAZON_SPAPI_IMPORT_REPORT:
            return amazon_spapi_import_report()
        if self is ProposalOperation.AMAZON_ADS_CAMPAIGN_UPDATE:
            return amazon_ads_campaign_update()
