

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_event import ConnectorEvent
from .connector_unified_apis_item_oauth_scopes_item import ConnectorUnifiedApisItemOauthScopesItem
from .linked_connector_resource import LinkedConnectorResource
from .resource_id import ResourceId
from .unified_api_id import UnifiedApiId


class ConnectorUnifiedApisItem(UniversalBaseModel):
    downstream_unsupported_resources: typing.Optional[typing.List[ResourceId]] = pydantic.Field(default=None)
    """
    List of resources that are not supported on the downstream.
    """

    id: typing.Optional[UnifiedApiId] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the API.
    """

    oauth_scopes: typing.Optional[typing.List[ConnectorUnifiedApisItemOauthScopesItem]] = None
    supported_events: typing.Optional[typing.List[ConnectorEvent]] = pydantic.Field(default=None)
    """
    List of events that are supported on the connector for this Unified API.
    """

    supported_resources: typing.Optional[typing.List[LinkedConnectorResource]] = pydantic.Field(default=None)
    """
    List of resources that are supported on the connector.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
