

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .widget import Widget


class Row(UniversalBaseModel):
    """
    Defines the layout properties and content for a row.
    """

    weight: typing.Optional[str] = pydantic.Field(default=None)
    """
    The relative weight of this row. The row weight is used to adjust the height of rows on the screen (relative to peers). Greater the weight, greater the height of the row on the screen. If omitted, a value of 1 is used while rendering.
    """

    widgets: typing.Optional[typing.List[Widget]] = pydantic.Field(default=None)
    """
    The display widgets arranged horizontally in this row.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
