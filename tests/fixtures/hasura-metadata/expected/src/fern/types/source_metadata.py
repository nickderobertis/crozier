

import typing

from .bigquery_source_metadata import BigquerySourceMetadata
from .citus_source_metadata import CitusSourceMetadata
from .cockroach_source_metadata import CockroachSourceMetadata
from .dataconnector_source_metadata import DataconnectorSourceMetadata
from .mssql_source_metadata import MssqlSourceMetadata
from .postgres_source_metadata import PostgresSourceMetadata

SourceMetadata = typing.Union[
    PostgresSourceMetadata,
    CitusSourceMetadata,
    CockroachSourceMetadata,
    MssqlSourceMetadata,
    BigquerySourceMetadata,
    DataconnectorSourceMetadata,
]
