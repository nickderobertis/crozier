

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id
from .journal_entry_line_item_type import JournalEntryLineItemType
from .linked_ledger_account import LinkedLedgerAccount
from .linked_tax_rate import LinkedTaxRate
from .linked_tracking_category import LinkedTrackingCategory


class JournalEntryLineItem(UniversalBaseModel):
    department_id: typing.Optional[Id] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    User defined description
    """

    id: typing.Optional[Id] = None
    ledger_account: typing.Optional[LinkedLedgerAccount] = None
    location_id: typing.Optional[Id] = None
    tax_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Tax amount
    """

    tax_rate: typing.Optional[LinkedTaxRate] = None
    total_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Debit entries are considered positive, and credit entries are considered negative.
    """

    tracking_category: typing.Optional[LinkedTrackingCategory] = None
    type: JournalEntryLineItemType = pydantic.Field()
    """
    Debit entries are considered positive, and credit entries are considered negative.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
