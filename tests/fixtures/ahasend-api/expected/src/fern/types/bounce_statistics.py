

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounce import Bounce


class BounceStatistics(UniversalBaseModel):
    from_timestamp: dt.datetime = pydantic.Field()
    """
    Start time of the statistics bucket
    """

    to_timestamp: dt.datetime = pydantic.Field()
    """
    End time of the statistics bucket
    """

    bounces: typing.List[Bounce] = pydantic.Field()
    """
    Bounce count per bounce classification
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
