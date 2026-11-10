

import typing

VerificationStatus = typing.Union[
    typing.Literal["VERIFIED", "UNVERIFIED", "NEEDS_INFO", "UNABLE_TO_VERIFY", "UNKNOWN"], typing.Any
]
