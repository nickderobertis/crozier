

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BalanceTransaction(UniversalBaseModel):
    id: typing.Optional[str] = None
    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    Amount in cents
    """

    type: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
