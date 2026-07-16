

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .final_payment_date_time import FinalPaymentDateTime
from .first_payment_date_time import FirstPaymentDateTime
from .frequency1 import Frequency1
from .last_payment_date_time import LastPaymentDateTime
from .next_payment_date_time import NextPaymentDateTime
from .number_of_payments import NumberOfPayments
from .ob_active_or_historic_currency_and_amount2 import ObActiveOrHistoricCurrencyAndAmount2
from .ob_active_or_historic_currency_and_amount3 import ObActiveOrHistoricCurrencyAndAmount3
from .ob_active_or_historic_currency_and_amount4 import ObActiveOrHistoricCurrencyAndAmount4
from .ob_active_or_historic_currency_and_amount11 import ObActiveOrHistoricCurrencyAndAmount11
from .ob_branch_and_financial_institution_identification51 import ObBranchAndFinancialInstitutionIdentification51
from .ob_cash_account51 import ObCashAccount51
from .ob_external_standing_order_status1code import ObExternalStandingOrderStatus1Code
from .ob_supplementary_data1 import ObSupplementaryData1
from .reference import Reference
from .standing_order_id import StandingOrderId


class ObStandingOrder6Detail(UniversalBaseModel):
    account_id: typing_extensions.Annotated[
        AccountId, FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ]
    creditor_account: typing_extensions.Annotated[
        ObCashAccount51, FieldMetadata(alias="CreditorAccount"), pydantic.Field(alias="CreditorAccount")
    ]
    creditor_agent: typing_extensions.Annotated[
        typing.Optional[ObBranchAndFinancialInstitutionIdentification51],
        FieldMetadata(alias="CreditorAgent"),
        pydantic.Field(alias="CreditorAgent"),
    ] = None
    final_payment_amount: typing_extensions.Annotated[
        typing.Optional[ObActiveOrHistoricCurrencyAndAmount4],
        FieldMetadata(alias="FinalPaymentAmount"),
        pydantic.Field(alias="FinalPaymentAmount"),
    ] = None
    final_payment_date_time: typing_extensions.Annotated[
        typing.Optional[FinalPaymentDateTime],
        FieldMetadata(alias="FinalPaymentDateTime"),
        pydantic.Field(alias="FinalPaymentDateTime"),
    ] = None
    first_payment_amount: typing_extensions.Annotated[
        typing.Optional[ObActiveOrHistoricCurrencyAndAmount2],
        FieldMetadata(alias="FirstPaymentAmount"),
        pydantic.Field(alias="FirstPaymentAmount"),
    ] = None
    first_payment_date_time: typing_extensions.Annotated[
        typing.Optional[FirstPaymentDateTime],
        FieldMetadata(alias="FirstPaymentDateTime"),
        pydantic.Field(alias="FirstPaymentDateTime"),
    ] = None
    frequency: typing_extensions.Annotated[
        Frequency1, FieldMetadata(alias="Frequency"), pydantic.Field(alias="Frequency")
    ]
    last_payment_amount: typing_extensions.Annotated[
        typing.Optional[ObActiveOrHistoricCurrencyAndAmount11],
        FieldMetadata(alias="LastPaymentAmount"),
        pydantic.Field(alias="LastPaymentAmount"),
    ] = None
    last_payment_date_time: typing_extensions.Annotated[
        typing.Optional[LastPaymentDateTime],
        FieldMetadata(alias="LastPaymentDateTime"),
        pydantic.Field(alias="LastPaymentDateTime"),
    ] = None
    next_payment_amount: typing_extensions.Annotated[
        typing.Optional[ObActiveOrHistoricCurrencyAndAmount3],
        FieldMetadata(alias="NextPaymentAmount"),
        pydantic.Field(alias="NextPaymentAmount"),
    ] = None
    next_payment_date_time: typing_extensions.Annotated[
        typing.Optional[NextPaymentDateTime],
        FieldMetadata(alias="NextPaymentDateTime"),
        pydantic.Field(alias="NextPaymentDateTime"),
    ] = None
    number_of_payments: typing_extensions.Annotated[
        typing.Optional[NumberOfPayments],
        FieldMetadata(alias="NumberOfPayments"),
        pydantic.Field(alias="NumberOfPayments"),
    ] = None
    reference: typing_extensions.Annotated[
        typing.Optional[Reference], FieldMetadata(alias="Reference"), pydantic.Field(alias="Reference")
    ] = None
    standing_order_id: typing_extensions.Annotated[
        typing.Optional[StandingOrderId],
        FieldMetadata(alias="StandingOrderId"),
        pydantic.Field(alias="StandingOrderId"),
    ] = None
    standing_order_status_code: typing_extensions.Annotated[
        typing.Optional[ObExternalStandingOrderStatus1Code],
        FieldMetadata(alias="StandingOrderStatusCode"),
        pydantic.Field(alias="StandingOrderStatusCode"),
    ] = None
    supplementary_data: typing_extensions.Annotated[
        typing.Optional[ObSupplementaryData1],
        FieldMetadata(alias="SupplementaryData"),
        pydantic.Field(alias="SupplementaryData"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
