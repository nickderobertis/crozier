

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .description1 import Description1
from .ob_active_or_historic_currency_and_amount6 import ObActiveOrHistoricCurrencyAndAmount6
from .ob_credit_debit_code0 import ObCreditDebitCode0
from .ob_external_statement_fee_frequency1code import ObExternalStatementFeeFrequency1Code
from .ob_external_statement_fee_rate_type1code import ObExternalStatementFeeRateType1Code
from .ob_external_statement_fee_type1code import ObExternalStatementFeeType1Code
from .ob_rate10 import ObRate10


class ObStatement2StatementFeeItem(UniversalBaseModel):
    """
    Set of elements used to provide details of a fee for the statement resource.
    """

    amount: typing_extensions.Annotated[
        ObActiveOrHistoricCurrencyAndAmount6, FieldMetadata(alias="Amount"), pydantic.Field(alias="Amount")
    ]
    credit_debit_indicator: typing_extensions.Annotated[
        ObCreditDebitCode0, FieldMetadata(alias="CreditDebitIndicator"), pydantic.Field(alias="CreditDebitIndicator")
    ]
    description: typing_extensions.Annotated[
        typing.Optional[Description1], FieldMetadata(alias="Description"), pydantic.Field(alias="Description")
    ] = None
    frequency: typing_extensions.Annotated[
        typing.Optional[ObExternalStatementFeeFrequency1Code],
        FieldMetadata(alias="Frequency"),
        pydantic.Field(alias="Frequency"),
    ] = None
    rate: typing_extensions.Annotated[
        typing.Optional[ObRate10], FieldMetadata(alias="Rate"), pydantic.Field(alias="Rate")
    ] = None
    rate_type: typing_extensions.Annotated[
        typing.Optional[ObExternalStatementFeeRateType1Code],
        FieldMetadata(alias="RateType"),
        pydantic.Field(alias="RateType"),
    ] = None
    type: typing_extensions.Annotated[
        ObExternalStatementFeeType1Code, FieldMetadata(alias="Type"), pydantic.Field(alias="Type")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
