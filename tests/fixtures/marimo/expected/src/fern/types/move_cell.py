

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .move_cell_type import MoveCellType


class MoveCell(UniversalBaseModel):
    """
    Reposition a cell in the notebook.
    """

    after: typing.Optional[CellId] = None
    before: typing.Optional[CellId] = None
    cell_id: typing_extensions.Annotated[CellId, FieldMetadata(alias="cellId"), pydantic.Field(alias="cellId")]
    type: MoveCellType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
