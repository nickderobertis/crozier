

import typing

ProcessCheckoutPaymentType = typing.Union[
    typing.Literal["card", "boleto", "ideal", "blik", "bancontact", "google_pay", "apple_pay"], typing.Any
]
