

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preview_sql_table_command_type import PreviewSqlTableCommandType
from .request_id import RequestId


class PreviewSqlTableCommand(UniversalBaseModel):
    """
    Preview SQL table details.

        Retrieves metadata and sample data for a table. Used by the SQL editor
        and data explorer.

        Attributes:
            request_id: Unique identifier for this request.
            engine: SQL engine ('postgresql', 'mysql', 'duckdb', etc.).
            database: Database containing the table.
            schema: Schema containing the table.
            table_name: Table to preview.
            schema_path: Path of nested schemas (relative to `database`) for
                catalogs with nested schemas. Empty for the top level.
    """

    database: str
    engine: str
    request_id: typing_extensions.Annotated[
        RequestId, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")
    ]
    schema_: typing_extensions.Annotated[str, FieldMetadata(alias="schema"), pydantic.Field(alias="schema")]
    schema_path: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="schemaPath"), pydantic.Field(alias="schemaPath")
    ] = None
    table_name: typing_extensions.Annotated[str, FieldMetadata(alias="tableName"), pydantic.Field(alias="tableName")]
    type: PreviewSqlTableCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
