

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class TenderCashDetails(UniversalBaseModel):
    """
    Represents the details of a tender with `type` `CASH`.
    """

    buyer_tendered_money: typing.Optional[Money] = None
    change_back_money: typing.Optional[Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
