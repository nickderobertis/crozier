

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timeline_envelopes_item import TimelineEnvelopesItem
from .timeline_items_item import TimelineItemsItem


class Timeline(UniversalBaseModel):
    items: typing.List[TimelineItemsItem]
    envelopes: typing.Optional[typing.List[TimelineEnvelopesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
