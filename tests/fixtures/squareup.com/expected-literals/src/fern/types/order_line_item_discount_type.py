

import typing

OrderLineItemDiscountType = typing.Union[
    typing.Literal["UNKNOWN_DISCOUNT", "FIXED_PERCENTAGE", "FIXED_AMOUNT", "VARIABLE_PERCENTAGE", "VARIABLE_AMOUNT"],
    typing.Any,
]
