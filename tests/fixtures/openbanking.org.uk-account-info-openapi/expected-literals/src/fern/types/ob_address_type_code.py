

import typing

ObAddressTypeCode = typing.Union[
    typing.Literal["Business", "Correspondence", "DeliveryTo", "MailTo", "POBox", "Postal", "Residential", "Statement"],
    typing.Any,
]
