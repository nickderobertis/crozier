

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .widget_channel import WidgetChannel
from .widget_member import WidgetMember


class WidgetResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    instant_invite: typing.Optional[str] = None
    channels: typing.List[WidgetChannel]
    members: typing.List[WidgetMember]
    presence_count: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
