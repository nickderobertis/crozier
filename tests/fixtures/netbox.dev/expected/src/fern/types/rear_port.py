

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .component_nested_module import ComponentNestedModule
from .nested_cable import NestedCable
from .nested_device import NestedDevice
from .nested_tag import NestedTag
from .rear_port_type import RearPortType


class RearPort(UniversalBaseModel):
    occupied: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="_occupied")] = None
    cable: typing.Optional[NestedCable] = None
    cable_end: typing.Optional[str] = None
    color: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device: NestedDevice
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

    module: typing.Optional[ComponentNestedModule] = None
    name: str
    positions: typing.Optional[int] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    type: RearPortType
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
