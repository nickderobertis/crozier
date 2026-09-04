

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .repayment_term import RepaymentTerm


class DynamicOfferRepayment(UniversalBaseModel):
    term: RepaymentTerm = pydantic.Field()
    """
    Contains information about the time period in which your user must repay the total amount of the grant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
