

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_employment_item import CreditBankEmploymentItem
from .credit_bank_employment_warning import CreditBankEmploymentWarning


class CreditBankEmploymentReport(UniversalBaseModel):
    """
    The report of the Bank Employment data for an end user.
    """

    bank_employment_report_id: str = pydantic.Field()
    """
    The unique identifier associated with the Bank Employment Report.
    """

    days_requested: int = pydantic.Field()
    """
    The number of days requested by the customer for the Bank Employment Report.
    """

    generated_time: dt.datetime = pydantic.Field()
    """
    The time when the Bank Employment Report was generated, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. "2018-04-12T03:32:11Z").
    """

    items: typing.List[CreditBankEmploymentItem] = pydantic.Field()
    """
    The list of Items in the report along with the associated metadata about the Item.
    """

    warnings: typing.List[CreditBankEmploymentWarning] = pydantic.Field()
    """
    If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
