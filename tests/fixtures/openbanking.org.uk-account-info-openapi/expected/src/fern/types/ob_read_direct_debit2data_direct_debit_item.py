

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .direct_debit_id import DirectDebitId
from .mandate_identification import MandateIdentification
from .name2 import Name2
from .ob_active_or_historic_currency_and_amount0 import ObActiveOrHistoricCurrencyAndAmount0
from .ob_external_direct_debit_status1code import ObExternalDirectDebitStatus1Code
from .previous_payment_date_time import PreviousPaymentDateTime


class ObReadDirectDebit2DataDirectDebitItem(UniversalBaseModel):
    """
    Account to or from which a cash entry is made.
    """

    account_id: typing_extensions.Annotated[
        AccountId, FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ]
    direct_debit_id: typing_extensions.Annotated[
        typing.Optional[DirectDebitId], FieldMetadata(alias="DirectDebitId"), pydantic.Field(alias="DirectDebitId")
    ] = None
    direct_debit_status_code: typing_extensions.Annotated[
        typing.Optional[ObExternalDirectDebitStatus1Code],
        FieldMetadata(alias="DirectDebitStatusCode"),
        pydantic.Field(alias="DirectDebitStatusCode"),
    ] = None
    frequency: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Frequency"),
        pydantic.Field(
            alias="Frequency",
            description="Regularity with which direct debit instructions are to be created and processed.",
        ),
    ] = None
    """
    Regularity with which direct debit instructions are to be created and processed.
    """

    mandate_identification: typing_extensions.Annotated[
        MandateIdentification,
        FieldMetadata(alias="MandateIdentification"),
        pydantic.Field(alias="MandateIdentification"),
    ]
    name: typing_extensions.Annotated[Name2, FieldMetadata(alias="Name"), pydantic.Field(alias="Name")]
    previous_payment_amount: typing_extensions.Annotated[
        typing.Optional[ObActiveOrHistoricCurrencyAndAmount0],
        FieldMetadata(alias="PreviousPaymentAmount"),
        pydantic.Field(alias="PreviousPaymentAmount"),
    ] = None
    previous_payment_date_time: typing_extensions.Annotated[
        typing.Optional[PreviousPaymentDateTime],
        FieldMetadata(alias="PreviousPaymentDateTime"),
        pydantic.Field(alias="PreviousPaymentDateTime"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
