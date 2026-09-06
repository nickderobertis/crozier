

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListItemsItemsRequestCreatedOn(UniversalBaseModel):
    lte: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Filter items created before this date
    """

    gte: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Filter items created after this date
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
