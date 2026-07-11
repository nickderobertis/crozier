

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .widget_scope import WidgetScope
from .widget_status import WidgetStatus


class Widget(UniversalBaseModel):
    scope: typing.Optional[WidgetScope] = None
    status: typing.Optional[WidgetStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
