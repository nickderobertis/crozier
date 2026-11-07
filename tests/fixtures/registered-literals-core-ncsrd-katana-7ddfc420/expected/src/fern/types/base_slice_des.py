

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .base_slice_des_deterministic_communication import BaseSliceDesDeterministicCommunication
from .base_slice_des_mission_critical_support import BaseSliceDesMissionCriticalSupport
from .base_slice_des_network_dl_throughput import BaseSliceDesNetworkDlThroughput
from .base_slice_des_network_ul_throughput import BaseSliceDesNetworkUlThroughput
from .base_slice_des_positional_support import BaseSliceDesPositionalSupport
from .base_slice_des_qos_item import BaseSliceDesQosItem
from .base_slice_des_ue_dl_throughput import BaseSliceDesUeDlThroughput
from .base_slice_des_ue_ul_throughput import BaseSliceDesUeUlThroughput


class BaseSliceDes(UniversalBaseModel):
    """
    This is the schema for the core part of the new slice
    """

    base_slice_des_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of the slice descriptor which will be used as base for the gst
    """

    base_slice_des_ref: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reference to an added slice descriptor which will be used as base for the gst
    """

    coverage: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list with all the locations that are part of the slice
    """

    delay_tolerance: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Supported or not supported
    """

    deterministic_communication: typing.Optional[BaseSliceDesDeterministicCommunication] = pydantic.Field(default=None)
    """
    This attribute defines if the network slice supports deterministic communication for periodic user traffic. Periodic traffic refers to the type of traffic with periodic transmissions.
    """

    network_dl_throughput: typing_extensions.Annotated[
        typing.Optional[BaseSliceDesNetworkDlThroughput],
        FieldMetadata(alias="network_DL_throughput"),
        pydantic.Field(
            alias="network_DL_throughput",
            description="The achievable data rate in downlink for the whole network slice (and not per user).",
        ),
    ] = None
    """
    The achievable data rate in downlink for the whole network slice (and not per user).
    """

    ue_dl_throughput: typing_extensions.Annotated[
        typing.Optional[BaseSliceDesUeDlThroughput],
        FieldMetadata(alias="ue_DL_throughput"),
        pydantic.Field(
            alias="ue_DL_throughput",
            description="This attribute describes the guaranteed data rate supported by the network slice per UE in downlink",
        ),
    ] = None
    """
    This attribute describes the guaranteed data rate supported by the network slice per UE in downlink
    """

    network_ul_throughput: typing_extensions.Annotated[
        typing.Optional[BaseSliceDesNetworkUlThroughput],
        FieldMetadata(alias="network_UL_throughput"),
        pydantic.Field(
            alias="network_UL_throughput",
            description="The achievable data rate in uplink for the whole network slice (and not per user).",
        ),
    ] = None
    """
    The achievable data rate in uplink for the whole network slice (and not per user).
    """

    ue_ul_throughput: typing_extensions.Annotated[
        typing.Optional[BaseSliceDesUeUlThroughput],
        FieldMetadata(alias="ue_UL_throughput"),
        pydantic.Field(
            alias="ue_UL_throughput",
            description="This attribute describes the guaranteed data rate supported by the network slice per UE in uplink",
        ),
    ] = None
    """
    This attribute describes the guaranteed data rate supported by the network slice per UE in uplink
    """

    group_communication_support: typing.Optional[int] = pydantic.Field(default=None)
    """
    0: not available 1: Single Cell Point to Multipoint (SCPTM) 2: Broadcast/Multicast 3: Broadcast/Multicast + SC-PTM
    """

    isolation: typing.Optional[float] = pydantic.Field(default=None)
    """
     A network slice instance may be fully or partly, isolated from another network slice instance. 0: No Isolation 1: Core Isolation 2: RAN Isolation 3: Both Isolation
    """

    mtu: typing.Optional[int] = pydantic.Field(default=None)
    """
    Bytes
    """

    mission_critical_support: typing.Optional[BaseSliceDesMissionCriticalSupport] = pydantic.Field(default=None)
    """
    Mission-critical (MC) leads to a priority of the network slice relative to others, for C-plane and U-plane decisions.
    """

    mmtel_support: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This attribute describes whether the network slice supports IP Multimedia Subsystem (IMS) and Multimedia Telephony Service MMTel.
    """

    nb_iot: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This parameter describes whether NB-IoT is supported in the network slice.
    """

    number_of_connections: typing.Optional[int] = pydantic.Field(default=None)
    """
    This attribute describes the maximum number of concurrent sessions supported by the network slice.
    """

    number_of_terminals: typing.Optional[int] = pydantic.Field(default=None)
    """
    This attribute describes the maximum number of concurrent terminals supported by the network slice.
    """

    positional_support: typing.Optional[BaseSliceDesPositionalSupport] = pydantic.Field(default=None)
    """
    This attribute describes if the network slice provides geo-localization methods or supporting methods.
    """

    radio_spectrum: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Defines the radio spectrum supported by the network slice.
    """

    simultaneous_nsi: typing.Optional[int] = pydantic.Field(default=None)
    """
    0: Can be used with any network slice 1: Can be used with network slices with same SST value 2: Can be used with any network slice with same SD value 3: Cannot be used with another network slice 4-15: operator defined class
    """

    qos: typing.Optional[typing.List[BaseSliceDesQosItem]] = pydantic.Field(default=None)
    """
    This attribute defines all the QoS relevant parameters supported by the network slice, based on 3GPP defined standard values (5QIs)
    """

    non_ip_traffic: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="nonIP_traffic"), pydantic.Field(alias="nonIP_traffic")
    ] = None
    device_velocity: typing.Optional[int] = pydantic.Field(default=None)
    """
    1: Stationary: 0 km/h 2: Pedestrian: 0 km/h to 10 km/h 3: Vehicular: 10 km/h to 120 km/h 4: High speed vehicular: 120 km/h to 500 km/h
    """

    terminal_density: typing.Optional[int] = pydantic.Field(default=None)
    """
    maximum number of connected and/or accessible devices per unit area (per km2) supported by the network slice [Number/km^2]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
