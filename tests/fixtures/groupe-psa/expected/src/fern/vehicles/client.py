

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alarm_details import AlarmDetails
from ..types.alarm_type_enum_item import AlarmTypeEnumItem
from ..types.alarms import Alarms
from ..types.alert import Alert
from ..types.alerts import Alerts
from ..types.collision import Collision
from ..types.collisions import Collisions
from ..types.data_profile import DataProfile
from ..types.index_range import IndexRange
from ..types.maintenance import Maintenance
from ..types.position import Position
from ..types.status import Status
from ..types.stolen import Stolen
from ..types.stolen_collection import StolenCollection
from ..types.telemetries import Telemetries
from ..types.telemetry_enum_item import TelemetryEnumItem
from ..types.telemetry_extension_type_item import TelemetryExtensionTypeItem
from ..types.vehicle import Vehicle
from ..types.vehicle_extension_type_item import VehicleExtensionTypeItem
from ..types.vehicles import Vehicles
from ..types.vehicles_extension_type_item import VehiclesExtensionTypeItem
from ..types.way_points import WayPoints
from .raw_client import AsyncRawVehiclesClient, RawVehiclesClient


class VehiclesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVehiclesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVehiclesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVehiclesClient
        """
        return self._raw_client

    def get_vehicles_by_device(
        self,
        fid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehiclesExtensionTypeItem, typing.Sequence[VehiclesExtensionTypeItem]]
        ] = None,
        vin_prefix: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vehicles:
        """
        Returns the Vehicles associated with the Fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehiclesExtensionTypeItem, typing.Sequence[VehiclesExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 2)```.

        vin_prefix : typing.Optional[str]
            Allows filtering on VINs that start with the same prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vehicles
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicles_by_device(
            fid="fid",
        )
        """
        _response = self._raw_client.get_vehicles_by_device(
            fid,
            page_size=page_size,
            page_token=page_token,
            locale=locale,
            extension=extension,
            vin_prefix=vin_prefix,
            request_options=request_options,
        )
        return _response.data

    def get_vehicle_byid(
        self,
        fid: str,
        vid: str,
        *,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vehicle:
        """
        Returns detailed information about a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vehicle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_byid(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_vehicle_byid(
            fid, vid, locale=locale, extension=extension, request_options=request_options
        )
        return _response.data

    def get_car_last_position(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Position:
        """
        Returns the latest GPS Position of the Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Position
            Position response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_car_last_position(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_car_last_position(fid, vid, profile=profile, request_options=request_options)
        return _response.data

    def get_vehicle_collision(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collisions:
        """
        Returns the list of Collisions that occurred for a given vehicle (id) during the timestamp ranges and bounded by an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collisions
            A list of Collision

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_collision(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_vehicle_collision(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_vehicle_collision_by_id(
        self,
        fid: str,
        vid: str,
        cid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collision:
        """
        Returns the Collision that matches the vehicle id and the Collision cid.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cid : str
            Results will only contain the Collision related to this Collision ID.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collision
            Collision response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_collision_by_id(
            fid="fid",
            vid="vid",
            cid="cid",
        )
        """
        _response = self._raw_client.get_vehicle_collision_by_id(
            fid, vid, cid, profile=profile, request_options=request_options
        )
        return _response.data

    def get_vehicle_maintenance(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Maintenance:
        """
        Returns the latest Maintenance information for a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Maintenance
            Maintenant response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_maintenance(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_vehicle_maintenance(fid, vid, profile=profile, request_options=request_options)
        return _response.data

    def get_fleet_vehicle_status(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Status:
        """
        Returns the latest vehicle status.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Status
            Status response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_fleet_vehicle_status(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_fleet_vehicle_status(
            fid, vid, profile=profile, request_options=request_options
        )
        return _response.data

    def get_vehicle_alerts(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alerts:
        """
        Returns the latest alert messages for a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alerts
            A list of alert

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_alerts(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_vehicle_alerts(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_vehicle_alerts_by_id(
        self,
        fid: str,
        vid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alert:
        """
        Returns information about a specific alert messages for a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        aid : str
            id of the alert.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alert
            Alert response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_fleet_vehicle_alerts_by_id(
            fid="fid",
            vid="vid",
            aid="aid",
        )
        """
        _response = self._raw_client.get_fleet_vehicle_alerts_by_id(
            fid, vid, aid, profile=profile, request_options=request_options
        )
        return _response.data

    def get_telemetry(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        type: typing.Optional[typing.Union[TelemetryEnumItem, typing.Sequence[TelemetryEnumItem]]] = None,
        extension: typing.Optional[
            typing.Union[TelemetryExtensionTypeItem, typing.Sequence[TelemetryExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Telemetries:
        """
        Returns the latest Telemetry messages that occurred during a selective timestamp-ranges and bounded by an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page for high frequency data upload. When not set, at most 60 results will be returned.  The range for this parameter is [1...2000]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        type : typing.Optional[typing.Union[TelemetryEnumItem, typing.Sequence[TelemetryEnumItem]]]
            Results will only contain Telemetry messages of this kind. You can add more than one message type. By default, if no type is selected then all telemetries will be taken ```(the number of elements in this array must be between 1 and 17)```.
             * _Disclaimer_:   ```vehicle.lighting``` is deprecated

        extension : typing.Optional[typing.Union[TelemetryExtensionTypeItem, typing.Sequence[TelemetryExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 2)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Telemetries
            Telemetry response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_telemetry(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_telemetry(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            type=type,
            extension=extension,
            request_options=request_options,
        )
        return _response.data

    def get_vehicle_alarms(
        self,
        fid: str,
        vid: str,
        *,
        type: typing.Optional[typing.Union[AlarmTypeEnumItem, typing.Sequence[AlarmTypeEnumItem]]] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alarms:
        """
        Returns a (filtered) list of alarm for a Vehicle.
        *Note:* Timestamp filtering concerns the creation date for status or trigger.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        type : typing.Optional[typing.Union[AlarmTypeEnumItem, typing.Sequence[AlarmTypeEnumItem]]]
            Results will only contain Alarm messages of this type.  If no filtering type is selected then all alarms will be taken .

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alarms
            A list of alert

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_alarms(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_vehicle_alarms(
            fid,
            vid,
            type=type,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_vehicle_alarms_by_id(
        self, fid: str, vid: str, aid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlarmDetails:
        """
        Returns information about a specific alarm for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        aid : str
            id of the alarm.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlarmDetails
            Alarm response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_alarms_by_id(
            fid="fid",
            vid="vid",
            aid="aid",
        )
        """
        _response = self._raw_client.get_vehicle_alarms_by_id(fid, vid, aid, request_options=request_options)
        return _response.data

    def get_vehicle_stolen_history(
        self,
        fid: str,
        vid: str,
        *,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StolenCollection:
        """
        Returns  list of stolen state for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StolenCollection
            A list of stolen context.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_stolen_history(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_vehicle_stolen_history(
            fid,
            vid,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_vehicle_stolen_by_id(
        self, fid: str, vid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Stolen:
        """
        Returns information about a specific stolen context for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        sid : str
            id of the stolen state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stolen
            Stolen response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_stolen_by_id(
            fid="fid",
            vid="vid",
            sid="sid",
        )
        """
        _response = self._raw_client.get_vehicle_stolen_by_id(fid, vid, sid, request_options=request_options)
        return _response.data

    def get_vehicle_stolen_id_position(
        self, fid: str, vid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WayPoints:
        """
        Returns position information about a specific stolen context for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        sid : str
            id of the stolen state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WayPoints
            Stolen position response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.vehicles.get_vehicle_stolen_id_position(
            fid="fid",
            vid="vid",
            sid="sid",
        )
        """
        _response = self._raw_client.get_vehicle_stolen_id_position(fid, vid, sid, request_options=request_options)
        return _response.data


class AsyncVehiclesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVehiclesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVehiclesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVehiclesClient
        """
        return self._raw_client

    async def get_vehicles_by_device(
        self,
        fid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehiclesExtensionTypeItem, typing.Sequence[VehiclesExtensionTypeItem]]
        ] = None,
        vin_prefix: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vehicles:
        """
        Returns the Vehicles associated with the Fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehiclesExtensionTypeItem, typing.Sequence[VehiclesExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 2)```.

        vin_prefix : typing.Optional[str]
            Allows filtering on VINs that start with the same prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vehicles
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicles_by_device(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicles_by_device(
            fid,
            page_size=page_size,
            page_token=page_token,
            locale=locale,
            extension=extension,
            vin_prefix=vin_prefix,
            request_options=request_options,
        )
        return _response.data

    async def get_vehicle_byid(
        self,
        fid: str,
        vid: str,
        *,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vehicle:
        """
        Returns detailed information about a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vehicle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_byid(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_byid(
            fid, vid, locale=locale, extension=extension, request_options=request_options
        )
        return _response.data

    async def get_car_last_position(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Position:
        """
        Returns the latest GPS Position of the Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Position
            Position response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_car_last_position(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_car_last_position(
            fid, vid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_vehicle_collision(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collisions:
        """
        Returns the list of Collisions that occurred for a given vehicle (id) during the timestamp ranges and bounded by an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collisions
            A list of Collision

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_collision(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_collision(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_vehicle_collision_by_id(
        self,
        fid: str,
        vid: str,
        cid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collision:
        """
        Returns the Collision that matches the vehicle id and the Collision cid.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        cid : str
            Results will only contain the Collision related to this Collision ID.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collision
            Collision response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_collision_by_id(
                fid="fid",
                vid="vid",
                cid="cid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_collision_by_id(
            fid, vid, cid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_vehicle_maintenance(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Maintenance:
        """
        Returns the latest Maintenance information for a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Maintenance
            Maintenant response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_maintenance(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_maintenance(
            fid, vid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_fleet_vehicle_status(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Status:
        """
        Returns the latest vehicle status.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Status
            Status response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_fleet_vehicle_status(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_vehicle_status(
            fid, vid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_vehicle_alerts(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alerts:
        """
        Returns the latest alert messages for a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alerts
            A list of alert

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_alerts(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_alerts(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_vehicle_alerts_by_id(
        self,
        fid: str,
        vid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alert:
        """
        Returns information about a specific alert messages for a Vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        aid : str
            id of the alert.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alert
            Alert response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_fleet_vehicle_alerts_by_id(
                fid="fid",
                vid="vid",
                aid="aid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_vehicle_alerts_by_id(
            fid, vid, aid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_telemetry(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        type: typing.Optional[typing.Union[TelemetryEnumItem, typing.Sequence[TelemetryEnumItem]]] = None,
        extension: typing.Optional[
            typing.Union[TelemetryExtensionTypeItem, typing.Sequence[TelemetryExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Telemetries:
        """
        Returns the latest Telemetry messages that occurred during a selective timestamp-ranges and bounded by an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page for high frequency data upload. When not set, at most 60 results will be returned.  The range for this parameter is [1...2000]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        type : typing.Optional[typing.Union[TelemetryEnumItem, typing.Sequence[TelemetryEnumItem]]]
            Results will only contain Telemetry messages of this kind. You can add more than one message type. By default, if no type is selected then all telemetries will be taken ```(the number of elements in this array must be between 1 and 17)```.
             * _Disclaimer_:   ```vehicle.lighting``` is deprecated

        extension : typing.Optional[typing.Union[TelemetryExtensionTypeItem, typing.Sequence[TelemetryExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 2)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Telemetries
            Telemetry response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_telemetry(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_telemetry(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            type=type,
            extension=extension,
            request_options=request_options,
        )
        return _response.data

    async def get_vehicle_alarms(
        self,
        fid: str,
        vid: str,
        *,
        type: typing.Optional[typing.Union[AlarmTypeEnumItem, typing.Sequence[AlarmTypeEnumItem]]] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alarms:
        """
        Returns a (filtered) list of alarm for a Vehicle.
        *Note:* Timestamp filtering concerns the creation date for status or trigger.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        type : typing.Optional[typing.Union[AlarmTypeEnumItem, typing.Sequence[AlarmTypeEnumItem]]]
            Results will only contain Alarm messages of this type.  If no filtering type is selected then all alarms will be taken .

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alarms
            A list of alert

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_alarms(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_alarms(
            fid,
            vid,
            type=type,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_vehicle_alarms_by_id(
        self, fid: str, vid: str, aid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlarmDetails:
        """
        Returns information about a specific alarm for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        aid : str
            id of the alarm.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlarmDetails
            Alarm response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_alarms_by_id(
                fid="fid",
                vid="vid",
                aid="aid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_alarms_by_id(fid, vid, aid, request_options=request_options)
        return _response.data

    async def get_vehicle_stolen_history(
        self,
        fid: str,
        vid: str,
        *,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StolenCollection:
        """
        Returns  list of stolen state for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        timestamps : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of  **"timestamp"** ranges. Results will contain results whose
            timestamps are included in those date-time ranges (see **timestamp**
            data  model).**"timestamp"** items should be expressed as in
            '[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array
            expresses a time range (with the pattern ```\\w?/\\w?``` or ```R\\d?/w/w(/w)?```)
            which is the period between two or more times. The range can be expressed by tw
            o times Points (start and end *Timestamp*s), by a start
            *Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
            is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
            - 'T1/T2' interval time from low limit T1 to hight T2
            - 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
            - 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
            - '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
            - Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
            - R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
            - T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
              - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
              - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
              - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
              - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StolenCollection
            A list of stolen context.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_stolen_history(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_stolen_history(
            fid,
            vid,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_vehicle_stolen_by_id(
        self, fid: str, vid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Stolen:
        """
        Returns information about a specific stolen context for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        sid : str
            id of the stolen state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stolen
            Stolen response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_stolen_by_id(
                fid="fid",
                vid="vid",
                sid="sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_stolen_by_id(fid, vid, sid, request_options=request_options)
        return _response.data

    async def get_vehicle_stolen_id_position(
        self, fid: str, vid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WayPoints:
        """
        Returns position information about a specific stolen context for a vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        sid : str
            id of the stolen state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WayPoints
            Stolen position response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.vehicles.get_vehicle_stolen_id_position(
                fid="fid",
                vid="vid",
                sid="sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicle_stolen_id_position(
            fid, vid, sid, request_options=request_options
        )
        return _response.data
