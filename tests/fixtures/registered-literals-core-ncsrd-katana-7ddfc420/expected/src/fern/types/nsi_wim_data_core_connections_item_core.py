

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nsi_wim_data_core_connections_item_core_ns_item import NsiWimDataCoreConnectionsItemCoreNsItem
from .nsi_wim_data_core_connections_item_core_pnf_item import NsiWimDataCoreConnectionsItemCorePnfItem


class NsiWimDataCoreConnectionsItemCore(UniversalBaseModel):
    """
    The core part of the radio connection
    """

    ns: typing.Optional[typing.List[NsiWimDataCoreConnectionsItemCoreNsItem]] = pydantic.Field(default=None)
    """
    A list of VIMs where the NSs have been instantiated
    """

    pnf: typing.Optional[typing.List[NsiWimDataCoreConnectionsItemCorePnfItem]] = pydantic.Field(default=None)
    """
    A list of the PNFs that are part of the slice
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
