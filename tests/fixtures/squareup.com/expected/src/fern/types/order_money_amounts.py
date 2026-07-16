

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class OrderMoneyAmounts(UniversalBaseModel):
    """
    A collection of various money amounts.
    """

    discount_money: typing.Optional[Money] = None
    service_charge_money: typing.Optional[Money] = None
    tax_money: typing.Optional[Money] = None
    tip_money: typing.Optional[Money] = None
    total_money: typing.Optional[Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
