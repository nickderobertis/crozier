

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreditSessionPayrollIncomeResult(UniversalBaseModel):
    """
    The details of a digital payroll income verification in Link
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Institution ID associated with the Item.
    """

    institution_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Institution Name associated with the Item.
    """

    num_paystubs_retrieved: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of paystubs retrieved from a payroll provider.
    """

    num_w2s_retrieved: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of w2s retrieved from a payroll provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
