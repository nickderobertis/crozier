

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContextListOwnerContextsResponseItemsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique ID of the context.
    """

    name: str = pydantic.Field()
    """
    The user defined name of the context.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the context was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
