

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_balance import AccountBalance
from .account_base_verification_status import AccountBaseVerificationStatus
from .account_subtype import AccountSubtype
from .account_type import AccountType


class AccountBase(UniversalBaseModel):
    """
    A single account at a financial institution.
    """

    account_id: str = pydantic.Field()
    """
    Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.
    
    The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.
    
    If an account with a specific `account_id` disappears instead of changing, the account is likely closed. Closed accounts are not returned by the Plaid API.
    
    Like all Plaid identifiers, the `account_id` is case sensitive.
    """

    balances: AccountBalance
    mask: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user.
    """

    name: str = pydantic.Field()
    """
    The name of the account, either assigned by the user or by the financial institution itself
    """

    official_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The official name of the account as given by the financial institution
    """

    persistent_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique and persistent identifier for accounts that can be used to trace multiple instances of the same account across different Items for depository accounts. This is currently an opt-in field and only supported for Chase Items.
    """

    subtype: typing.Optional[AccountSubtype] = None
    type: AccountType
    verification_status: typing.Optional[AccountBaseVerificationStatus] = pydantic.Field(default=None)
    """
    The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.
    
    `pending_automatic_verification`: The Item is pending automatic verification
    
    `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the two amounts.
    
    `automatically_verified`: The Item has successfully been automatically verified    
    
    `manually_verified`: The Item has successfully been manually verified
    
    `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.
    
    `verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.    
        
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
