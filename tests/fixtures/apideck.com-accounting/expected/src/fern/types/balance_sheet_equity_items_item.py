

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id


class BalanceSheetEquityItemsItem(UniversalBaseModel):
    id: typing.Optional[Id] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the equity
    """

    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    The equity amount
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
