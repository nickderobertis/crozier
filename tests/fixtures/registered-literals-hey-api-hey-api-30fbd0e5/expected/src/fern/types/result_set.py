

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .result_set_last_insert_rowid import ResultSetLastInsertRowid


class ResultSet(UniversalBaseModel):
    """
    Result of executing an SQL statement.
    """

    columns: typing.List[str] = pydantic.Field()
    """
    Names of columns.
    
    Names of columns can be defined using the `AS` keyword in SQL:
    
    ```sql
    SELECT author AS author, COUNT(*) AS count FROM books GROUP BY author
    ```
    """

    column_types: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="columnTypes"),
        pydantic.Field(
            alias="columnTypes",
            description="Types of columns.\n\nThe types are currently shown for types declared in a SQL table. For column types of function calls, for example, an empty string is returned.",
        ),
    ]
    """
    Types of columns.
    
    The types are currently shown for types declared in a SQL table. For column types of function calls, for example, an empty string is returned.
    """

    rows: typing.List[typing.List[typing.Any]] = pydantic.Field()
    """
    Rows produced by the statement.
    """

    rows_affected: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="rowsAffected"),
        pydantic.Field(
            alias="rowsAffected",
            description="Number of rows that were affected by an UPDATE, INSERT or DELETE operation.\n\nThis value is not specified for other SQL statements.",
        ),
    ]
    """
    Number of rows that were affected by an UPDATE, INSERT or DELETE operation.
    
    This value is not specified for other SQL statements.
    """

    last_insert_rowid: typing_extensions.Annotated[
        typing.Optional[ResultSetLastInsertRowid],
        FieldMetadata(alias="lastInsertRowid"),
        pydantic.Field(
            alias="lastInsertRowid",
            description="ROWID of the last inserted row.\n\nThis value is not specified if the SQL statement was not an INSERT or if the table was not a ROWID table.",
        ),
    ] = None
    """
    ROWID of the last inserted row.
    
    This value is not specified if the SQL statement was not an INSERT or if the table was not a ROWID table.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
