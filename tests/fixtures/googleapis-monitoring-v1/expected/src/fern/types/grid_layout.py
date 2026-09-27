

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .widget import Widget


class GridLayout(UniversalBaseModel):
    """
    A basic layout divides the available space into vertical columns of equal width and arranges a list of widgets using a row-first strategy.
    """

    columns: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of columns into which the view's width is divided. If omitted or set to zero, a system default will be used while rendering.
    """

    widgets: typing.Optional[typing.List[Widget]] = pydantic.Field(default=None)
    """
    The informational elements that are arranged into the columns row-first.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
