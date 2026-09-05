

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .widget_details import WidgetDetails
from .widget_type import WidgetType


class Widget(UniversalBaseModel):
    type: WidgetType = pydantic.Field()
    """
    type of the property
    """

    details: WidgetDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
