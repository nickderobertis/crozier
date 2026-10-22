

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeliveryEvent(UniversalBaseModel):
    time: dt.datetime = pydantic.Field()
    """
    Timestamp of the delivery event
    """

    log: str = pydantic.Field()
    """
    Log message for the delivery event
    """

    status: str = pydantic.Field()
    """
    Status of the delivery event
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
