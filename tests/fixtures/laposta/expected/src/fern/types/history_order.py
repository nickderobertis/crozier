

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .history_order_order import HistoryOrderOrder


class HistoryOrder(UniversalBaseModel):
    order_by: typing.Optional[str] = None
    order: typing.Optional[HistoryOrderOrder] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
