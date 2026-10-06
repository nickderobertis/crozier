

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_sql_tables_command_type import ListSqlTablesCommandType
from .request_id import RequestId


class ListSqlTablesCommand(UniversalBaseModel):
    """
    List tables in an SQL schema.

        Retrieves names of all tables and views in a schema. Used by the SQL
        editor for table selection.

        Attributes:
            request_id: Unique identifier for this request.
            engine: SQL engine ('postgresql', 'mysql', 'duckdb', etc.).
            database: Database to query.
            schema: Schema to list tables from.
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
    type: ListSqlTablesCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
