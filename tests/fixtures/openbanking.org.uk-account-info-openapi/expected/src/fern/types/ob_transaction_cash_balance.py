

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_balance_type1code import ObBalanceType1Code
from .ob_credit_debit_code2 import ObCreditDebitCode2
from .ob_transaction_cash_balance_amount import ObTransactionCashBalanceAmount


class ObTransactionCashBalance(UniversalBaseModel):
    """
    Set of elements used to define the balance as a numerical representation of the net increases and decreases in an account after a transaction entry is applied to the account.
    """

    amount: typing_extensions.Annotated[ObTransactionCashBalanceAmount, FieldMetadata(alias="Amount")] = (
        pydantic.Field()
    )
    """
    Amount of money of the cash balance after a transaction entry is applied to the account..
    """

    credit_debit_indicator: typing_extensions.Annotated[ObCreditDebitCode2, FieldMetadata(alias="CreditDebitIndicator")]
    type: typing_extensions.Annotated[ObBalanceType1Code, FieldMetadata(alias="Type")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
