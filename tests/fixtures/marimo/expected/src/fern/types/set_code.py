

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .set_code_type import SetCodeType


class SetCode(UniversalBaseModel):
    """
    Replace a cell's source code.
    """

    cell_id: typing_extensions.Annotated[CellId, FieldMetadata(alias="cellId"), pydantic.Field(alias="cellId")]
    code: str
    type: SetCodeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
