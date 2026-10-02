

import typing

LandingEventRequestCta = typing.Union[
    typing.Literal[
        "hero-waitlist",
        "hero-register",
        "nav-register",
        "nav-login",
        "pricing-free-register",
        "pricing-pro-waitlist",
        "waitlist-success-register",
    ],
    typing.Any,
]
