

import typing

WebsiteMetricsRequestType = typing.Union[
    typing.Literal[
        "url",
        "language",
        "referrer",
        "title",
        "browser",
        "os",
        "device",
        "country",
        "event",
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_term",
        "utm_content",
    ],
    typing.Any,
]
