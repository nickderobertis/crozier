

import typing

from .get_quote_by_id_quote_response_data_deposit_option_type_one import (
    GetQuoteByIdQuoteResponseDataDepositOptionTypeOne,
)
from .get_quote_by_id_quote_response_data_deposit_option_type_zero import (
    GetQuoteByIdQuoteResponseDataDepositOptionTypeZero,
)

GetQuoteByIdQuoteResponseDataDepositOptionType = typing.Union[
    GetQuoteByIdQuoteResponseDataDepositOptionTypeZero, GetQuoteByIdQuoteResponseDataDepositOptionTypeOne
]
