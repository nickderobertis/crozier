

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .filter_base import FilterBase


class SumFilter(FilterBase):
    """
    Filters entities to having the sum over a set of columns to be within a user defined range. See SumSelect for more info.
    """

    distinct: typing.Optional[bool] = None
    column: typing.Optional[ColumnId] = None
    subtract_column: typing_extensions.Annotated[
        typing.Optional[ColumnId], FieldMetadata(alias="subtractColumn"), pydantic.Field(alias="subtractColumn")
    ] = None
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
