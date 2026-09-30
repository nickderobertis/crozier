

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .citus_function_metadata import CitusFunctionMetadata
from .citus_health_check_config import CitusHealthCheckConfig
from .citus_logical_model_metadata import CitusLogicalModelMetadata
from .citus_native_query_metadata import CitusNativeQueryMetadata
from .citus_source_metadata_kind import CitusSourceMetadataKind
from .citus_stored_procedure_metadata import CitusStoredProcedureMetadata
from .citus_table_metadata import CitusTableMetadata
from .postgres_conn_configuration import PostgresConnConfiguration
from .query_tags_config import QueryTagsConfig
from .source_customization import SourceCustomization


class CitusSourceMetadata(UniversalBaseModel):
    configuration: PostgresConnConfiguration
    customization: typing.Optional[SourceCustomization] = None
    functions: typing.Optional[typing.List[CitusFunctionMetadata]] = None
    health_check: typing.Optional[CitusHealthCheckConfig] = None
    kind: CitusSourceMetadataKind
    logical_models: typing.Optional[typing.List[CitusLogicalModelMetadata]] = None
    name: str
    native_queries: typing.Optional[typing.List[CitusNativeQueryMetadata]] = None
    query_tags: typing.Optional[QueryTagsConfig] = None
    stored_procedures: typing.Optional[typing.List[CitusStoredProcedureMetadata]] = None
    tables: typing.List[CitusTableMetadata]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CitusSourceMetadata)
