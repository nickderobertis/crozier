

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nsi_ns_list_item_nsd_info import NsiNsListItemNsdInfo
from .nsi_ns_list_item_placement_loc import NsiNsListItemPlacementLoc


class NsiNsListItem(UniversalBaseModel):
    """
    A Network Service
    """

    nsd_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nsd-id"),
        pydantic.Field(alias="nsd-id", description="The NSD id as defined on the NFVO"),
    ] = None
    """
    The NSD id as defined on the NFVO
    """

    ns_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ns-name"),
        pydantic.Field(alias="ns-name", description="The name of the NS"),
    ] = None
    """
    The name of the NS
    """

    placement: typing.Optional[float] = pydantic.Field(default=None)
    """
    1: Core, 2: Edge
    """

    optional: typing.Optional[bool] = None
    nsd_info: typing_extensions.Annotated[
        typing.Optional[NsiNsListItemNsdInfo],
        FieldMetadata(alias="nsd-info"),
        pydantic.Field(alias="nsd-info", description="Information about the NS Descriptor"),
    ] = None
    """
    Information about the NS Descriptor
    """

    placement_loc: typing.Optional[NsiNsListItemPlacementLoc] = pydantic.Field(default=None)
    """
    Detailed info regarding the placement of the NS
    """

    vims: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of VIMs used for the NS
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
