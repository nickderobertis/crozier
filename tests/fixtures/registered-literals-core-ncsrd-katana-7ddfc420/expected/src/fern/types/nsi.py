

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nsi_connections_item import NsiConnectionsItem
from .nsi_mission_critical_support import NsiMissionCriticalSupport
from .nsi_network_dl_throughput import NsiNetworkDlThroughput
from .nsi_network_ul_throughput import NsiNetworkUlThroughput
from .nsi_ns_list_item import NsiNsListItem
from .nsi_positional_support import NsiPositionalSupport
from .nsi_qos_item import NsiQosItem
from .nsi_ue_dl_throughput import NsiUeDlThroughput
from .nsi_ue_ul_throughput import NsiUeUlThroughput
from .nsi_wim_data import NsiWimData
from .time import Time


class Nsi(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="_id"),
        pydantic.Field(alias="_id", description="The uuid that is used for storing the NSI in the database"),
    ] = None
    """
    The uuid that is used for storing the NSI in the database
    """

    created_at: typing.Optional[float] = None
    deployment_time: typing.Optional[Time] = None
    coverage: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list with all the locations that are part of the slice
    """

    network_dl_throughput: typing_extensions.Annotated[
        typing.Optional[NsiNetworkDlThroughput],
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
        typing.Optional[NsiUeDlThroughput],
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
        typing.Optional[NsiNetworkUlThroughput],
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
        typing.Optional[NsiUeUlThroughput],
        FieldMetadata(alias="ue_UL_throughput"),
        pydantic.Field(
            alias="ue_UL_throughput",
            description="This attribute describes the guaranteed data rate supported by the network slice per UE in uplink",
        ),
    ] = None
    """
    This attribute describes the guaranteed data rate supported by the network slice per UE in uplink
    """

    group_communication_support: typing.Optional[float] = pydantic.Field(default=None)
    """
    0: not available 1: Single Cell Point to Multipoint (SCPTM) 2: Broadcast/Multicast 3: Broadcast/Multicast + SC-PTM
    """

    mtu: typing.Optional[float] = pydantic.Field(default=None)
    """
    Bytes
    """

    mission_critical_support: typing.Optional[NsiMissionCriticalSupport] = pydantic.Field(default=None)
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

    number_of_connections: typing.Optional[float] = pydantic.Field(default=None)
    """
    This attribute describes the maximum number of concurrent sessions supported by the network slice.
    """

    number_of_terminals: typing.Optional[float] = pydantic.Field(default=None)
    """
    This attribute describes the maximum number of concurrent terminals supported by the network slice.
    """

    positional_support: typing.Optional[NsiPositionalSupport] = pydantic.Field(default=None)
    """
    This attribute describes if the network slice provides geo-localization methods or supporting methods.
    """

    radio_spectrum: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Defines the radio spectrum supported by the network slice.
    """

    qos: typing.Optional[typing.List[NsiQosItem]] = pydantic.Field(default=None)
    """
    This attribute defines all the QoS relevant parameters supported by the network slice, based on 3GPP defined standard values (5QIs)
    """

    non_ip_traffic: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="nonIP_traffic"), pydantic.Field(alias="nonIP_traffic")
    ] = None
    device_velocity: typing.Optional[float] = pydantic.Field(default=None)
    """
    1: Stationary: 0 km/h 2: Pedestrian: 0 km/h to 10 km/h 3: Vehicular: 10 km/h to 120 km/h 4: High speed vehicular: 120 km/h to 500 km/h
    """

    terminal_density: typing.Optional[float] = pydantic.Field(default=None)
    """
    maximum number of connected and/or accessible devices per unit area (per km2) supported by the network slice [Number/km^2]
    """

    probe_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of probe ids to be included in the slice
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Init, Peovisioning, Activation, Running or Terminating
    """

    connections: typing.Optional[typing.List[NsiConnectionsItem]] = pydantic.Field(default=None)
    """
    A list of 5G service connections. Each connection contains a core and a radio endpoint. The endpoints are selected from the platform fanctions repository of the Slice Manager
    """

    functions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of all the functions that are used in the slice
    """

    conf_comp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The items components that have been configured by the ems
    """

    ns_list: typing.Optional[typing.List[NsiNsListItem]] = pydantic.Field(default=None)
    """
    A list of the instantiated NSs
    """

    wim_data: typing.Optional[NsiWimData] = pydantic.Field(default=None)
    """
    The data that was sent to WIM
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
