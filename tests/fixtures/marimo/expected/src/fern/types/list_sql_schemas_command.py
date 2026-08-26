

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_sql_schemas_command_type import ListSqlSchemasCommandType
from .request_id import RequestId


class ListSqlSchemasCommand(UniversalBaseModel):
    """
    List schemas in an SQL database.

        Retrieves names of all schemas in a database. Used by the SQL editor for
        schema selection.

        Attributes:
            request_id: Unique identifier for this request.
            engine: SQL engine ('postgresql', 'mysql', 'duckdb', etc.).
            database: Database to query.
            schema_path: Parent schema path whose child schemas to list.
                Empty lists the database's top-level schemas.
    """

    database: str
    engine: str
    request_id: typing_extensions.Annotated[
        RequestId, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")
    ]
    schema_path: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="schemaPath"), pydantic.Field(alias="schemaPath")
    ] = None
    type: ListSqlSchemasCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
