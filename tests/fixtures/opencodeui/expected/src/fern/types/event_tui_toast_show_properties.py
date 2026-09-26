

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_tui_toast_show_properties_variant import EventTuiToastShowPropertiesVariant


class EventTuiToastShowProperties(UniversalBaseModel):
    title: typing.Optional[str] = None
    message: str
    variant: EventTuiToastShowPropertiesVariant
    duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    Duration in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
