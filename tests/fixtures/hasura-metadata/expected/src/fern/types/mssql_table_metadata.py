

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .apollo_federation_config import ApolloFederationConfig
from .mssql_computed_field_metadata import MssqlComputedFieldMetadata
from .mssql_delete_perm_def import MssqlDeletePermDef
from .mssql_event_trigger_conf_event_trigger_conf import MssqlEventTriggerConfEventTriggerConf
from .mssql_insert_perm_def import MssqlInsertPermDef
from .mssql_select_perm_def import MssqlSelectPermDef
from .mssql_table_config import MssqlTableConfig
from .mssql_update_perm_def import MssqlUpdatePermDef
from .rel_def_rel_using_mssql_arr_rel_using_f_key_on_mssql import RelDefRelUsingMssqlArrRelUsingFKeyOnMssql
from .rel_def_rel_using_mssql_obj_rel_using_choice_mssql import RelDefRelUsingMssqlObjRelUsingChoiceMssql
from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition


class MssqlTableMetadata(UniversalBaseModel):
    """
    Representation of a table in metadata, 'tables.yaml' and 'metadata.json'
    """

    apollo_federation_config: typing.Optional[ApolloFederationConfig] = None
    array_relationships: typing.Optional[typing.List[RelDefRelUsingMssqlArrRelUsingFKeyOnMssql]] = None
    computed_fields: typing.Optional[typing.List[MssqlComputedFieldMetadata]] = None
    configuration: typing.Optional[MssqlTableConfig] = None
    delete_permissions: typing.Optional[typing.List[MssqlDeletePermDef]] = None
    event_triggers: typing.Optional[typing.List[MssqlEventTriggerConfEventTriggerConf]] = None
    insert_permissions: typing.Optional[typing.List[MssqlInsertPermDef]] = None
    is_enum: typing.Optional[bool] = None
    logical_model: typing.Optional[str] = None
    object_relationships: typing.Optional[typing.List[RelDefRelUsingMssqlObjRelUsingChoiceMssql]] = None
    remote_relationships: typing.Optional[typing.List[RemoteRelationshipRemoteRelationshipDefinition]] = None
    select_permissions: typing.Optional[typing.List[MssqlSelectPermDef]] = None
    table: typing.Dict[str, typing.Any]
    update_permissions: typing.Optional[typing.List[MssqlUpdatePermDef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(MssqlTableMetadata)
