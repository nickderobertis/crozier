

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_cable import NestedCable
from .nested_tag import NestedTag
from .writable_power_feed_phase import WritablePowerFeedPhase
from .writable_power_feed_status import WritablePowerFeedStatus
from .writable_power_feed_supply import WritablePowerFeedSupply
from .writable_power_feed_type import WritablePowerFeedType


class WritablePowerFeed(UniversalBaseModel):
    occupied: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="_occupied"), pydantic.Field(alias="_occupied")
    ] = None
    amperage: typing.Optional[int] = None
    cable: typing.Optional[NestedCable] = None
    cable_end: typing.Optional[str] = None
    comments: typing.Optional[str] = None
    connected_endpoints: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Return the appropriate serializer for the type of connected object.
    """

    connected_endpoints_reachable: typing.Optional[bool] = None
    connected_endpoints_type: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    link_peers: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Return the appropriate serializer for the link termination model.
    """

    link_peers_type: typing.Optional[str] = None
    mark_connected: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Treat as if a cable is connected
    """

    max_utilization: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum permissible draw (percentage)
    """

    name: str
    phase: typing.Optional[WritablePowerFeedPhase] = None
    power_panel: int
    rack: typing.Optional[int] = None
    status: typing.Optional[WritablePowerFeedStatus] = None
    supply: typing.Optional[WritablePowerFeedSupply] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    type: typing.Optional[WritablePowerFeedType] = None
    url: typing.Optional[str] = None
    voltage: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
