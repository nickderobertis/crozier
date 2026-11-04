

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nsi_connections_item_core_ns_list_item import NsiConnectionsItemCoreNsListItem
from .nsi_connections_item_core_pnf_list_item import NsiConnectionsItemCorePnfListItem
from .nsi_connections_item_core_shared import NsiConnectionsItemCoreShared


class NsiConnectionsItemCore(UniversalBaseModel):
    """
    The Core part of the 5G service connection
    """

    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="_id"),
        pydantic.Field(alias="_id", description="The uuid of the function that is used in the database"),
    ] = None
    """
    The uuid of the function that is used in the database
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID of the function
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the function
    """

    gen: typing.Optional[float] = pydantic.Field(default=None)
    """
    Type of the network function - 4: 4G, 5: 5G
    """

    func: typing.Optional[float] = pydantic.Field(default=None)
    """
    0: Core, 1: Radio
    """

    shared: typing.Optional[NsiConnectionsItemCoreShared] = pydantic.Field(default=None)
    """
    Defines if the function can be shared between different slices
    """

    type: typing.Optional[float] = pydantic.Field(default=None)
    """
    0: Virtual, 1: Physical
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Supported location
    """

    ns_list: typing.Optional[typing.List[NsiConnectionsItemCoreNsListItem]] = pydantic.Field(default=None)
    """
    Conditional - If type == Virtual - A list of the NSs that will be part of the slice
    """

    pnf_list: typing.Optional[typing.List[NsiConnectionsItemCorePnfListItem]] = pydantic.Field(default=None)
    """
    Conditional - If type == Physical - A list of the PNFs that will be part of the slice
    """

    ems_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ems-id"),
        pydantic.Field(
            alias="ems-id", description="Optional - Defines the EMS that is responsible for D1&2 configuration"
        ),
    ] = None
    """
    Optional - Defines the EMS that is responsible for D1&2 configuration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
