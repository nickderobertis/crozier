

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_active_or_historic_currency_and_amount8 import ObActiveOrHistoricCurrencyAndAmount8
from .ob_credit_debit_code0 import ObCreditDebitCode0
from .ob_external_statement_amount_type1code import ObExternalStatementAmountType1Code


class ObStatement2DetailStatementAmountItem(UniversalBaseModel):
    """
    Set of elements used to provide details of a generic amount for the statement resource.
    """

    amount: typing_extensions.Annotated[
        ObActiveOrHistoricCurrencyAndAmount8, FieldMetadata(alias="Amount"), pydantic.Field(alias="Amount")
    ]
    credit_debit_indicator: typing_extensions.Annotated[
        ObCreditDebitCode0, FieldMetadata(alias="CreditDebitIndicator"), pydantic.Field(alias="CreditDebitIndicator")
    ]
    type: typing_extensions.Annotated[
        ObExternalStatementAmountType1Code, FieldMetadata(alias="Type"), pydantic.Field(alias="Type")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
