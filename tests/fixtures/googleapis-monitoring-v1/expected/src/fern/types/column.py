

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .widget import Widget


class Column(UniversalBaseModel):
    """
    Defines the layout properties and content for a column.
    """

    weight: typing.Optional[str] = pydantic.Field(default=None)
    """
    The relative weight of this column. The column weight is used to adjust the width of columns on the screen (relative to peers). Greater the weight, greater the width of the column on the screen. If omitted, a value of 1 is used while rendering.
    """

    widgets: typing.Optional[typing.List[Widget]] = pydantic.Field(default=None)
    """
    The display widgets arranged vertically in this column.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
