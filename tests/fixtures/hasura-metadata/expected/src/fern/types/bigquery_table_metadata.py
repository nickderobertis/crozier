

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .apollo_federation_config import ApolloFederationConfig
from .big_query_table_name import BigQueryTableName
from .bigquery_computed_field_metadata import BigqueryComputedFieldMetadata
from .bigquery_delete_perm_def import BigqueryDeletePermDef
from .bigquery_insert_perm_def import BigqueryInsertPermDef
from .bigquery_select_perm_def import BigquerySelectPermDef
from .bigquery_table_config import BigqueryTableConfig
from .bigquery_update_perm_def import BigqueryUpdatePermDef
from .rel_def_rel_using_big_query_arr_rel_using_f_key_on_big_query import (
    RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQuery,
)
from .rel_def_rel_using_big_query_obj_rel_using_choice_big_query import RelDefRelUsingBigQueryObjRelUsingChoiceBigQuery
from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition


class BigqueryTableMetadata(UniversalBaseModel):
    """
    Representation of a table in metadata, 'tables.yaml' and 'metadata.json'
    """

    apollo_federation_config: typing.Optional[ApolloFederationConfig] = None
    array_relationships: typing.Optional[typing.List[RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQuery]] = None
    computed_fields: typing.Optional[typing.List[BigqueryComputedFieldMetadata]] = None
    configuration: typing.Optional[BigqueryTableConfig] = None
    delete_permissions: typing.Optional[typing.List[BigqueryDeletePermDef]] = None
    insert_permissions: typing.Optional[typing.List[BigqueryInsertPermDef]] = None
    is_enum: typing.Optional[bool] = None
    logical_model: typing.Optional[str] = None
    object_relationships: typing.Optional[typing.List[RelDefRelUsingBigQueryObjRelUsingChoiceBigQuery]] = None
    remote_relationships: typing.Optional[typing.List[RemoteRelationshipRemoteRelationshipDefinition]] = None
    select_permissions: typing.Optional[typing.List[BigquerySelectPermDef]] = None
    table: BigQueryTableName
    update_permissions: typing.Optional[typing.List[BigqueryUpdatePermDef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(BigqueryTableMetadata)
