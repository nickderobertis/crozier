

import typing

TopDimensionsReportsRequestDimension = typing.Union[
    typing.Literal[
        "country",
        "region",
        "deviceType",
        "os",
        "browser",
        "language",
        "locale",
        "referrer",
        "trafficSource",
        "utmCampaign",
        "utmContent",
        "utmMedium",
        "utmSource",
        "utmTerm",
        "audienceIds",
    ],
    typing.Any,
]
