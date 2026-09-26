

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Refund(UniversalBaseModel):
    id: typing.Optional[str] = None
    payment_id: typing.Optional[str] = None
    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    Refund amount in cents
    """

    created: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
