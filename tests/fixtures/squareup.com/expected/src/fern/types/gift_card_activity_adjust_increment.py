

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money
from .reason import Reason


class GiftCardActivityAdjustIncrement(UniversalBaseModel):
    """
    Describes a gift card activity of the ADJUST_INCREMENT type.
    """

    amount_money: Money
    reason: Reason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
