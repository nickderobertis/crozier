

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SourcePostgresConfig(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Schema containing the source table"),
    ] = None
    """
    Schema containing the source table
    """

    primary_key: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Columns that uniquely identify a row in this stream
    """

    cursor_field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Monotonic column used for incremental reads
    """

    page_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Rows to read per page
    """

    ssl_ca_pem: typing.Optional[str] = pydantic.Field(default=None)
    """
    PEM-encoded CA certificate for SSL verification (required for verify-ca / verify-full with a private CA)
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postgres connection string
    """

    connection_string: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated alias for url; prefer url
    """

    table: typing.Optional[str] = pydantic.Field(default=None)
    """
    Table to read from
    """

    stream: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stream name emitted in the catalog and records. Defaults to table name.
    """

    query: typing.Optional[str] = pydantic.Field(default=None)
    """
    SQL query to read from. Must expose the primary_key and cursor_field columns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
