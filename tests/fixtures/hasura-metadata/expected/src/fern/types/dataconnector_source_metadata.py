

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .dataconnector_function_metadata import DataconnectorFunctionMetadata
from .dataconnector_logical_model_metadata import DataconnectorLogicalModelMetadata
from .dataconnector_native_query_metadata import DataconnectorNativeQueryMetadata
from .dataconnector_stored_procedure_metadata import DataconnectorStoredProcedureMetadata
from .dataconnector_table_metadata import DataconnectorTableMetadata
from .graph_ql_name import GraphQlName
from .query_tags_config import QueryTagsConfig
from .source_customization import SourceCustomization


class DataconnectorSourceMetadata(UniversalBaseModel):
    configuration: typing.Dict[str, typing.Any]
    customization: typing.Optional[SourceCustomization] = None
    functions: typing.Optional[typing.List[DataconnectorFunctionMetadata]] = None
    kind: GraphQlName
    logical_models: typing.Optional[typing.List[DataconnectorLogicalModelMetadata]] = None
    name: str
    native_queries: typing.Optional[typing.List[DataconnectorNativeQueryMetadata]] = None
    query_tags: typing.Optional[QueryTagsConfig] = None
    stored_procedures: typing.Optional[typing.List[DataconnectorStoredProcedureMetadata]] = None
    tables: typing.List[DataconnectorTableMetadata]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DataconnectorSourceMetadata)
