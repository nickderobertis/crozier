

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .cockroach_function_metadata import CockroachFunctionMetadata
from .cockroach_health_check_config import CockroachHealthCheckConfig
from .cockroach_logical_model_metadata import CockroachLogicalModelMetadata
from .cockroach_native_query_metadata import CockroachNativeQueryMetadata
from .cockroach_source_metadata_kind import CockroachSourceMetadataKind
from .cockroach_stored_procedure_metadata import CockroachStoredProcedureMetadata
from .cockroach_table_metadata import CockroachTableMetadata
from .postgres_conn_configuration import PostgresConnConfiguration
from .query_tags_config import QueryTagsConfig
from .source_customization import SourceCustomization


class CockroachSourceMetadata(UniversalBaseModel):
    configuration: PostgresConnConfiguration
    customization: typing.Optional[SourceCustomization] = None
    functions: typing.Optional[typing.List[CockroachFunctionMetadata]] = None
    health_check: typing.Optional[CockroachHealthCheckConfig] = None
    kind: CockroachSourceMetadataKind
    logical_models: typing.Optional[typing.List[CockroachLogicalModelMetadata]] = None
    name: str
    native_queries: typing.Optional[typing.List[CockroachNativeQueryMetadata]] = None
    query_tags: typing.Optional[QueryTagsConfig] = None
    stored_procedures: typing.Optional[typing.List[CockroachStoredProcedureMetadata]] = None
    tables: typing.List[CockroachTableMetadata]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CockroachSourceMetadata)
