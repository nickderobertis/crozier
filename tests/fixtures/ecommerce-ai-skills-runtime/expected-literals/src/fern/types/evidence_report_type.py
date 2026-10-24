

import typing

EvidenceReportType = typing.Union[
    typing.Literal[
        "amazon_business_report",
        "amazon_ads_search_term",
        "amazon_fba_inventory",
        "amazon_returns",
        "amazon_listing",
        "platform_generic",
    ],
    typing.Any,
]
