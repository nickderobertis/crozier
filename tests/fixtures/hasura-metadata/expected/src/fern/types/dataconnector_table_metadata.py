

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .apollo_federation_config import ApolloFederationConfig
from .dataconnector_computed_field_metadata import DataconnectorComputedFieldMetadata
from .dataconnector_delete_perm_def import DataconnectorDeletePermDef
from .dataconnector_insert_perm_def import DataconnectorInsertPermDef
from .dataconnector_select_perm_def import DataconnectorSelectPermDef
from .dataconnector_table_config import DataconnectorTableConfig
from .dataconnector_update_perm_def import DataconnectorUpdatePermDef
from .rel_def_rel_using_data_connector_arr_rel_using_f_key_on_data_connector import (
    RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnector,
)
from .rel_def_rel_using_data_connector_obj_rel_using_choice_data_connector import (
    RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnector,
)
from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition


class DataconnectorTableMetadata(UniversalBaseModel):
    """
    Representation of a table in metadata, 'tables.yaml' and 'metadata.json'
    """

    apollo_federation_config: typing.Optional[ApolloFederationConfig] = None
    array_relationships: typing.Optional[typing.List[RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnector]] = None
    computed_fields: typing.Optional[typing.List[DataconnectorComputedFieldMetadata]] = None
    configuration: typing.Optional[DataconnectorTableConfig] = None
    delete_permissions: typing.Optional[typing.List[DataconnectorDeletePermDef]] = None
    insert_permissions: typing.Optional[typing.List[DataconnectorInsertPermDef]] = None
    is_enum: typing.Optional[bool] = None
    logical_model: typing.Optional[str] = None
    object_relationships: typing.Optional[typing.List[RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnector]] = None
    remote_relationships: typing.Optional[typing.List[RemoteRelationshipRemoteRelationshipDefinition]] = None
    select_permissions: typing.Optional[typing.List[DataconnectorSelectPermDef]] = None
    table: typing.List[str]
    update_permissions: typing.Optional[typing.List[DataconnectorUpdatePermDef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DataconnectorTableMetadata)
