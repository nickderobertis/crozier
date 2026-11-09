

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pay import Pay
from .total_canonical_description import TotalCanonicalDescription


class Total(UniversalBaseModel):
    """
    An object representing both the current pay period and year to date amount for a category.
    """

    canonical_description: typing.Optional[TotalCanonicalDescription] = None
    current_pay: typing.Optional[Pay] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Text of the line item as printed on the paystub.
    """

    ytd_pay: typing.Optional[Pay] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
