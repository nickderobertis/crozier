

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preview_dataset_column_command_source_type import PreviewDatasetColumnCommandSourceType
from .preview_dataset_column_command_type import PreviewDatasetColumnCommandType


class PreviewDatasetColumnCommand(UniversalBaseModel):
    """
    Preview a dataset column.

        Retrieves and displays data from a single column (dataframe or SQL table).
        Used by the data explorer UI.

        Attributes:
            source_type: Data source type ('dataframe', 'sql', etc.).
            source: Source identifier (connection string or variable name).
            table_name: Table or dataframe variable name.
            column_name: Column to preview.
            fully_qualified_table_name: Full database.schema.table name for SQL.
    """

    column_name: typing_extensions.Annotated[str, FieldMetadata(alias="columnName"), pydantic.Field(alias="columnName")]
    fully_qualified_table_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fullyQualifiedTableName"),
        pydantic.Field(alias="fullyQualifiedTableName"),
    ] = None
    source: str
    source_type: typing_extensions.Annotated[
        PreviewDatasetColumnCommandSourceType, FieldMetadata(alias="sourceType"), pydantic.Field(alias="sourceType")
    ]
    table_name: typing_extensions.Annotated[str, FieldMetadata(alias="tableName"), pydantic.Field(alias="tableName")]
    type: PreviewDatasetColumnCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
