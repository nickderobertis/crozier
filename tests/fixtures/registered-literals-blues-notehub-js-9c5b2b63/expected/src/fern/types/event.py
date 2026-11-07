

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Event(UniversalBaseModel):
    app: typing.Optional[str] = pydantic.Field(default=None)
    """
    App UID (globally unique)
    """

    bars: typing.Optional[int] = pydantic.Field(default=None)
    """
    Bars. Only available on _session.qo events.
    """

    best_country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country
    """

    best_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The device serial number, or the DeviceUID if the serial number is not set
    """

    best_lat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Latitude
    """

    best_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location
    """

    best_location_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    One of "gps", "triangulated", or "tower"
    """

    best_location_when: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp
    """

    best_lon: typing.Optional[float] = pydantic.Field(default=None)
    """
    Longitude
    """

    best_timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone
    """

    body: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A JSON object containing event details
    """

    bssid: typing.Optional[str] = pydantic.Field(default=None)
    """
    BSSID. Only available on _session.qo events.
    """

    device: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device UID (globally unique)
    """

    environment: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Routed environment variables beginning with "$". Only available on _session.qo events.
    """

    event: typing.Optional[str] = pydantic.Field(default=None)
    """
    Event UID (globally unique)
    """

    file: typing.Optional[str] = pydantic.Field(default=None)
    """
    The notefile associated with this event
    """

    moved: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of times the device was sensed to have moved between the last session and this session. Only available on _session.qo events.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    The note ID in the notefile
    """

    ordering_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ordering code. Only available on _session.qo events.
    """

    orientation: typing.Optional[str] = pydantic.Field(default=None)
    """
    The orientation of the device. Only available on _session.qo events.
    """

    payload: typing.Optional[str] = pydantic.Field(default=None)
    """
    A base64-encoded binary payload
    """

    product: typing.Optional[str] = pydantic.Field(default=None)
    """
    Product UID (globally unique)
    """

    rat: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rat. Only available on _session.qo events.
    """

    received: typing.Optional[float] = pydantic.Field(default=None)
    """
    The unix timestamp when the event was received
    """

    req: typing.Optional[str] = pydantic.Field(default=None)
    """
    The notecard request
    """

    rsrp: typing.Optional[int] = pydantic.Field(default=None)
    """
    RSRP. Only available on _session.qo events.
    """

    rsrq: typing.Optional[int] = pydantic.Field(default=None)
    """
    RSRQ. Only available on _session.qo events.
    """

    rssi: typing.Optional[int] = pydantic.Field(default=None)
    """
    Received Signal Strength Indicator (RSSI) is an estimated measurement of how well a device can receive signals. Only available on _session.qo events.
    """

    sensor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sensor UID, for events originating from a sensor attached to the device
    """

    session: typing.Optional[str] = pydantic.Field(default=None)
    """
    Session UID (globally unique)
    """

    sinr: typing.Optional[int] = pydantic.Field(default=None)
    """
    SINR. Only available on _session.qo events.
    """

    sku: typing.Optional[str] = pydantic.Field(default=None)
    """
    SKU. Only available on _session.qo events.
    """

    sn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The device serial number
    """

    ssid: typing.Optional[str] = pydantic.Field(default=None)
    """
    SSID. Only available on _session.qo events.
    """

    temp: typing.Optional[float] = pydantic.Field(default=None)
    """
    Device temperature. Only available on _session.qo events.
    """

    tls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether TLS was used on the connection between the device and notehub. Only available on _session.qo events.
    """

    tower_country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country
    """

    tower_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tower ID
    """

    tower_lat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Latitude
    """

    tower_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location
    """

    tower_lon: typing.Optional[float] = pydantic.Field(default=None)
    """
    Longitude
    """

    tower_timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone
    """

    tower_when: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp
    """

    transport: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transport used for this event, e.g., "cellular", "wifi", ", etc.
    """

    tri_country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country
    """

    tri_lat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Latitude
    """

    tri_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location
    """

    tri_lon: typing.Optional[float] = pydantic.Field(default=None)
    """
    Longitude
    """

    tri_points: typing.Optional[int] = pydantic.Field(default=None)
    """
    Triangulation points
    """

    tri_timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone
    """

    tri_when: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp
    """

    updates: typing.Optional[int] = None
    voltage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Device voltage. Only available on _session.qo events.
    """

    when: typing.Optional[int] = pydantic.Field(default=None)
    """
    When the event was captured on the device
    """

    when_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    Millisecond-accurate Unix epoch timestamp for when the event was captured on the device
    """

    where_country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country
    """

    where_lat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Latitude
    """

    where_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location
    """

    where_lon: typing.Optional[float] = pydantic.Field(default=None)
    """
    Longitude
    """

    where_olc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Open Location Code
    """

    where_timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone
    """

    where_when: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
