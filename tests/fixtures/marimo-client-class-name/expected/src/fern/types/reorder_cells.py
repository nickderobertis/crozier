

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .reorder_cells_type import ReorderCellsType


class ReorderCells(UniversalBaseModel):
    """
    Replace the full cell ordering.

        Cell IDs present in the document but missing from `cell_ids`
        are appended at the end. IDs not in the document are ignored.
    """

    cell_ids: typing_extensions.Annotated[
        typing.List[CellId], FieldMetadata(alias="cellIds"), pydantic.Field(alias="cellIds")
    ]
    type: ReorderCellsType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
