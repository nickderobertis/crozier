

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .apollo_federation_config import ApolloFederationConfig
from .citus_computed_field_metadata import CitusComputedFieldMetadata
from .citus_delete_perm_def import CitusDeletePermDef
from .citus_event_trigger_conf_event_trigger_conf import CitusEventTriggerConfEventTriggerConf
from .citus_insert_perm_def import CitusInsertPermDef
from .citus_select_perm_def import CitusSelectPermDef
from .citus_table_config import CitusTableConfig
from .citus_update_perm_def import CitusUpdatePermDef
from .rel_def_rel_using_postgres_citus_arr_rel_using_f_key_on_postgres_citus import (
    RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitus,
)
from .rel_def_rel_using_postgres_citus_obj_rel_using_choice_postgres_citus import (
    RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitus,
)
from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition


class CitusTableMetadata(UniversalBaseModel):
    """
    Representation of a table in metadata, 'tables.yaml' and 'metadata.json'
    """

    apollo_federation_config: typing.Optional[ApolloFederationConfig] = None
    array_relationships: typing.Optional[typing.List[RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitus]] = None
    computed_fields: typing.Optional[typing.List[CitusComputedFieldMetadata]] = None
    configuration: typing.Optional[CitusTableConfig] = None
    delete_permissions: typing.Optional[typing.List[CitusDeletePermDef]] = None
    event_triggers: typing.Optional[typing.List[CitusEventTriggerConfEventTriggerConf]] = None
    insert_permissions: typing.Optional[typing.List[CitusInsertPermDef]] = None
    is_enum: typing.Optional[bool] = None
    logical_model: typing.Optional[str] = None
    object_relationships: typing.Optional[typing.List[RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitus]] = None
    remote_relationships: typing.Optional[typing.List[RemoteRelationshipRemoteRelationshipDefinition]] = None
    select_permissions: typing.Optional[typing.List[CitusSelectPermDef]] = None
    table: typing.Dict[str, typing.Any]
    update_permissions: typing.Optional[typing.List[CitusUpdatePermDef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CitusTableMetadata)
