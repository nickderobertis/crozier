

import typing

SiacoinOriginSource = typing.Union[
    typing.Literal["transaction", "minerPayout", "contractPayout", "siafundClaim", "foundationSubsidy", "unknown"],
    typing.Any,
]
