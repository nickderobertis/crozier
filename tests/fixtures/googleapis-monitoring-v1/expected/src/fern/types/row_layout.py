

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .row import Row


class RowLayout(UniversalBaseModel):
    """
    A simplified layout that divides the available space into rows and arranges a set of widgets horizontally in each row.
    """

    rows: typing.Optional[typing.List[Row]] = pydantic.Field(default=None)
    """
    The rows of content to display.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
