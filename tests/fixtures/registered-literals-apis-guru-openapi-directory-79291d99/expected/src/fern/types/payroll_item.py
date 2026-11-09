

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .payroll_income_account_data import PayrollIncomeAccountData
from .payroll_income_object import PayrollIncomeObject
from .payroll_item_status import PayrollItemStatus


class PayrollItem(UniversalBaseModel):
    """
    An object containing information about the payroll item.
    """

    accounts: typing.List[typing.Optional[PayrollIncomeAccountData]]
    institution_id: str = pydantic.Field()
    """
    The unique identifier of the institution associated with the Item.
    """

    institution_name: str = pydantic.Field()
    """
    The name of the institution associated with the Item.
    """

    item_id: ItemId
    payroll_income: typing.List[PayrollIncomeObject]
    status: typing.Optional[PayrollItemStatus] = None
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the Item was updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
