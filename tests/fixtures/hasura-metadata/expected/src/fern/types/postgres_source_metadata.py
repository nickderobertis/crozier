

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .postgres_conn_configuration import PostgresConnConfiguration
from .postgres_function_metadata import PostgresFunctionMetadata
from .postgres_health_check_config import PostgresHealthCheckConfig
from .postgres_logical_model_metadata import PostgresLogicalModelMetadata
from .postgres_native_query_metadata import PostgresNativeQueryMetadata
from .postgres_source_metadata_kind import PostgresSourceMetadataKind
from .postgres_stored_procedure_metadata import PostgresStoredProcedureMetadata
from .postgres_table_metadata import PostgresTableMetadata
from .query_tags_config import QueryTagsConfig
from .source_customization import SourceCustomization


class PostgresSourceMetadata(UniversalBaseModel):
    configuration: PostgresConnConfiguration
    customization: typing.Optional[SourceCustomization] = None
    functions: typing.Optional[typing.List[PostgresFunctionMetadata]] = None
    health_check: typing.Optional[PostgresHealthCheckConfig] = None
    kind: PostgresSourceMetadataKind
    logical_models: typing.Optional[typing.List[PostgresLogicalModelMetadata]] = None
    name: str
    native_queries: typing.Optional[typing.List[PostgresNativeQueryMetadata]] = None
    query_tags: typing.Optional[QueryTagsConfig] = None
    stored_procedures: typing.Optional[typing.List[PostgresStoredProcedureMetadata]] = None
    tables: typing.List[PostgresTableMetadata]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PostgresSourceMetadata)
