

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_event_event_source import ConnectorEventEventSource
from .resource_id import ResourceId


class ConnectorEvent(UniversalBaseModel):
    """
    Unify event that is supported on the connector. Events are delivered via Webhooks.
    """

    downstream_event_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Downstream event type
    """

    entity_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unify entity type
    """

    event_source: typing.Optional[ConnectorEventEventSource] = pydantic.Field(default=None)
    """
    Unify event source
    """

    event_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unify event type
    """

    resources: typing.Optional[typing.List[ResourceId]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
