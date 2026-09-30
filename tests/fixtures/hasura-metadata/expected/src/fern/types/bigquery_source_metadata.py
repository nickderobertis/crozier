

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .big_query_conn_source_config import BigQueryConnSourceConfig
from .bigquery_function_metadata import BigqueryFunctionMetadata
from .bigquery_logical_model_metadata import BigqueryLogicalModelMetadata
from .bigquery_native_query_metadata import BigqueryNativeQueryMetadata
from .bigquery_source_metadata_kind import BigquerySourceMetadataKind
from .bigquery_stored_procedure_metadata import BigqueryStoredProcedureMetadata
from .bigquery_table_metadata import BigqueryTableMetadata
from .query_tags_config import QueryTagsConfig
from .source_customization import SourceCustomization


class BigquerySourceMetadata(UniversalBaseModel):
    configuration: BigQueryConnSourceConfig
    customization: typing.Optional[SourceCustomization] = None
    functions: typing.Optional[typing.List[BigqueryFunctionMetadata]] = None
    kind: BigquerySourceMetadataKind
    logical_models: typing.Optional[typing.List[BigqueryLogicalModelMetadata]] = None
    name: str
    native_queries: typing.Optional[typing.List[BigqueryNativeQueryMetadata]] = None
    query_tags: typing.Optional[QueryTagsConfig] = None
    stored_procedures: typing.Optional[typing.List[BigqueryStoredProcedureMetadata]] = None
    tables: typing.List[BigqueryTableMetadata]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(BigquerySourceMetadata)
