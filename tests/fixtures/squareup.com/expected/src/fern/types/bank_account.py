

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BankAccount(UniversalBaseModel):
    """
    Represents a bank account. For more information about
    linking a bank account to a Square account, see
    [Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api).
    """

    account_number_suffix: str = pydantic.Field()
    """
    The last few digits of the account number.
    """

    account_type: str = pydantic.Field()
    """
    The financial purpose of the associated bank account.
    """

    bank_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Read only. Name of actual financial institution. 
    For example "Bank of America".
    """

    country: str = pydantic.Field()
    """
    The ISO 3166 Alpha-2 country code where the bank account is based.
    """

    creditable: bool = pydantic.Field()
    """
    Indicates whether it is possible for Square to send money to this bank account.
    """

    currency: str = pydantic.Field()
    """
    The 3-character ISO 4217 currency code indicating the operating
    currency of the bank account. For example, the currency code for US dollars
    is `USD`.
    """

    debit_mandate_reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reference identifier that will be displayed to UK bank account owners
    when collecting direct debit authorization. Only required for UK bank accounts.
    """

    debitable: bool = pydantic.Field()
    """
    Indicates whether it is possible for Square to take money from this 
    bank account.
    """

    fingerprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Square-assigned, unique identifier for the bank account based on the
    account information. The account fingerprint can be used to compare account
    entries and determine if the they represent the same real-world bank account.
    """

    holder_name: str = pydantic.Field()
    """
    Name of the account holder. This name must match the name 
    on the targeted bank account record.
    """

    id: str = pydantic.Field()
    """
    The unique, Square-issued identifier for the bank account.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location to which the bank account belongs.
    """

    primary_bank_identification_number: str = pydantic.Field()
    """
    Primary identifier for the bank. For more information, see 
    [Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api).
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client-provided identifier for linking the banking account to an entity
    in a third-party system (for example, a bank account number or a user identifier).
    """

    secondary_bank_identification_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secondary identifier for the bank. For more information, see 
    [Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api).
    """

    status: str = pydantic.Field()
    """
    Read-only. The current verification status of this BankAccount object.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current version of the `BankAccount`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
