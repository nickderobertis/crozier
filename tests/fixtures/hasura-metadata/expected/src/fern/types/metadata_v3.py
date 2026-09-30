

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .action_metadata import ActionMetadata
from .allowlist_entry import AllowlistEntry
from .api_limit import ApiLimit
from .backend_map_backend_config_wrapper import BackendMapBackendConfigWrapper
from .create_collection import CreateCollection
from .cron_trigger_metadata import CronTriggerMetadata
from .custom_types import CustomTypes
from .endpoint_metadata_query_reference import EndpointMetadataQueryReference
from .metrics_config import MetricsConfig
from .network import Network
from .open_telemetry_config import OpenTelemetryConfig
from .remote_schema_metadata_remote_relationship_definition import RemoteSchemaMetadataRemoteRelationshipDefinition
from .role import Role
from .source_metadata import SourceMetadata


class MetadataV3(UniversalBaseModel):
    actions: typing.Optional[typing.List[ActionMetadata]] = pydantic.Field(default=None)
    """
    action definitions which extend Hasura's schema with custom business logic using custom queries and mutations
    """

    allowlist: typing.Optional[typing.List[AllowlistEntry]] = pydantic.Field(default=None)
    """
    safe GraphQL operations - when allow lists are enabled only these operations are allowed
    """

    api_limits: typing.Optional[ApiLimit] = None
    backend_configs: typing.Optional[BackendMapBackendConfigWrapper] = None
    cron_triggers: typing.Optional[typing.List[CronTriggerMetadata]] = pydantic.Field(default=None)
    """
    reliably trigger HTTP endpoints to run custom business logic periodically based on a cron schedule
    """

    custom_types: typing.Optional[CustomTypes] = None
    graphql_schema_introspection: typing.Optional[typing.List[str]] = None
    inherited_roles: typing.Optional[typing.List[Role]] = pydantic.Field(default=None)
    """
    an inherited role is a way to create a new role which inherits permissions from two or more roles
    """

    metrics_config: typing.Optional[MetricsConfig] = None
    network: typing.Optional[Network] = None
    opentelemetry: typing.Optional[OpenTelemetryConfig] = None
    query_collections: typing.Optional[typing.List[CreateCollection]] = pydantic.Field(default=None)
    """
    group queries using query collections
    """

    remote_schemas: typing.Optional[typing.List[RemoteSchemaMetadataRemoteRelationshipDefinition]] = pydantic.Field(
        default=None
    )
    """
    merge remote GraphQL schemas and provide a unified GraphQL API
    """

    rest_endpoints: typing.Optional[typing.List[EndpointMetadataQueryReference]] = pydantic.Field(default=None)
    """
    REST interfaces to saved GraphQL queries and mutations
    """

    sources: typing.List[SourceMetadata] = pydantic.Field()
    """
    configured databases
    """

    version: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(MetadataV3)
