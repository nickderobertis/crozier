

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ColumnSettings(UniversalBaseModel):
    """
    The persistent settings for a table's columns.
    """

    column: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required. The id of the column.
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Required. Whether the column should be visible on page load.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
