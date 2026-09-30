

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .apollo_federation_config import ApolloFederationConfig
from .cockroach_computed_field_metadata import CockroachComputedFieldMetadata
from .cockroach_delete_perm_def import CockroachDeletePermDef
from .cockroach_event_trigger_conf_event_trigger_conf import CockroachEventTriggerConfEventTriggerConf
from .cockroach_insert_perm_def import CockroachInsertPermDef
from .cockroach_select_perm_def import CockroachSelectPermDef
from .cockroach_table_config import CockroachTableConfig
from .cockroach_update_perm_def import CockroachUpdatePermDef
from .rel_def_rel_using_postgres_cockroach_arr_rel_using_f_key_on_postgres_cockroach import (
    RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroach,
)
from .rel_def_rel_using_postgres_cockroach_obj_rel_using_choice_postgres_cockroach import (
    RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroach,
)
from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition


class CockroachTableMetadata(UniversalBaseModel):
    """
    Representation of a table in metadata, 'tables.yaml' and 'metadata.json'
    """

    apollo_federation_config: typing.Optional[ApolloFederationConfig] = None
    array_relationships: typing.Optional[
        typing.List[RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroach]
    ] = None
    computed_fields: typing.Optional[typing.List[CockroachComputedFieldMetadata]] = None
    configuration: typing.Optional[CockroachTableConfig] = None
    delete_permissions: typing.Optional[typing.List[CockroachDeletePermDef]] = None
    event_triggers: typing.Optional[typing.List[CockroachEventTriggerConfEventTriggerConf]] = None
    insert_permissions: typing.Optional[typing.List[CockroachInsertPermDef]] = None
    is_enum: typing.Optional[bool] = None
    logical_model: typing.Optional[str] = None
    object_relationships: typing.Optional[
        typing.List[RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroach]
    ] = None
    remote_relationships: typing.Optional[typing.List[RemoteRelationshipRemoteRelationshipDefinition]] = None
    select_permissions: typing.Optional[typing.List[CockroachSelectPermDef]] = None
    table: typing.Dict[str, typing.Any]
    update_permissions: typing.Optional[typing.List[CockroachUpdatePermDef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CockroachTableMetadata)
