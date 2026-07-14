

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_subcategory import EventSubcategory


class EventCategory(UniversalBaseModel):
    """
    A collection of event subcategories
    """

    category: typing.Optional[str] = None
    description: typing.Optional[str] = None
    subcategories: typing.Optional[typing.List[EventSubcategory]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
