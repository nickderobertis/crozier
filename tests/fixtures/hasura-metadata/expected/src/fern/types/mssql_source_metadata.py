

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .mssql_conn_configuration import MssqlConnConfiguration
from .mssql_function_metadata import MssqlFunctionMetadata
from .mssql_health_check_config import MssqlHealthCheckConfig
from .mssql_logical_model_metadata import MssqlLogicalModelMetadata
from .mssql_native_query_metadata import MssqlNativeQueryMetadata
from .mssql_source_metadata_kind import MssqlSourceMetadataKind
from .mssql_stored_procedure_metadata import MssqlStoredProcedureMetadata
from .mssql_table_metadata import MssqlTableMetadata
from .query_tags_config import QueryTagsConfig
from .source_customization import SourceCustomization


class MssqlSourceMetadata(UniversalBaseModel):
    configuration: MssqlConnConfiguration
    customization: typing.Optional[SourceCustomization] = None
    functions: typing.Optional[typing.List[MssqlFunctionMetadata]] = None
    health_check: typing.Optional[MssqlHealthCheckConfig] = None
    kind: MssqlSourceMetadataKind
    logical_models: typing.Optional[typing.List[MssqlLogicalModelMetadata]] = None
    name: str
    native_queries: typing.Optional[typing.List[MssqlNativeQueryMetadata]] = None
    query_tags: typing.Optional[QueryTagsConfig] = None
    stored_procedures: typing.Optional[typing.List[MssqlStoredProcedureMetadata]] = None
    tables: typing.List[MssqlTableMetadata]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(MssqlSourceMetadata)
