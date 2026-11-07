

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nsi_wim_data_core_connections_item import NsiWimDataCoreConnectionsItem
from .nsi_wim_data_extra_ns_item import NsiWimDataExtraNsItem
from .nsi_wim_data_slice_sla import NsiWimDataSliceSla


class NsiWimData(UniversalBaseModel):
    """
    The data that was sent to WIM
    """

    slice_sla: typing.Optional[NsiWimDataSliceSla] = pydantic.Field(default=None)
    """
    Slice parameteres as defiend in NEST
    """

    core_connections: typing.Optional[typing.List[NsiWimDataCoreConnectionsItem]] = pydantic.Field(default=None)
    """
    List of connections that are part of the slice and must be implemented by the WIM
    """

    extra_ns: typing.Optional[typing.List[NsiWimDataExtraNsItem]] = pydantic.Field(default=None)
    """
    A list of VIMs where the NSs that are not part of the core slice have been instantiated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
