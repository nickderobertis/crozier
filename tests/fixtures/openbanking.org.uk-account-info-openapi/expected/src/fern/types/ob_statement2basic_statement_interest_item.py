

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .description2 import Description2
from .ob_active_or_historic_currency_and_amount7 import ObActiveOrHistoricCurrencyAndAmount7
from .ob_credit_debit_code0 import ObCreditDebitCode0
from .ob_external_statement_interest_frequency1code import ObExternalStatementInterestFrequency1Code
from .ob_external_statement_interest_rate_type1code import ObExternalStatementInterestRateType1Code
from .ob_external_statement_interest_type1code import ObExternalStatementInterestType1Code
from .ob_rate11 import ObRate11


class ObStatement2BasicStatementInterestItem(UniversalBaseModel):
    """
    Set of elements used to provide details of a generic interest amount related to the statement resource.
    """

    amount: typing_extensions.Annotated[
        ObActiveOrHistoricCurrencyAndAmount7, FieldMetadata(alias="Amount"), pydantic.Field(alias="Amount")
    ]
    credit_debit_indicator: typing_extensions.Annotated[
        ObCreditDebitCode0, FieldMetadata(alias="CreditDebitIndicator"), pydantic.Field(alias="CreditDebitIndicator")
    ]
    description: typing_extensions.Annotated[
        typing.Optional[Description2], FieldMetadata(alias="Description"), pydantic.Field(alias="Description")
    ] = None
    frequency: typing_extensions.Annotated[
        typing.Optional[ObExternalStatementInterestFrequency1Code],
        FieldMetadata(alias="Frequency"),
        pydantic.Field(alias="Frequency"),
    ] = None
    rate: typing_extensions.Annotated[
        typing.Optional[ObRate11], FieldMetadata(alias="Rate"), pydantic.Field(alias="Rate")
    ] = None
    rate_type: typing_extensions.Annotated[
        typing.Optional[ObExternalStatementInterestRateType1Code],
        FieldMetadata(alias="RateType"),
        pydantic.Field(alias="RateType"),
    ] = None
    type: typing_extensions.Annotated[
        ObExternalStatementInterestType1Code, FieldMetadata(alias="Type"), pydantic.Field(alias="Type")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
