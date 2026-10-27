

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .select_base import SelectBase


class SumSelect(SelectBase):
    """
    Calculates the sum over a specified column, if `subtractColumn` is set subtracts that. Additionally, if `distinctByColumn` is set, only aggregates the first encountered value for unique sets of keys.
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
