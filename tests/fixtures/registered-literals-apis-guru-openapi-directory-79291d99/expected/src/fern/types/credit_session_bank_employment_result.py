

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_session_bank_employment_status import CreditSessionBankEmploymentStatus


class CreditSessionBankEmploymentResult(UniversalBaseModel):
    """
    The details of a bank employment verification in Link.
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Institution ID associated with the Item.
    """

    item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive.
    """

    status: typing.Optional[CreditSessionBankEmploymentStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
