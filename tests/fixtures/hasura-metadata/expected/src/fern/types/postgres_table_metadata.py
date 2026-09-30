

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .apollo_federation_config import ApolloFederationConfig
from .postgres_computed_field_metadata import PostgresComputedFieldMetadata
from .postgres_delete_perm_def import PostgresDeletePermDef
from .postgres_event_trigger_conf_event_trigger_conf import PostgresEventTriggerConfEventTriggerConf
from .postgres_insert_perm_def import PostgresInsertPermDef
from .postgres_select_perm_def import PostgresSelectPermDef
from .postgres_table_config import PostgresTableConfig
from .postgres_update_perm_def import PostgresUpdatePermDef
from .rel_def_rel_using_postgres_vanilla_arr_rel_using_f_key_on_postgres_vanilla import (
    RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanilla,
)
from .rel_def_rel_using_postgres_vanilla_obj_rel_using_choice_postgres_vanilla import (
    RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanilla,
)
from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition


class PostgresTableMetadata(UniversalBaseModel):
    """
    Representation of a table in metadata, 'tables.yaml' and 'metadata.json'
    """

    apollo_federation_config: typing.Optional[ApolloFederationConfig] = None
    array_relationships: typing.Optional[typing.List[RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanilla]] = (
        None
    )
    computed_fields: typing.Optional[typing.List[PostgresComputedFieldMetadata]] = None
    configuration: typing.Optional[PostgresTableConfig] = None
    delete_permissions: typing.Optional[typing.List[PostgresDeletePermDef]] = None
    event_triggers: typing.Optional[typing.List[PostgresEventTriggerConfEventTriggerConf]] = None
    insert_permissions: typing.Optional[typing.List[PostgresInsertPermDef]] = None
    is_enum: typing.Optional[bool] = None
    logical_model: typing.Optional[str] = None
    object_relationships: typing.Optional[
        typing.List[RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanilla]
    ] = None
    remote_relationships: typing.Optional[typing.List[RemoteRelationshipRemoteRelationshipDefinition]] = None
    select_permissions: typing.Optional[typing.List[PostgresSelectPermDef]] = None
    table: typing.Dict[str, typing.Any]
    update_permissions: typing.Optional[typing.List[PostgresUpdatePermDef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PostgresTableMetadata)
