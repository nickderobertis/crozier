

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_cable import NestedCable
from .nested_tag import NestedTag
from .writable_power_port_type import WritablePowerPortType


class WritablePowerPort(UniversalBaseModel):
    occupied: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="_occupied")] = None
    allocated_draw: typing.Optional[int] = pydantic.Field(default=None)
    """
    Allocated power draw (watts)
    """

    cable: typing.Optional[NestedCable] = None
    cable_end: typing.Optional[str] = None
    connected_endpoints: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Return the appropriate serializer for the type of connected object.
    """

    connected_endpoints_reachable: typing.Optional[bool] = None
    connected_endpoints_type: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device: int
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

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

    maximum_draw: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum power draw (watts)
    """

    module: typing.Optional[int] = None
    name: str
    tags: typing.Optional[typing.List[NestedTag]] = None
    type: typing.Optional[WritablePowerPortType] = pydantic.Field(default=None)
    """
    Physical port type
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
