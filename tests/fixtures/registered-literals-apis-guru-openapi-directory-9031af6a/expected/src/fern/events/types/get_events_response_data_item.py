

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_events_response_data_item_group import GetEventsResponseDataItemGroup


class GetEventsResponseDataItem(UniversalBaseModel):
    """
    Event details
    """

    group: typing.Optional[GetEventsResponseDataItemGroup] = pydantic.Field(default=None)
    """
    Event group details
    """

    id: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
