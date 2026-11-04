

import typing

TransactionFullVerificationMethod = typing.Union[
    typing.Literal["none", "signature", "offline PIN", "online PIN", "offline PIN + signature", "na"], typing.Any
]
