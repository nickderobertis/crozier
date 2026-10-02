

import typing

OrderFulfillmentState = typing.Union[
    typing.Literal["PROPOSED", "RESERVED", "PREPARED", "COMPLETED", "CANCELED", "FAILED"], typing.Any
]
