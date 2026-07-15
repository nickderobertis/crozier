

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_account import BankAccount
from .created_at import CreatedAt
from .created_by import CreatedBy
from .currency import Currency
from .id import Id
from .ledger_account_categories_item import LedgerAccountCategoriesItem
from .ledger_account_classification import LedgerAccountClassification
from .ledger_account_parent_account import LedgerAccountParentAccount
from .ledger_account_status import LedgerAccountStatus
from .ledger_account_sub_accounts_item import LedgerAccountSubAccountsItem
from .ledger_account_type import LedgerAccountType
from .linked_tax_rate import LinkedTaxRate
from .row_version import RowVersion
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class LedgerAccount(UniversalBaseModel):
    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the account is active or not.
    """

    bank_account: typing.Optional[BankAccount] = None
    categories: typing.Optional[typing.List[LedgerAccountCategoriesItem]] = pydantic.Field(default=None)
    """
    The categories of the account.
    """

    classification: typing.Optional[LedgerAccountClassification] = pydantic.Field(default=None)
    """
    The classification of account.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The code assigned to the account.
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    current_balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    The current balance of the account.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the account.
    """

    display_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human readable display ID used when displaying the account
    """

    fully_qualified_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fully qualified name of the account.
    """

    header: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the account is a header or not.
    """

    id: typing.Optional[Id] = None
    last_reconciliation_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Reconciliation Date means the last calendar day of each Reconciliation Period.
    """

    level: typing.Optional[float] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the account.
    """

    nominal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The nominal code of the ledger account.
    """

    opening_balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    The opening balance of the account.
    """

    parent_account: typing.Optional[LedgerAccountParentAccount] = None
    row_version: typing.Optional[RowVersion] = None
    status: typing.Optional[LedgerAccountStatus] = pydantic.Field(default=None)
    """
    The status of the account.
    """

    sub_account: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the account is a sub account or not.
    """

    sub_accounts: typing.Optional[typing.List[LedgerAccountSubAccountsItem]] = pydantic.Field(default=None)
    """
    The sub accounts of the account.
    """

    sub_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub type of account.
    """

    tax_rate: typing.Optional[LinkedTaxRate] = None
    tax_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax type of the account.
    """

    type: typing.Optional[LedgerAccountType] = pydantic.Field(default=None)
    """
    The type of account.
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
