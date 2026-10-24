

import typing

ProposalOperation = typing.Union[
    typing.Literal["human.review", "shopify.sync_products", "amazon_spapi.import_report", "amazon_ads.campaign_update"],
    typing.Any,
]
