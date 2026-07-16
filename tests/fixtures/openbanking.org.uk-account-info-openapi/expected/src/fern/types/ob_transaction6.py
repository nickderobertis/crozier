

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
from .ob_branch_and_financial_institution_identification61 import ObBranchAndFinancialInstitutionIdentification61
from .ob_branch_and_financial_institution_identification62 import ObBranchAndFinancialInstitutionIdentification62
from .ob_cash_account60 import ObCashAccount60
from .ob_cash_account61 import ObCashAccount61
from .ob_credit_debit_code1 import ObCreditDebitCode1
from .ob_currency_exchange5 import ObCurrencyExchange5
from .ob_entry_status1code import ObEntryStatus1Code
from .ob_merchant_details1 import ObMerchantDetails1
from .ob_supplementary_data1 import ObSupplementaryData1
from .ob_transaction_card_instrument1 import ObTransactionCardInstrument1
from .ob_transaction_cash_balance import ObTransactionCashBalance
from .ob_transaction_mutability1code import ObTransactionMutability1Code
from .proprietary_bank_transaction_code_structure1 import ProprietaryBankTransactionCodeStructure1
from .statement_reference import StatementReference
from .transaction_id import TransactionId
from .transaction_information import TransactionInformation
from .transaction_reference import TransactionReference
from .value_date_time import ValueDateTime


class ObTransaction6(UniversalBaseModel):
    """
    Provides further details on an entry in the report.
    """

    account_id: typing_extensions.Annotated[AccountId, FieldMetadata(alias="AccountId")]
    address_line: typing_extensions.Annotated[typing.Optional[AddressLine], FieldMetadata(alias="AddressLine")] = None
    amount: typing_extensions.Annotated[ObActiveOrHistoricCurrencyAndAmount9, FieldMetadata(alias="Amount")]
    balance: typing_extensions.Annotated[typing.Optional[ObTransactionCashBalance], FieldMetadata(alias="Balance")] = (
        None
    )
    bank_transaction_code: typing_extensions.Annotated[
        typing.Optional[ObBankTransactionCodeStructure1], FieldMetadata(alias="BankTransactionCode")
    ] = None
    booking_date_time: typing_extensions.Annotated[BookingDateTime, FieldMetadata(alias="BookingDateTime")]
    card_instrument: typing_extensions.Annotated[
        typing.Optional[ObTransactionCardInstrument1], FieldMetadata(alias="CardInstrument")
    ] = None
    charge_amount: typing_extensions.Annotated[
        typing.Optional[ObActiveOrHistoricCurrencyAndAmount10], FieldMetadata(alias="ChargeAmount")
    ] = None
    credit_debit_indicator: typing_extensions.Annotated[ObCreditDebitCode1, FieldMetadata(alias="CreditDebitIndicator")]
    creditor_account: typing_extensions.Annotated[
        typing.Optional[ObCashAccount60], FieldMetadata(alias="CreditorAccount")
    ] = None
    creditor_agent: typing_extensions.Annotated[
        typing.Optional[ObBranchAndFinancialInstitutionIdentification61], FieldMetadata(alias="CreditorAgent")
    ] = None
    currency_exchange: typing_extensions.Annotated[
        typing.Optional[ObCurrencyExchange5], FieldMetadata(alias="CurrencyExchange")
    ] = None
    debtor_account: typing_extensions.Annotated[
        typing.Optional[ObCashAccount61], FieldMetadata(alias="DebtorAccount")
    ] = None
    debtor_agent: typing_extensions.Annotated[
        typing.Optional[ObBranchAndFinancialInstitutionIdentification62], FieldMetadata(alias="DebtorAgent")
    ] = None
    merchant_details: typing_extensions.Annotated[
        typing.Optional[ObMerchantDetails1], FieldMetadata(alias="MerchantDetails")
    ] = None
    proprietary_bank_transaction_code: typing_extensions.Annotated[
        typing.Optional[ProprietaryBankTransactionCodeStructure1], FieldMetadata(alias="ProprietaryBankTransactionCode")
    ] = None
    statement_reference: typing_extensions.Annotated[
        typing.Optional[typing.List[StatementReference]], FieldMetadata(alias="StatementReference")
    ] = None
    status: typing_extensions.Annotated[ObEntryStatus1Code, FieldMetadata(alias="Status")]
    supplementary_data: typing_extensions.Annotated[
        typing.Optional[ObSupplementaryData1], FieldMetadata(alias="SupplementaryData")
    ] = None
    transaction_id: typing_extensions.Annotated[
        typing.Optional[TransactionId], FieldMetadata(alias="TransactionId")
    ] = None
    transaction_information: typing_extensions.Annotated[
        typing.Optional[TransactionInformation], FieldMetadata(alias="TransactionInformation")
    ] = None
    transaction_mutability: typing_extensions.Annotated[
        typing.Optional[ObTransactionMutability1Code], FieldMetadata(alias="TransactionMutability")
    ] = None
    transaction_reference: typing_extensions.Annotated[
        typing.Optional[TransactionReference], FieldMetadata(alias="TransactionReference")
    ] = None
    value_date_time: typing_extensions.Annotated[
        typing.Optional[ValueDateTime], FieldMetadata(alias="ValueDateTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
