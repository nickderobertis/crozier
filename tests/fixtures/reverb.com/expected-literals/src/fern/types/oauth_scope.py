

import typing

OauthScope = typing.Union[
    typing.Literal[
        "public",
        "read_feedback",
        "read_listings",
        "read_lists",
        "read_messages",
        "read_offers",
        "read_orders",
        "read_payouts",
        "read_profile",
        "write_feedback",
        "write_listings",
        "write_listings_for_others",
        "write_lists",
        "write_messages",
        "write_offers",
        "write_orders",
        "write_profile",
        "write_reviews",
    ],
    typing.Any,
]
