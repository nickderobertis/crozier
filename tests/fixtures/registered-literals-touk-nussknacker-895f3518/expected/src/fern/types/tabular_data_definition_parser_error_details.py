

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_error import CellError
from .column_definition import ColumnDefinition


class TabularDataDefinitionParserErrorDetails(UniversalBaseModel):
    cell_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[CellError]], FieldMetadata(alias="cellErrors"), pydantic.Field(alias="cellErrors")
    ] = None
    column_definitions: typing_extensions.Annotated[
        typing.Optional[typing.List[ColumnDefinition]],
        FieldMetadata(alias="columnDefinitions"),
        pydantic.Field(alias="columnDefinitions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
