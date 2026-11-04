

import typing

FinancialPayoutType = typing.Union[
    typing.Literal["PAYOUT", "CHARGE_BACK_DEDUCTION", "REFUND_DEDUCTION", "DD_RETURN_DEDUCTION", "BALANCE_DEDUCTION"],
    typing.Any,
]
