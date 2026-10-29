

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .select_base import SelectBase


class CountSelect(SelectBase):
    """
    Emits the number of filtered events, or number of unique entries in a selected column.
    """

    distinct: typing.Optional[bool] = None
    column: typing.Optional[ColumnId] = None
    distinct_by_column: typing_extensions.Annotated[
        typing.Optional[typing.List[ColumnId]],
        FieldMetadata(alias="distinctByColumn"),
        pydantic.Field(alias="distinctByColumn"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
