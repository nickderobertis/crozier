

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nsi_wim_data_slice_sla_network_dl_throughput import NsiWimDataSliceSlaNetworkDlThroughput
from .nsi_wim_data_slice_sla_network_ul_throughput import NsiWimDataSliceSlaNetworkUlThroughput


class NsiWimDataSliceSla(UniversalBaseModel):
    """
    Slice parameteres as defiend in NEST
    """

    network_dl_throughput: typing_extensions.Annotated[
        typing.Optional[NsiWimDataSliceSlaNetworkDlThroughput],
        FieldMetadata(alias="network_DL_throughput"),
        pydantic.Field(
            alias="network_DL_throughput",
            description="The achievable data rate in downlink for the whole network slice (and not per user).",
        ),
    ] = None
    """
    The achievable data rate in downlink for the whole network slice (and not per user).
    """

    network_ul_throughput: typing_extensions.Annotated[
        typing.Optional[NsiWimDataSliceSlaNetworkUlThroughput],
        FieldMetadata(alias="network_UL_throughput"),
        pydantic.Field(
            alias="network_UL_throughput",
            description="The achievable data rate in uplink for the whole network slice (and not per user).",
        ),
    ] = None
    """
    The achievable data rate in uplink for the whole network slice (and not per user).
    """

    mtu: typing.Optional[float] = pydantic.Field(default=None)
    """
    Bytes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
