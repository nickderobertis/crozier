

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_usage import DeviceUsage
from .tower_location import TowerLocation


class DeviceSession(UniversalBaseModel):
    apn: typing.Optional[str] = None
    bars: typing.Optional[int] = None
    bearer: typing.Optional[str] = None
    bssid: typing.Optional[str] = None
    cell: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cell ID where the session originated and quality ("mcc,mnc,lac,cellid")
    """

    continuous: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Was this a continuous connection?
    """

    device: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device UID
    """

    events: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of events routed
    """

    failed_connects: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of failed connection attempts in the prior session
    """

    fleets: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array of Fleet UIDs
    """

    hp_cycles_data: typing.Optional[int] = None
    hp_cycles_gps: typing.Optional[int] = None
    hp_cycles_total: typing.Optional[int] = None
    hp_secs_data: typing.Optional[int] = None
    hp_secs_gps: typing.Optional[int] = None
    hp_secs_total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of seconds in high power mode
    """

    iccid: typing.Optional[str] = None
    ip: typing.Optional[str] = None
    moved: typing.Optional[int] = None
    orientation: typing.Optional[str] = None
    penalty_secs: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of seconds in penalty in the prior session
    """

    period: typing.Optional[DeviceUsage] = None
    power_charging: typing.Optional[bool] = None
    power_mah: typing.Optional[float] = None
    power_primary: typing.Optional[bool] = None
    power_usb: typing.Optional[bool] = None
    product: typing.Optional[str] = pydantic.Field(default=None)
    """
    Product UID
    """

    rat: typing.Optional[str] = None
    rsrp: typing.Optional[int] = None
    rsrq: typing.Optional[int] = None
    rssi: typing.Optional[int] = None
    scan: typing.Optional[str] = None
    session: typing.Optional[str] = pydantic.Field(default=None)
    """
    Session UID
    """

    session_began: typing.Optional[int] = pydantic.Field(default=None)
    """
    UNIX timestamp of session start
    """

    session_ended: typing.Optional[int] = pydantic.Field(default=None)
    """
    UNIX timestamp of session end
    """

    sinr: typing.Optional[int] = None
    sn: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device Serial Number
    """

    ssid: typing.Optional[str] = None
    temp: typing.Optional[float] = None
    tls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Was TLS used?
    """

    tower: typing.Optional[TowerLocation] = None
    transport: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of network transport
    """

    tri: typing.Optional[TowerLocation] = None
    triangulate: typing.Optional[typing.Dict[str, typing.Any]] = None
    usage_actual: typing.Optional[bool] = None
    voltage: typing.Optional[float] = None
    when: typing.Optional[int] = pydantic.Field(default=None)
    """
    Last known capture time of a note routed through this session in Unix timestamp
    """

    where: typing.Optional[str] = pydantic.Field(default=None)
    """
    Open Location Code from last GPS location
    """

    where_country: typing.Optional[str] = None
    where_lat: typing.Optional[float] = None
    where_location: typing.Optional[str] = None
    where_lon: typing.Optional[float] = None
    where_timezone: typing.Optional[str] = None
    where_when: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp of last GPS location
    """

    why_session_closed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason for session closing
    """

    why_session_opened: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason for session opening
    """

    work: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp of the last time work was done for this session
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
