

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NsiQosItem(UniversalBaseModel):
    """
    Refers to 5QI defined in https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3144
    """

    qi: typing.Optional[float] = pydantic.Field(default=None)
    """
    Based on the table of defined 5QI by 3GPP
    """

    resource_type: typing.Optional[float] = pydantic.Field(default=None)
    """
    0: GBR (Mission Critical Video user plane) 1: Delay critical GBR (Intelligent Transport Systems) 2: Non-GBR (Voice, AR)
    """

    priority_level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Associated with 5G QoS characteristics indicates a priority in scheduling resources among QoS Flows.
    """

    packet_delay_budget: typing.Optional[float] = pydantic.Field(default=None)
    """
    The Packet Delay Budget (PDB) defines an upper bound for the time that a packet may be delayed between the UE and the UPF [Seconds].
    """

    packet_error_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The Packet Error Rate (PER) defines an upper bound for the rate of packets that are not successfully delivered by the corresponding receiver [percentage].
    """

    jitter: typing.Optional[float] = pydantic.Field(default=None)
    """
    Jitter is defined as a variation in the delay of received packets [Seconds].
    """

    max_packet_loss_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
     the maximum rate for lost packets of the QoS flow that can be tolerated in the uplink (UL) and downlink (DL) direction [percentage.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
