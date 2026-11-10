

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_session_bank_income_status import CreditSessionBankIncomeStatus


class CreditSessionBankIncomeResult(UniversalBaseModel):
    """
    The details of a bank income verification in Link
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Institution ID associated with the Item.
    """

    item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive.
    """

    status: typing.Optional[CreditSessionBankIncomeStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
