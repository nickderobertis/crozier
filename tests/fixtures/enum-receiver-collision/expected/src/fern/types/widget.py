

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .widget_binding import WidgetBinding
from .widget_owner import WidgetOwner


class Widget(UniversalBaseModel):
    owner: typing.Optional[WidgetOwner] = None
    binding: typing.Optional[WidgetBinding] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
