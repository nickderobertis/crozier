

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .currency import Currency
from .currency_rate import CurrencyRate
from .id import Id
from .journal_entry_line_item import JournalEntryLineItem
from .row_version import RowVersion
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class JournalEntry(UniversalBaseModel):
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    currency_rate: typing.Optional[CurrencyRate] = None
    id: typing.Optional[Id] = None
    journal_symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    Journal symbol of the entry. For example IND for indirect costs
    """

    line_items: typing.Optional[typing.List[JournalEntryLineItem]] = pydantic.Field(default=None)
    """
    Requires a minimum of 2 line items that sum to 0
    """

    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reference for the journal entry.
    """

    posted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.
    """

    row_version: typing.Optional[RowVersion] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Journal entry title
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
