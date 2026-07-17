

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .address_line import AddressLine
from .booking_date_time import BookingDateTime
from .ob_active_or_historic_currency_and_amount9 import ObActiveOrHistoricCurrencyAndAmount9
from .ob_active_or_historic_currency_and_amount10 import ObActiveOrHistoricCurrencyAndAmount10
from .ob_bank_transaction_code_structure1 import ObBankTransactionCodeStructure1
from .ob_credit_debit_code1 import ObCreditDebitCode1
from .ob_currency_exchange5 import ObCurrencyExchange5
from .ob_entry_status1code import ObEntryStatus1Code
from .ob_supplementary_data1 import ObSupplementaryData1
from .ob_transaction_card_instrument1 import ObTransactionCardInstrument1
from .ob_transaction_mutability1code import ObTransactionMutability1Code
from .proprietary_bank_transaction_code_structure1 import ProprietaryBankTransactionCodeStructure1
from .statement_reference import StatementReference
from .transaction_id import TransactionId
from .transaction_reference import TransactionReference
from .value_date_time import ValueDateTime


class ObTransaction6Basic(UniversalBaseModel):
    """
    Provides further details on an entry in the report.
    """

    account_id: typing_extensions.Annotated[
        AccountId, FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ]
    address_line: typing_extensions.Annotated[
        typing.Optional[AddressLine], FieldMetadata(alias="AddressLine"), pydantic.Field(alias="AddressLine")
    ] = None
    amount: typing_extensions.Annotated[
        ObActiveOrHistoricCurrencyAndAmount9, FieldMetadata(alias="Amount"), pydantic.Field(alias="Amount")
    ]
    bank_transaction_code: typing_extensions.Annotated[
        typing.Optional[ObBankTransactionCodeStructure1],
        FieldMetadata(alias="BankTransactionCode"),
        pydantic.Field(alias="BankTransactionCode"),
    ] = None
    booking_date_time: typing_extensions.Annotated[
        BookingDateTime, FieldMetadata(alias="BookingDateTime"), pydantic.Field(alias="BookingDateTime")
    ]
    card_instrument: typing_extensions.Annotated[
        typing.Optional[ObTransactionCardInstrument1],
        FieldMetadata(alias="CardInstrument"),
        pydantic.Field(alias="CardInstrument"),
    ] = None
    charge_amount: typing_extensions.Annotated[
        typing.Optional[ObActiveOrHistoricCurrencyAndAmount10],
        FieldMetadata(alias="ChargeAmount"),
        pydantic.Field(alias="ChargeAmount"),
    ] = None
    credit_debit_indicator: typing_extensions.Annotated[
        ObCreditDebitCode1, FieldMetadata(alias="CreditDebitIndicator"), pydantic.Field(alias="CreditDebitIndicator")
    ]
    currency_exchange: typing_extensions.Annotated[
        typing.Optional[ObCurrencyExchange5],
        FieldMetadata(alias="CurrencyExchange"),
        pydantic.Field(alias="CurrencyExchange"),
    ] = None
    proprietary_bank_transaction_code: typing_extensions.Annotated[
        typing.Optional[ProprietaryBankTransactionCodeStructure1],
        FieldMetadata(alias="ProprietaryBankTransactionCode"),
        pydantic.Field(alias="ProprietaryBankTransactionCode"),
    ] = None
    statement_reference: typing_extensions.Annotated[
        typing.Optional[typing.List[StatementReference]],
        FieldMetadata(alias="StatementReference"),
        pydantic.Field(alias="StatementReference"),
    ] = None
    status: typing_extensions.Annotated[
        ObEntryStatus1Code, FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ]
    supplementary_data: typing_extensions.Annotated[
        typing.Optional[ObSupplementaryData1],
        FieldMetadata(alias="SupplementaryData"),
        pydantic.Field(alias="SupplementaryData"),
    ] = None
    transaction_id: typing_extensions.Annotated[
        typing.Optional[TransactionId], FieldMetadata(alias="TransactionId"), pydantic.Field(alias="TransactionId")
    ] = None
    transaction_mutability: typing_extensions.Annotated[
        typing.Optional[ObTransactionMutability1Code],
        FieldMetadata(alias="TransactionMutability"),
        pydantic.Field(alias="TransactionMutability"),
    ] = None
    transaction_reference: typing_extensions.Annotated[
        typing.Optional[TransactionReference],
        FieldMetadata(alias="TransactionReference"),
        pydantic.Field(alias="TransactionReference"),
    ] = None
    value_date_time: typing_extensions.Annotated[
        typing.Optional[ValueDateTime], FieldMetadata(alias="ValueDateTime"), pydantic.Field(alias="ValueDateTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
