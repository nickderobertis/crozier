

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .set_config_type import SetConfigType


class SetConfig(UniversalBaseModel):
    """
    Replace a cell's config.
    """

    cell_id: typing_extensions.Annotated[CellId, FieldMetadata(alias="cellId"), pydantic.Field(alias="cellId")]
    column: typing.Optional[int] = None
    disabled: bool
    hide_code: typing_extensions.Annotated[bool, FieldMetadata(alias="hideCode"), pydantic.Field(alias="hideCode")]
    type: SetConfigType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
