

import typing

TransferKind = typing.Union[
    typing.Literal["Issuance", "ReceiveBlind", "ReceiveWitness", "Send", "Inflation", "Burn"], typing.Any
]
