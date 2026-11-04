

import typing

PaymentInteractionPaymentProtocol = typing.Union[
    typing.Literal["DARWIN_WALLET", "HOSTED_CHECKOUT", "UCP_SPT", "ACP_SPT", "MPP_SPT", "X402"], typing.Any
]
