

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.device_usage import DeviceUsage
from ..types.tower_location import TowerLocation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExternalDevicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_event_ext_device(
        self,
        product_uid: str,
        device_uid: str,
        *,
        app: typing.Optional[str] = OMIT,
        bars: typing.Optional[int] = OMIT,
        best_country: typing.Optional[str] = OMIT,
        best_id: typing.Optional[str] = OMIT,
        best_lat: typing.Optional[float] = OMIT,
        best_location: typing.Optional[str] = OMIT,
        best_location_type: typing.Optional[str] = OMIT,
        best_location_when: typing.Optional[int] = OMIT,
        best_lon: typing.Optional[float] = OMIT,
        best_timezone: typing.Optional[str] = OMIT,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        bssid: typing.Optional[str] = OMIT,
        device: typing.Optional[str] = OMIT,
        environment: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        event: typing.Optional[str] = OMIT,
        file: typing.Optional[str] = OMIT,
        moved: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        ordering_code: typing.Optional[str] = OMIT,
        orientation: typing.Optional[str] = OMIT,
        payload: typing.Optional[str] = OMIT,
        product: typing.Optional[str] = OMIT,
        rat: typing.Optional[str] = OMIT,
        received: typing.Optional[float] = OMIT,
        req: typing.Optional[str] = OMIT,
        rsrp: typing.Optional[int] = OMIT,
        rsrq: typing.Optional[int] = OMIT,
        rssi: typing.Optional[int] = OMIT,
        sensor: typing.Optional[str] = OMIT,
        session: typing.Optional[str] = OMIT,
        sinr: typing.Optional[int] = OMIT,
        sku: typing.Optional[str] = OMIT,
        sn: typing.Optional[str] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        temp: typing.Optional[float] = OMIT,
        tls: typing.Optional[bool] = OMIT,
        tower_country: typing.Optional[str] = OMIT,
        tower_id: typing.Optional[str] = OMIT,
        tower_lat: typing.Optional[float] = OMIT,
        tower_location: typing.Optional[str] = OMIT,
        tower_lon: typing.Optional[float] = OMIT,
        tower_timezone: typing.Optional[str] = OMIT,
        tower_when: typing.Optional[int] = OMIT,
        transport: typing.Optional[str] = OMIT,
        tri_country: typing.Optional[str] = OMIT,
        tri_lat: typing.Optional[float] = OMIT,
        tri_location: typing.Optional[str] = OMIT,
        tri_lon: typing.Optional[float] = OMIT,
        tri_points: typing.Optional[int] = OMIT,
        tri_timezone: typing.Optional[str] = OMIT,
        tri_when: typing.Optional[int] = OMIT,
        updates: typing.Optional[int] = OMIT,
        voltage: typing.Optional[float] = OMIT,
        when: typing.Optional[int] = OMIT,
        when_ms: typing.Optional[int] = OMIT,
        where_country: typing.Optional[str] = OMIT,
        where_lat: typing.Optional[float] = OMIT,
        where_location: typing.Optional[str] = OMIT,
        where_lon: typing.Optional[float] = OMIT,
        where_olc: typing.Optional[str] = OMIT,
        where_timezone: typing.Optional[str] = OMIT,
        where_when: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Creates an event using specified webhook

        Parameters
        ----------
        product_uid : str

        device_uid : str

        app : typing.Optional[str]
            App UID (globally unique)

        bars : typing.Optional[int]
            Bars. Only available on _session.qo events.

        best_country : typing.Optional[str]
            Country

        best_id : typing.Optional[str]
            The device serial number, or the DeviceUID if the serial number is not set

        best_lat : typing.Optional[float]
            Latitude

        best_location : typing.Optional[str]
            Location

        best_location_type : typing.Optional[str]
            One of "gps", "triangulated", or "tower"

        best_location_when : typing.Optional[int]
            Unix timestamp

        best_lon : typing.Optional[float]
            Longitude

        best_timezone : typing.Optional[str]
            Timezone

        body : typing.Optional[typing.Dict[str, typing.Any]]
            A JSON object containing event details

        bssid : typing.Optional[str]
            BSSID. Only available on _session.qo events.

        device : typing.Optional[str]
            Device UID (globally unique)

        environment : typing.Optional[typing.Dict[str, typing.Any]]
            Routed environment variables beginning with "$". Only available on _session.qo events.

        event : typing.Optional[str]
            Event UID (globally unique)

        file : typing.Optional[str]
            The notefile associated with this event

        moved : typing.Optional[int]
            The number of times the device was sensed to have moved between the last session and this session. Only available on _session.qo events.

        note : typing.Optional[str]
            The note ID in the notefile

        ordering_code : typing.Optional[str]
            Ordering code. Only available on _session.qo events.

        orientation : typing.Optional[str]
            The orientation of the device. Only available on _session.qo events.

        payload : typing.Optional[str]
            A base64-encoded binary payload

        product : typing.Optional[str]
            Product UID (globally unique)

        rat : typing.Optional[str]
            Rat. Only available on _session.qo events.

        received : typing.Optional[float]
            The unix timestamp when the event was received

        req : typing.Optional[str]
            The notecard request

        rsrp : typing.Optional[int]
            RSRP. Only available on _session.qo events.

        rsrq : typing.Optional[int]
            RSRQ. Only available on _session.qo events.

        rssi : typing.Optional[int]
            Received Signal Strength Indicator (RSSI) is an estimated measurement of how well a device can receive signals. Only available on _session.qo events.

        sensor : typing.Optional[str]
            Sensor UID, for events originating from a sensor attached to the device

        session : typing.Optional[str]
            Session UID (globally unique)

        sinr : typing.Optional[int]
            SINR. Only available on _session.qo events.

        sku : typing.Optional[str]
            SKU. Only available on _session.qo events.

        sn : typing.Optional[str]
            The device serial number

        ssid : typing.Optional[str]
            SSID. Only available on _session.qo events.

        temp : typing.Optional[float]
            Device temperature. Only available on _session.qo events.

        tls : typing.Optional[bool]
            Whether TLS was used on the connection between the device and notehub. Only available on _session.qo events.

        tower_country : typing.Optional[str]
            Country

        tower_id : typing.Optional[str]
            Tower ID

        tower_lat : typing.Optional[float]
            Latitude

        tower_location : typing.Optional[str]
            Location

        tower_lon : typing.Optional[float]
            Longitude

        tower_timezone : typing.Optional[str]
            Timezone

        tower_when : typing.Optional[int]
            Unix timestamp

        transport : typing.Optional[str]
            The transport used for this event, e.g., "cellular", "wifi", ", etc.

        tri_country : typing.Optional[str]
            Country

        tri_lat : typing.Optional[float]
            Latitude

        tri_location : typing.Optional[str]
            Location

        tri_lon : typing.Optional[float]
            Longitude

        tri_points : typing.Optional[int]
            Triangulation points

        tri_timezone : typing.Optional[str]
            Timezone

        tri_when : typing.Optional[int]
            Unix timestamp

        updates : typing.Optional[int]

        voltage : typing.Optional[float]
            Device voltage. Only available on _session.qo events.

        when : typing.Optional[int]
            When the event was captured on the device

        when_ms : typing.Optional[int]
            Millisecond-accurate Unix epoch timestamp for when the event was captured on the device

        where_country : typing.Optional[str]
            Country

        where_lat : typing.Optional[float]
            Latitude

        where_location : typing.Optional[str]
            Location

        where_lon : typing.Optional[float]
            Longitude

        where_olc : typing.Optional[str]
            Open Location Code

        where_timezone : typing.Optional[str]
            Timezone

        where_when : typing.Optional[int]
            Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/ext-devices/{encode_path_param(device_uid)}/event",
            method="POST",
            json={
                "app": app,
                "bars": bars,
                "best_country": best_country,
                "best_id": best_id,
                "best_lat": best_lat,
                "best_location": best_location,
                "best_location_type": best_location_type,
                "best_location_when": best_location_when,
                "best_lon": best_lon,
                "best_timezone": best_timezone,
                "body": body,
                "bssid": bssid,
                "device": device,
                "environment": environment,
                "event": event,
                "file": file,
                "moved": moved,
                "note": note,
                "ordering_code": ordering_code,
                "orientation": orientation,
                "payload": payload,
                "product": product,
                "rat": rat,
                "received": received,
                "req": req,
                "rsrp": rsrp,
                "rsrq": rsrq,
                "rssi": rssi,
                "sensor": sensor,
                "session": session,
                "sinr": sinr,
                "sku": sku,
                "sn": sn,
                "ssid": ssid,
                "temp": temp,
                "tls": tls,
                "tower_country": tower_country,
                "tower_id": tower_id,
                "tower_lat": tower_lat,
                "tower_location": tower_location,
                "tower_lon": tower_lon,
                "tower_timezone": tower_timezone,
                "tower_when": tower_when,
                "transport": transport,
                "tri_country": tri_country,
                "tri_lat": tri_lat,
                "tri_location": tri_location,
                "tri_lon": tri_lon,
                "tri_points": tri_points,
                "tri_timezone": tri_timezone,
                "tri_when": tri_when,
                "updates": updates,
                "voltage": voltage,
                "when": when,
                "when_ms": when_ms,
                "where_country": where_country,
                "where_lat": where_lat,
                "where_location": where_location,
                "where_lon": where_lon,
                "where_olc": where_olc,
                "where_timezone": where_timezone,
                "where_when": where_when,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ext_device_session_close(
        self,
        product_uid: str,
        device_uid: str,
        *,
        apn: typing.Optional[str] = OMIT,
        bars: typing.Optional[int] = OMIT,
        bearer: typing.Optional[str] = OMIT,
        bssid: typing.Optional[str] = OMIT,
        cell: typing.Optional[str] = OMIT,
        continuous: typing.Optional[bool] = OMIT,
        device: typing.Optional[str] = OMIT,
        events: typing.Optional[int] = OMIT,
        failed_connects: typing.Optional[int] = OMIT,
        fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        hp_cycles_data: typing.Optional[int] = OMIT,
        hp_cycles_gps: typing.Optional[int] = OMIT,
        hp_cycles_total: typing.Optional[int] = OMIT,
        hp_secs_data: typing.Optional[int] = OMIT,
        hp_secs_gps: typing.Optional[int] = OMIT,
        hp_secs_total: typing.Optional[int] = OMIT,
        iccid: typing.Optional[str] = OMIT,
        ip: typing.Optional[str] = OMIT,
        moved: typing.Optional[int] = OMIT,
        orientation: typing.Optional[str] = OMIT,
        penalty_secs: typing.Optional[int] = OMIT,
        period: typing.Optional[DeviceUsage] = OMIT,
        power_charging: typing.Optional[bool] = OMIT,
        power_mah: typing.Optional[float] = OMIT,
        power_primary: typing.Optional[bool] = OMIT,
        power_usb: typing.Optional[bool] = OMIT,
        product: typing.Optional[str] = OMIT,
        rat: typing.Optional[str] = OMIT,
        rsrp: typing.Optional[int] = OMIT,
        rsrq: typing.Optional[int] = OMIT,
        rssi: typing.Optional[int] = OMIT,
        scan: typing.Optional[str] = OMIT,
        session: typing.Optional[str] = OMIT,
        session_began: typing.Optional[int] = OMIT,
        session_ended: typing.Optional[int] = OMIT,
        sinr: typing.Optional[int] = OMIT,
        sn: typing.Optional[str] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        temp: typing.Optional[float] = OMIT,
        tls: typing.Optional[bool] = OMIT,
        tower: typing.Optional[TowerLocation] = OMIT,
        transport: typing.Optional[str] = OMIT,
        tri: typing.Optional[TowerLocation] = OMIT,
        triangulate: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        usage_actual: typing.Optional[bool] = OMIT,
        voltage: typing.Optional[float] = OMIT,
        when: typing.Optional[int] = OMIT,
        where: typing.Optional[str] = OMIT,
        where_country: typing.Optional[str] = OMIT,
        where_lat: typing.Optional[float] = OMIT,
        where_location: typing.Optional[str] = OMIT,
        where_lon: typing.Optional[float] = OMIT,
        where_timezone: typing.Optional[str] = OMIT,
        where_when: typing.Optional[int] = OMIT,
        why_session_closed: typing.Optional[str] = OMIT,
        why_session_opened: typing.Optional[str] = OMIT,
        work: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Closes the session for the specified device if open

        Parameters
        ----------
        product_uid : str

        device_uid : str

        apn : typing.Optional[str]

        bars : typing.Optional[int]

        bearer : typing.Optional[str]

        bssid : typing.Optional[str]

        cell : typing.Optional[str]
            Cell ID where the session originated and quality ("mcc,mnc,lac,cellid")

        continuous : typing.Optional[bool]
            Was this a continuous connection?

        device : typing.Optional[str]
            Device UID

        events : typing.Optional[int]
            Number of events routed

        failed_connects : typing.Optional[int]
            Number of failed connection attempts in the prior session

        fleets : typing.Optional[typing.Sequence[str]]
            Array of Fleet UIDs

        hp_cycles_data : typing.Optional[int]

        hp_cycles_gps : typing.Optional[int]

        hp_cycles_total : typing.Optional[int]

        hp_secs_data : typing.Optional[int]

        hp_secs_gps : typing.Optional[int]

        hp_secs_total : typing.Optional[int]
            Total number of seconds in high power mode

        iccid : typing.Optional[str]

        ip : typing.Optional[str]

        moved : typing.Optional[int]

        orientation : typing.Optional[str]

        penalty_secs : typing.Optional[int]
            Number of seconds in penalty in the prior session

        period : typing.Optional[DeviceUsage]

        power_charging : typing.Optional[bool]

        power_mah : typing.Optional[float]

        power_primary : typing.Optional[bool]

        power_usb : typing.Optional[bool]

        product : typing.Optional[str]
            Product UID

        rat : typing.Optional[str]

        rsrp : typing.Optional[int]

        rsrq : typing.Optional[int]

        rssi : typing.Optional[int]

        scan : typing.Optional[str]

        session : typing.Optional[str]
            Session UID

        session_began : typing.Optional[int]
            UNIX timestamp of session start

        session_ended : typing.Optional[int]
            UNIX timestamp of session end

        sinr : typing.Optional[int]

        sn : typing.Optional[str]
            Device Serial Number

        ssid : typing.Optional[str]

        temp : typing.Optional[float]

        tls : typing.Optional[bool]
            Was TLS used?

        tower : typing.Optional[TowerLocation]

        transport : typing.Optional[str]
            Type of network transport

        tri : typing.Optional[TowerLocation]

        triangulate : typing.Optional[typing.Dict[str, typing.Any]]

        usage_actual : typing.Optional[bool]

        voltage : typing.Optional[float]

        when : typing.Optional[int]
            Last known capture time of a note routed through this session in Unix timestamp

        where : typing.Optional[str]
            Open Location Code from last GPS location

        where_country : typing.Optional[str]

        where_lat : typing.Optional[float]

        where_location : typing.Optional[str]

        where_lon : typing.Optional[float]

        where_timezone : typing.Optional[str]

        where_when : typing.Optional[int]
            Unix timestamp of last GPS location

        why_session_closed : typing.Optional[str]
            Reason for session closing

        why_session_opened : typing.Optional[str]
            Reason for session opening

        work : typing.Optional[int]
            Unix timestamp of the last time work was done for this session

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/ext-devices/{encode_path_param(device_uid)}/session/close",
            method="POST",
            json={
                "apn": apn,
                "bars": bars,
                "bearer": bearer,
                "bssid": bssid,
                "cell": cell,
                "continuous": continuous,
                "device": device,
                "events": events,
                "failed_connects": failed_connects,
                "fleets": fleets,
                "hp_cycles_data": hp_cycles_data,
                "hp_cycles_gps": hp_cycles_gps,
                "hp_cycles_total": hp_cycles_total,
                "hp_secs_data": hp_secs_data,
                "hp_secs_gps": hp_secs_gps,
                "hp_secs_total": hp_secs_total,
                "iccid": iccid,
                "ip": ip,
                "moved": moved,
                "orientation": orientation,
                "penalty_secs": penalty_secs,
                "period": convert_and_respect_annotation_metadata(
                    object_=period, annotation=DeviceUsage, direction="write"
                ),
                "power_charging": power_charging,
                "power_mah": power_mah,
                "power_primary": power_primary,
                "power_usb": power_usb,
                "product": product,
                "rat": rat,
                "rsrp": rsrp,
                "rsrq": rsrq,
                "rssi": rssi,
                "scan": scan,
                "session": session,
                "session_began": session_began,
                "session_ended": session_ended,
                "sinr": sinr,
                "sn": sn,
                "ssid": ssid,
                "temp": temp,
                "tls": tls,
                "tower": convert_and_respect_annotation_metadata(
                    object_=tower, annotation=TowerLocation, direction="write"
                ),
                "transport": transport,
                "tri": convert_and_respect_annotation_metadata(
                    object_=tri, annotation=TowerLocation, direction="write"
                ),
                "triangulate": triangulate,
                "usage_actual": usage_actual,
                "voltage": voltage,
                "when": when,
                "where": where,
                "where_country": where_country,
                "where_lat": where_lat,
                "where_location": where_location,
                "where_lon": where_lon,
                "where_timezone": where_timezone,
                "where_when": where_when,
                "why_session_closed": why_session_closed,
                "why_session_opened": why_session_opened,
                "work": work,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ext_device_session_open(
        self,
        product_uid: str,
        device_uid: str,
        *,
        apn: typing.Optional[str] = OMIT,
        bars: typing.Optional[int] = OMIT,
        bearer: typing.Optional[str] = OMIT,
        bssid: typing.Optional[str] = OMIT,
        cell: typing.Optional[str] = OMIT,
        continuous: typing.Optional[bool] = OMIT,
        device: typing.Optional[str] = OMIT,
        events: typing.Optional[int] = OMIT,
        failed_connects: typing.Optional[int] = OMIT,
        fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        hp_cycles_data: typing.Optional[int] = OMIT,
        hp_cycles_gps: typing.Optional[int] = OMIT,
        hp_cycles_total: typing.Optional[int] = OMIT,
        hp_secs_data: typing.Optional[int] = OMIT,
        hp_secs_gps: typing.Optional[int] = OMIT,
        hp_secs_total: typing.Optional[int] = OMIT,
        iccid: typing.Optional[str] = OMIT,
        ip: typing.Optional[str] = OMIT,
        moved: typing.Optional[int] = OMIT,
        orientation: typing.Optional[str] = OMIT,
        penalty_secs: typing.Optional[int] = OMIT,
        period: typing.Optional[DeviceUsage] = OMIT,
        power_charging: typing.Optional[bool] = OMIT,
        power_mah: typing.Optional[float] = OMIT,
        power_primary: typing.Optional[bool] = OMIT,
        power_usb: typing.Optional[bool] = OMIT,
        product: typing.Optional[str] = OMIT,
        rat: typing.Optional[str] = OMIT,
        rsrp: typing.Optional[int] = OMIT,
        rsrq: typing.Optional[int] = OMIT,
        rssi: typing.Optional[int] = OMIT,
        scan: typing.Optional[str] = OMIT,
        session: typing.Optional[str] = OMIT,
        session_began: typing.Optional[int] = OMIT,
        session_ended: typing.Optional[int] = OMIT,
        sinr: typing.Optional[int] = OMIT,
        sn: typing.Optional[str] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        temp: typing.Optional[float] = OMIT,
        tls: typing.Optional[bool] = OMIT,
        tower: typing.Optional[TowerLocation] = OMIT,
        transport: typing.Optional[str] = OMIT,
        tri: typing.Optional[TowerLocation] = OMIT,
        triangulate: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        usage_actual: typing.Optional[bool] = OMIT,
        voltage: typing.Optional[float] = OMIT,
        when: typing.Optional[int] = OMIT,
        where: typing.Optional[str] = OMIT,
        where_country: typing.Optional[str] = OMIT,
        where_lat: typing.Optional[float] = OMIT,
        where_location: typing.Optional[str] = OMIT,
        where_lon: typing.Optional[float] = OMIT,
        where_timezone: typing.Optional[str] = OMIT,
        where_when: typing.Optional[int] = OMIT,
        why_session_closed: typing.Optional[str] = OMIT,
        why_session_opened: typing.Optional[str] = OMIT,
        work: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Create a Session for the specified device.  | If a session is currently open it will be closed and a new one opened.

        Parameters
        ----------
        product_uid : str

        device_uid : str

        apn : typing.Optional[str]

        bars : typing.Optional[int]

        bearer : typing.Optional[str]

        bssid : typing.Optional[str]

        cell : typing.Optional[str]
            Cell ID where the session originated and quality ("mcc,mnc,lac,cellid")

        continuous : typing.Optional[bool]
            Was this a continuous connection?

        device : typing.Optional[str]
            Device UID

        events : typing.Optional[int]
            Number of events routed

        failed_connects : typing.Optional[int]
            Number of failed connection attempts in the prior session

        fleets : typing.Optional[typing.Sequence[str]]
            Array of Fleet UIDs

        hp_cycles_data : typing.Optional[int]

        hp_cycles_gps : typing.Optional[int]

        hp_cycles_total : typing.Optional[int]

        hp_secs_data : typing.Optional[int]

        hp_secs_gps : typing.Optional[int]

        hp_secs_total : typing.Optional[int]
            Total number of seconds in high power mode

        iccid : typing.Optional[str]

        ip : typing.Optional[str]

        moved : typing.Optional[int]

        orientation : typing.Optional[str]

        penalty_secs : typing.Optional[int]
            Number of seconds in penalty in the prior session

        period : typing.Optional[DeviceUsage]

        power_charging : typing.Optional[bool]

        power_mah : typing.Optional[float]

        power_primary : typing.Optional[bool]

        power_usb : typing.Optional[bool]

        product : typing.Optional[str]
            Product UID

        rat : typing.Optional[str]

        rsrp : typing.Optional[int]

        rsrq : typing.Optional[int]

        rssi : typing.Optional[int]

        scan : typing.Optional[str]

        session : typing.Optional[str]
            Session UID

        session_began : typing.Optional[int]
            UNIX timestamp of session start

        session_ended : typing.Optional[int]
            UNIX timestamp of session end

        sinr : typing.Optional[int]

        sn : typing.Optional[str]
            Device Serial Number

        ssid : typing.Optional[str]

        temp : typing.Optional[float]

        tls : typing.Optional[bool]
            Was TLS used?

        tower : typing.Optional[TowerLocation]

        transport : typing.Optional[str]
            Type of network transport

        tri : typing.Optional[TowerLocation]

        triangulate : typing.Optional[typing.Dict[str, typing.Any]]

        usage_actual : typing.Optional[bool]

        voltage : typing.Optional[float]

        when : typing.Optional[int]
            Last known capture time of a note routed through this session in Unix timestamp

        where : typing.Optional[str]
            Open Location Code from last GPS location

        where_country : typing.Optional[str]

        where_lat : typing.Optional[float]

        where_location : typing.Optional[str]

        where_lon : typing.Optional[float]

        where_timezone : typing.Optional[str]

        where_when : typing.Optional[int]
            Unix timestamp of last GPS location

        why_session_closed : typing.Optional[str]
            Reason for session closing

        why_session_opened : typing.Optional[str]
            Reason for session opening

        work : typing.Optional[int]
            Unix timestamp of the last time work was done for this session

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/ext-devices/{encode_path_param(device_uid)}/session/open",
            method="POST",
            json={
                "apn": apn,
                "bars": bars,
                "bearer": bearer,
                "bssid": bssid,
                "cell": cell,
                "continuous": continuous,
                "device": device,
                "events": events,
                "failed_connects": failed_connects,
                "fleets": fleets,
                "hp_cycles_data": hp_cycles_data,
                "hp_cycles_gps": hp_cycles_gps,
                "hp_cycles_total": hp_cycles_total,
                "hp_secs_data": hp_secs_data,
                "hp_secs_gps": hp_secs_gps,
                "hp_secs_total": hp_secs_total,
                "iccid": iccid,
                "ip": ip,
                "moved": moved,
                "orientation": orientation,
                "penalty_secs": penalty_secs,
                "period": convert_and_respect_annotation_metadata(
                    object_=period, annotation=DeviceUsage, direction="write"
                ),
                "power_charging": power_charging,
                "power_mah": power_mah,
                "power_primary": power_primary,
                "power_usb": power_usb,
                "product": product,
                "rat": rat,
                "rsrp": rsrp,
                "rsrq": rsrq,
                "rssi": rssi,
                "scan": scan,
                "session": session,
                "session_began": session_began,
                "session_ended": session_ended,
                "sinr": sinr,
                "sn": sn,
                "ssid": ssid,
                "temp": temp,
                "tls": tls,
                "tower": convert_and_respect_annotation_metadata(
                    object_=tower, annotation=TowerLocation, direction="write"
                ),
                "transport": transport,
                "tri": convert_and_respect_annotation_metadata(
                    object_=tri, annotation=TowerLocation, direction="write"
                ),
                "triangulate": triangulate,
                "usage_actual": usage_actual,
                "voltage": voltage,
                "when": when,
                "where": where,
                "where_country": where_country,
                "where_lat": where_lat,
                "where_location": where_location,
                "where_lon": where_lon,
                "where_timezone": where_timezone,
                "where_when": where_when,
                "why_session_closed": why_session_closed,
                "why_session_opened": why_session_opened,
                "work": work,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawExternalDevicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_event_ext_device(
        self,
        product_uid: str,
        device_uid: str,
        *,
        app: typing.Optional[str] = OMIT,
        bars: typing.Optional[int] = OMIT,
        best_country: typing.Optional[str] = OMIT,
        best_id: typing.Optional[str] = OMIT,
        best_lat: typing.Optional[float] = OMIT,
        best_location: typing.Optional[str] = OMIT,
        best_location_type: typing.Optional[str] = OMIT,
        best_location_when: typing.Optional[int] = OMIT,
        best_lon: typing.Optional[float] = OMIT,
        best_timezone: typing.Optional[str] = OMIT,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        bssid: typing.Optional[str] = OMIT,
        device: typing.Optional[str] = OMIT,
        environment: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        event: typing.Optional[str] = OMIT,
        file: typing.Optional[str] = OMIT,
        moved: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        ordering_code: typing.Optional[str] = OMIT,
        orientation: typing.Optional[str] = OMIT,
        payload: typing.Optional[str] = OMIT,
        product: typing.Optional[str] = OMIT,
        rat: typing.Optional[str] = OMIT,
        received: typing.Optional[float] = OMIT,
        req: typing.Optional[str] = OMIT,
        rsrp: typing.Optional[int] = OMIT,
        rsrq: typing.Optional[int] = OMIT,
        rssi: typing.Optional[int] = OMIT,
        sensor: typing.Optional[str] = OMIT,
        session: typing.Optional[str] = OMIT,
        sinr: typing.Optional[int] = OMIT,
        sku: typing.Optional[str] = OMIT,
        sn: typing.Optional[str] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        temp: typing.Optional[float] = OMIT,
        tls: typing.Optional[bool] = OMIT,
        tower_country: typing.Optional[str] = OMIT,
        tower_id: typing.Optional[str] = OMIT,
        tower_lat: typing.Optional[float] = OMIT,
        tower_location: typing.Optional[str] = OMIT,
        tower_lon: typing.Optional[float] = OMIT,
        tower_timezone: typing.Optional[str] = OMIT,
        tower_when: typing.Optional[int] = OMIT,
        transport: typing.Optional[str] = OMIT,
        tri_country: typing.Optional[str] = OMIT,
        tri_lat: typing.Optional[float] = OMIT,
        tri_location: typing.Optional[str] = OMIT,
        tri_lon: typing.Optional[float] = OMIT,
        tri_points: typing.Optional[int] = OMIT,
        tri_timezone: typing.Optional[str] = OMIT,
        tri_when: typing.Optional[int] = OMIT,
        updates: typing.Optional[int] = OMIT,
        voltage: typing.Optional[float] = OMIT,
        when: typing.Optional[int] = OMIT,
        when_ms: typing.Optional[int] = OMIT,
        where_country: typing.Optional[str] = OMIT,
        where_lat: typing.Optional[float] = OMIT,
        where_location: typing.Optional[str] = OMIT,
        where_lon: typing.Optional[float] = OMIT,
        where_olc: typing.Optional[str] = OMIT,
        where_timezone: typing.Optional[str] = OMIT,
        where_when: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Creates an event using specified webhook

        Parameters
        ----------
        product_uid : str

        device_uid : str

        app : typing.Optional[str]
            App UID (globally unique)

        bars : typing.Optional[int]
            Bars. Only available on _session.qo events.

        best_country : typing.Optional[str]
            Country

        best_id : typing.Optional[str]
            The device serial number, or the DeviceUID if the serial number is not set

        best_lat : typing.Optional[float]
            Latitude

        best_location : typing.Optional[str]
            Location

        best_location_type : typing.Optional[str]
            One of "gps", "triangulated", or "tower"

        best_location_when : typing.Optional[int]
            Unix timestamp

        best_lon : typing.Optional[float]
            Longitude

        best_timezone : typing.Optional[str]
            Timezone

        body : typing.Optional[typing.Dict[str, typing.Any]]
            A JSON object containing event details

        bssid : typing.Optional[str]
            BSSID. Only available on _session.qo events.

        device : typing.Optional[str]
            Device UID (globally unique)

        environment : typing.Optional[typing.Dict[str, typing.Any]]
            Routed environment variables beginning with "$". Only available on _session.qo events.

        event : typing.Optional[str]
            Event UID (globally unique)

        file : typing.Optional[str]
            The notefile associated with this event

        moved : typing.Optional[int]
            The number of times the device was sensed to have moved between the last session and this session. Only available on _session.qo events.

        note : typing.Optional[str]
            The note ID in the notefile

        ordering_code : typing.Optional[str]
            Ordering code. Only available on _session.qo events.

        orientation : typing.Optional[str]
            The orientation of the device. Only available on _session.qo events.

        payload : typing.Optional[str]
            A base64-encoded binary payload

        product : typing.Optional[str]
            Product UID (globally unique)

        rat : typing.Optional[str]
            Rat. Only available on _session.qo events.

        received : typing.Optional[float]
            The unix timestamp when the event was received

        req : typing.Optional[str]
            The notecard request

        rsrp : typing.Optional[int]
            RSRP. Only available on _session.qo events.

        rsrq : typing.Optional[int]
            RSRQ. Only available on _session.qo events.

        rssi : typing.Optional[int]
            Received Signal Strength Indicator (RSSI) is an estimated measurement of how well a device can receive signals. Only available on _session.qo events.

        sensor : typing.Optional[str]
            Sensor UID, for events originating from a sensor attached to the device

        session : typing.Optional[str]
            Session UID (globally unique)

        sinr : typing.Optional[int]
            SINR. Only available on _session.qo events.

        sku : typing.Optional[str]
            SKU. Only available on _session.qo events.

        sn : typing.Optional[str]
            The device serial number

        ssid : typing.Optional[str]
            SSID. Only available on _session.qo events.

        temp : typing.Optional[float]
            Device temperature. Only available on _session.qo events.

        tls : typing.Optional[bool]
            Whether TLS was used on the connection between the device and notehub. Only available on _session.qo events.

        tower_country : typing.Optional[str]
            Country

        tower_id : typing.Optional[str]
            Tower ID

        tower_lat : typing.Optional[float]
            Latitude

        tower_location : typing.Optional[str]
            Location

        tower_lon : typing.Optional[float]
            Longitude

        tower_timezone : typing.Optional[str]
            Timezone

        tower_when : typing.Optional[int]
            Unix timestamp

        transport : typing.Optional[str]
            The transport used for this event, e.g., "cellular", "wifi", ", etc.

        tri_country : typing.Optional[str]
            Country

        tri_lat : typing.Optional[float]
            Latitude

        tri_location : typing.Optional[str]
            Location

        tri_lon : typing.Optional[float]
            Longitude

        tri_points : typing.Optional[int]
            Triangulation points

        tri_timezone : typing.Optional[str]
            Timezone

        tri_when : typing.Optional[int]
            Unix timestamp

        updates : typing.Optional[int]

        voltage : typing.Optional[float]
            Device voltage. Only available on _session.qo events.

        when : typing.Optional[int]
            When the event was captured on the device

        when_ms : typing.Optional[int]
            Millisecond-accurate Unix epoch timestamp for when the event was captured on the device

        where_country : typing.Optional[str]
            Country

        where_lat : typing.Optional[float]
            Latitude

        where_location : typing.Optional[str]
            Location

        where_lon : typing.Optional[float]
            Longitude

        where_olc : typing.Optional[str]
            Open Location Code

        where_timezone : typing.Optional[str]
            Timezone

        where_when : typing.Optional[int]
            Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/ext-devices/{encode_path_param(device_uid)}/event",
            method="POST",
            json={
                "app": app,
                "bars": bars,
                "best_country": best_country,
                "best_id": best_id,
                "best_lat": best_lat,
                "best_location": best_location,
                "best_location_type": best_location_type,
                "best_location_when": best_location_when,
                "best_lon": best_lon,
                "best_timezone": best_timezone,
                "body": body,
                "bssid": bssid,
                "device": device,
                "environment": environment,
                "event": event,
                "file": file,
                "moved": moved,
                "note": note,
                "ordering_code": ordering_code,
                "orientation": orientation,
                "payload": payload,
                "product": product,
                "rat": rat,
                "received": received,
                "req": req,
                "rsrp": rsrp,
                "rsrq": rsrq,
                "rssi": rssi,
                "sensor": sensor,
                "session": session,
                "sinr": sinr,
                "sku": sku,
                "sn": sn,
                "ssid": ssid,
                "temp": temp,
                "tls": tls,
                "tower_country": tower_country,
                "tower_id": tower_id,
                "tower_lat": tower_lat,
                "tower_location": tower_location,
                "tower_lon": tower_lon,
                "tower_timezone": tower_timezone,
                "tower_when": tower_when,
                "transport": transport,
                "tri_country": tri_country,
                "tri_lat": tri_lat,
                "tri_location": tri_location,
                "tri_lon": tri_lon,
                "tri_points": tri_points,
                "tri_timezone": tri_timezone,
                "tri_when": tri_when,
                "updates": updates,
                "voltage": voltage,
                "when": when,
                "when_ms": when_ms,
                "where_country": where_country,
                "where_lat": where_lat,
                "where_location": where_location,
                "where_lon": where_lon,
                "where_olc": where_olc,
                "where_timezone": where_timezone,
                "where_when": where_when,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ext_device_session_close(
        self,
        product_uid: str,
        device_uid: str,
        *,
        apn: typing.Optional[str] = OMIT,
        bars: typing.Optional[int] = OMIT,
        bearer: typing.Optional[str] = OMIT,
        bssid: typing.Optional[str] = OMIT,
        cell: typing.Optional[str] = OMIT,
        continuous: typing.Optional[bool] = OMIT,
        device: typing.Optional[str] = OMIT,
        events: typing.Optional[int] = OMIT,
        failed_connects: typing.Optional[int] = OMIT,
        fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        hp_cycles_data: typing.Optional[int] = OMIT,
        hp_cycles_gps: typing.Optional[int] = OMIT,
        hp_cycles_total: typing.Optional[int] = OMIT,
        hp_secs_data: typing.Optional[int] = OMIT,
        hp_secs_gps: typing.Optional[int] = OMIT,
        hp_secs_total: typing.Optional[int] = OMIT,
        iccid: typing.Optional[str] = OMIT,
        ip: typing.Optional[str] = OMIT,
        moved: typing.Optional[int] = OMIT,
        orientation: typing.Optional[str] = OMIT,
        penalty_secs: typing.Optional[int] = OMIT,
        period: typing.Optional[DeviceUsage] = OMIT,
        power_charging: typing.Optional[bool] = OMIT,
        power_mah: typing.Optional[float] = OMIT,
        power_primary: typing.Optional[bool] = OMIT,
        power_usb: typing.Optional[bool] = OMIT,
        product: typing.Optional[str] = OMIT,
        rat: typing.Optional[str] = OMIT,
        rsrp: typing.Optional[int] = OMIT,
        rsrq: typing.Optional[int] = OMIT,
        rssi: typing.Optional[int] = OMIT,
        scan: typing.Optional[str] = OMIT,
        session: typing.Optional[str] = OMIT,
        session_began: typing.Optional[int] = OMIT,
        session_ended: typing.Optional[int] = OMIT,
        sinr: typing.Optional[int] = OMIT,
        sn: typing.Optional[str] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        temp: typing.Optional[float] = OMIT,
        tls: typing.Optional[bool] = OMIT,
        tower: typing.Optional[TowerLocation] = OMIT,
        transport: typing.Optional[str] = OMIT,
        tri: typing.Optional[TowerLocation] = OMIT,
        triangulate: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        usage_actual: typing.Optional[bool] = OMIT,
        voltage: typing.Optional[float] = OMIT,
        when: typing.Optional[int] = OMIT,
        where: typing.Optional[str] = OMIT,
        where_country: typing.Optional[str] = OMIT,
        where_lat: typing.Optional[float] = OMIT,
        where_location: typing.Optional[str] = OMIT,
        where_lon: typing.Optional[float] = OMIT,
        where_timezone: typing.Optional[str] = OMIT,
        where_when: typing.Optional[int] = OMIT,
        why_session_closed: typing.Optional[str] = OMIT,
        why_session_opened: typing.Optional[str] = OMIT,
        work: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Closes the session for the specified device if open

        Parameters
        ----------
        product_uid : str

        device_uid : str

        apn : typing.Optional[str]

        bars : typing.Optional[int]

        bearer : typing.Optional[str]

        bssid : typing.Optional[str]

        cell : typing.Optional[str]
            Cell ID where the session originated and quality ("mcc,mnc,lac,cellid")

        continuous : typing.Optional[bool]
            Was this a continuous connection?

        device : typing.Optional[str]
            Device UID

        events : typing.Optional[int]
            Number of events routed

        failed_connects : typing.Optional[int]
            Number of failed connection attempts in the prior session

        fleets : typing.Optional[typing.Sequence[str]]
            Array of Fleet UIDs

        hp_cycles_data : typing.Optional[int]

        hp_cycles_gps : typing.Optional[int]

        hp_cycles_total : typing.Optional[int]

        hp_secs_data : typing.Optional[int]

        hp_secs_gps : typing.Optional[int]

        hp_secs_total : typing.Optional[int]
            Total number of seconds in high power mode

        iccid : typing.Optional[str]

        ip : typing.Optional[str]

        moved : typing.Optional[int]

        orientation : typing.Optional[str]

        penalty_secs : typing.Optional[int]
            Number of seconds in penalty in the prior session

        period : typing.Optional[DeviceUsage]

        power_charging : typing.Optional[bool]

        power_mah : typing.Optional[float]

        power_primary : typing.Optional[bool]

        power_usb : typing.Optional[bool]

        product : typing.Optional[str]
            Product UID

        rat : typing.Optional[str]

        rsrp : typing.Optional[int]

        rsrq : typing.Optional[int]

        rssi : typing.Optional[int]

        scan : typing.Optional[str]

        session : typing.Optional[str]
            Session UID

        session_began : typing.Optional[int]
            UNIX timestamp of session start

        session_ended : typing.Optional[int]
            UNIX timestamp of session end

        sinr : typing.Optional[int]

        sn : typing.Optional[str]
            Device Serial Number

        ssid : typing.Optional[str]

        temp : typing.Optional[float]

        tls : typing.Optional[bool]
            Was TLS used?

        tower : typing.Optional[TowerLocation]

        transport : typing.Optional[str]
            Type of network transport

        tri : typing.Optional[TowerLocation]

        triangulate : typing.Optional[typing.Dict[str, typing.Any]]

        usage_actual : typing.Optional[bool]

        voltage : typing.Optional[float]

        when : typing.Optional[int]
            Last known capture time of a note routed through this session in Unix timestamp

        where : typing.Optional[str]
            Open Location Code from last GPS location

        where_country : typing.Optional[str]

        where_lat : typing.Optional[float]

        where_location : typing.Optional[str]

        where_lon : typing.Optional[float]

        where_timezone : typing.Optional[str]

        where_when : typing.Optional[int]
            Unix timestamp of last GPS location

        why_session_closed : typing.Optional[str]
            Reason for session closing

        why_session_opened : typing.Optional[str]
            Reason for session opening

        work : typing.Optional[int]
            Unix timestamp of the last time work was done for this session

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/ext-devices/{encode_path_param(device_uid)}/session/close",
            method="POST",
            json={
                "apn": apn,
                "bars": bars,
                "bearer": bearer,
                "bssid": bssid,
                "cell": cell,
                "continuous": continuous,
                "device": device,
                "events": events,
                "failed_connects": failed_connects,
                "fleets": fleets,
                "hp_cycles_data": hp_cycles_data,
                "hp_cycles_gps": hp_cycles_gps,
                "hp_cycles_total": hp_cycles_total,
                "hp_secs_data": hp_secs_data,
                "hp_secs_gps": hp_secs_gps,
                "hp_secs_total": hp_secs_total,
                "iccid": iccid,
                "ip": ip,
                "moved": moved,
                "orientation": orientation,
                "penalty_secs": penalty_secs,
                "period": convert_and_respect_annotation_metadata(
                    object_=period, annotation=DeviceUsage, direction="write"
                ),
                "power_charging": power_charging,
                "power_mah": power_mah,
                "power_primary": power_primary,
                "power_usb": power_usb,
                "product": product,
                "rat": rat,
                "rsrp": rsrp,
                "rsrq": rsrq,
                "rssi": rssi,
                "scan": scan,
                "session": session,
                "session_began": session_began,
                "session_ended": session_ended,
                "sinr": sinr,
                "sn": sn,
                "ssid": ssid,
                "temp": temp,
                "tls": tls,
                "tower": convert_and_respect_annotation_metadata(
                    object_=tower, annotation=TowerLocation, direction="write"
                ),
                "transport": transport,
                "tri": convert_and_respect_annotation_metadata(
                    object_=tri, annotation=TowerLocation, direction="write"
                ),
                "triangulate": triangulate,
                "usage_actual": usage_actual,
                "voltage": voltage,
                "when": when,
                "where": where,
                "where_country": where_country,
                "where_lat": where_lat,
                "where_location": where_location,
                "where_lon": where_lon,
                "where_timezone": where_timezone,
                "where_when": where_when,
                "why_session_closed": why_session_closed,
                "why_session_opened": why_session_opened,
                "work": work,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ext_device_session_open(
        self,
        product_uid: str,
        device_uid: str,
        *,
        apn: typing.Optional[str] = OMIT,
        bars: typing.Optional[int] = OMIT,
        bearer: typing.Optional[str] = OMIT,
        bssid: typing.Optional[str] = OMIT,
        cell: typing.Optional[str] = OMIT,
        continuous: typing.Optional[bool] = OMIT,
        device: typing.Optional[str] = OMIT,
        events: typing.Optional[int] = OMIT,
        failed_connects: typing.Optional[int] = OMIT,
        fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        hp_cycles_data: typing.Optional[int] = OMIT,
        hp_cycles_gps: typing.Optional[int] = OMIT,
        hp_cycles_total: typing.Optional[int] = OMIT,
        hp_secs_data: typing.Optional[int] = OMIT,
        hp_secs_gps: typing.Optional[int] = OMIT,
        hp_secs_total: typing.Optional[int] = OMIT,
        iccid: typing.Optional[str] = OMIT,
        ip: typing.Optional[str] = OMIT,
        moved: typing.Optional[int] = OMIT,
        orientation: typing.Optional[str] = OMIT,
        penalty_secs: typing.Optional[int] = OMIT,
        period: typing.Optional[DeviceUsage] = OMIT,
        power_charging: typing.Optional[bool] = OMIT,
        power_mah: typing.Optional[float] = OMIT,
        power_primary: typing.Optional[bool] = OMIT,
        power_usb: typing.Optional[bool] = OMIT,
        product: typing.Optional[str] = OMIT,
        rat: typing.Optional[str] = OMIT,
        rsrp: typing.Optional[int] = OMIT,
        rsrq: typing.Optional[int] = OMIT,
        rssi: typing.Optional[int] = OMIT,
        scan: typing.Optional[str] = OMIT,
        session: typing.Optional[str] = OMIT,
        session_began: typing.Optional[int] = OMIT,
        session_ended: typing.Optional[int] = OMIT,
        sinr: typing.Optional[int] = OMIT,
        sn: typing.Optional[str] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        temp: typing.Optional[float] = OMIT,
        tls: typing.Optional[bool] = OMIT,
        tower: typing.Optional[TowerLocation] = OMIT,
        transport: typing.Optional[str] = OMIT,
        tri: typing.Optional[TowerLocation] = OMIT,
        triangulate: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        usage_actual: typing.Optional[bool] = OMIT,
        voltage: typing.Optional[float] = OMIT,
        when: typing.Optional[int] = OMIT,
        where: typing.Optional[str] = OMIT,
        where_country: typing.Optional[str] = OMIT,
        where_lat: typing.Optional[float] = OMIT,
        where_location: typing.Optional[str] = OMIT,
        where_lon: typing.Optional[float] = OMIT,
        where_timezone: typing.Optional[str] = OMIT,
        where_when: typing.Optional[int] = OMIT,
        why_session_closed: typing.Optional[str] = OMIT,
        why_session_opened: typing.Optional[str] = OMIT,
        work: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Create a Session for the specified device.  | If a session is currently open it will be closed and a new one opened.

        Parameters
        ----------
        product_uid : str

        device_uid : str

        apn : typing.Optional[str]

        bars : typing.Optional[int]

        bearer : typing.Optional[str]

        bssid : typing.Optional[str]

        cell : typing.Optional[str]
            Cell ID where the session originated and quality ("mcc,mnc,lac,cellid")

        continuous : typing.Optional[bool]
            Was this a continuous connection?

        device : typing.Optional[str]
            Device UID

        events : typing.Optional[int]
            Number of events routed

        failed_connects : typing.Optional[int]
            Number of failed connection attempts in the prior session

        fleets : typing.Optional[typing.Sequence[str]]
            Array of Fleet UIDs

        hp_cycles_data : typing.Optional[int]

        hp_cycles_gps : typing.Optional[int]

        hp_cycles_total : typing.Optional[int]

        hp_secs_data : typing.Optional[int]

        hp_secs_gps : typing.Optional[int]

        hp_secs_total : typing.Optional[int]
            Total number of seconds in high power mode

        iccid : typing.Optional[str]

        ip : typing.Optional[str]

        moved : typing.Optional[int]

        orientation : typing.Optional[str]

        penalty_secs : typing.Optional[int]
            Number of seconds in penalty in the prior session

        period : typing.Optional[DeviceUsage]

        power_charging : typing.Optional[bool]

        power_mah : typing.Optional[float]

        power_primary : typing.Optional[bool]

        power_usb : typing.Optional[bool]

        product : typing.Optional[str]
            Product UID

        rat : typing.Optional[str]

        rsrp : typing.Optional[int]

        rsrq : typing.Optional[int]

        rssi : typing.Optional[int]

        scan : typing.Optional[str]

        session : typing.Optional[str]
            Session UID

        session_began : typing.Optional[int]
            UNIX timestamp of session start

        session_ended : typing.Optional[int]
            UNIX timestamp of session end

        sinr : typing.Optional[int]

        sn : typing.Optional[str]
            Device Serial Number

        ssid : typing.Optional[str]

        temp : typing.Optional[float]

        tls : typing.Optional[bool]
            Was TLS used?

        tower : typing.Optional[TowerLocation]

        transport : typing.Optional[str]
            Type of network transport

        tri : typing.Optional[TowerLocation]

        triangulate : typing.Optional[typing.Dict[str, typing.Any]]

        usage_actual : typing.Optional[bool]

        voltage : typing.Optional[float]

        when : typing.Optional[int]
            Last known capture time of a note routed through this session in Unix timestamp

        where : typing.Optional[str]
            Open Location Code from last GPS location

        where_country : typing.Optional[str]

        where_lat : typing.Optional[float]

        where_location : typing.Optional[str]

        where_lon : typing.Optional[float]

        where_timezone : typing.Optional[str]

        where_when : typing.Optional[int]
            Unix timestamp of last GPS location

        why_session_closed : typing.Optional[str]
            Reason for session closing

        why_session_opened : typing.Optional[str]
            Reason for session opening

        work : typing.Optional[int]
            Unix timestamp of the last time work was done for this session

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/ext-devices/{encode_path_param(device_uid)}/session/open",
            method="POST",
            json={
                "apn": apn,
                "bars": bars,
                "bearer": bearer,
                "bssid": bssid,
                "cell": cell,
                "continuous": continuous,
                "device": device,
                "events": events,
                "failed_connects": failed_connects,
                "fleets": fleets,
                "hp_cycles_data": hp_cycles_data,
                "hp_cycles_gps": hp_cycles_gps,
                "hp_cycles_total": hp_cycles_total,
                "hp_secs_data": hp_secs_data,
                "hp_secs_gps": hp_secs_gps,
                "hp_secs_total": hp_secs_total,
                "iccid": iccid,
                "ip": ip,
                "moved": moved,
                "orientation": orientation,
                "penalty_secs": penalty_secs,
                "period": convert_and_respect_annotation_metadata(
                    object_=period, annotation=DeviceUsage, direction="write"
                ),
                "power_charging": power_charging,
                "power_mah": power_mah,
                "power_primary": power_primary,
                "power_usb": power_usb,
                "product": product,
                "rat": rat,
                "rsrp": rsrp,
                "rsrq": rsrq,
                "rssi": rssi,
                "scan": scan,
                "session": session,
                "session_began": session_began,
                "session_ended": session_ended,
                "sinr": sinr,
                "sn": sn,
                "ssid": ssid,
                "temp": temp,
                "tls": tls,
                "tower": convert_and_respect_annotation_metadata(
                    object_=tower, annotation=TowerLocation, direction="write"
                ),
                "transport": transport,
                "tri": convert_and_respect_annotation_metadata(
                    object_=tri, annotation=TowerLocation, direction="write"
                ),
                "triangulate": triangulate,
                "usage_actual": usage_actual,
                "voltage": voltage,
                "when": when,
                "where": where,
                "where_country": where_country,
                "where_lat": where_lat,
                "where_location": where_location,
                "where_lon": where_lon,
                "where_timezone": where_timezone,
                "where_when": where_when,
                "why_session_closed": why_session_closed,
                "why_session_opened": why_session_opened,
                "work": work,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
