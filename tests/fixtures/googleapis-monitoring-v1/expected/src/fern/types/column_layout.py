

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column import Column


class ColumnLayout(UniversalBaseModel):
    """
    A simplified layout that divides the available space into vertical columns and arranges a set of widgets vertically in each column.
    """

    columns: typing.Optional[typing.List[Column]] = pydantic.Field(default=None)
    """
    The columns of content to display.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
