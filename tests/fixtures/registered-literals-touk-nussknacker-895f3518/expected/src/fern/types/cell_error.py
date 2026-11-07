

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CellError(UniversalBaseModel):
    column_name: typing_extensions.Annotated[str, FieldMetadata(alias="columnName"), pydantic.Field(alias="columnName")]
    row_index: typing_extensions.Annotated[int, FieldMetadata(alias="rowIndex"), pydantic.Field(alias="rowIndex")]
    error_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
