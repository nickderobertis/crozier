

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alert import Alert
from ..types.alerts import Alerts
from ..types.collisions import Collisions
from ..types.data_profile import DataProfile
from ..types.index_range import IndexRange
from ..types.range import Range
from ..types.telemetries import Telemetries
from ..types.telemetry_enum_item import TelemetryEnumItem
from ..types.telemetry_extension_type_item import TelemetryExtensionTypeItem
from ..types.trip import Trip
from ..types.trip_state_enum import TripStateEnum
from ..types.trips import Trips
from ..types.way_points import WayPoints
from .raw_client import AsyncRawTripsClient, RawTripsClient


class TripsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTripsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTripsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTripsClient
        """
        return self._raw_client

    def get_trips_by_vehicle(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        distance: typing.Optional[Range] = None,
        duration: typing.Optional[Range] = None,
        states: typing.Optional[typing.Union[TripStateEnum, typing.Sequence[TripStateEnum]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Trips:
        """
        This method returns a list of all Trips that a given Vehicle has taken. This will NOT include Trips that have not yet been completed.

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

        distance : typing.Optional[Range]
            Trip distance  validity interval. It allows to  define the min or max duration of a trip.
            **Unit = Km** and format : float (only one digit after the decimal point is aceepted for the interval bounds).

            *Example:*

                      * 1-150: Trip with distance between 1 Km and 150 km .

                      * 0.1-: Trip with distance  greater than 100 m.

              default: 0-

        duration : typing.Optional[Range]
            Trip duration validity interval. It allows to  define the min or max duration of a trip. **Unit = sec**

            *Example:*

                      * 10-3600: Trip with duration between 10 sec and 1 hour.

                      * 20-: Trip with duration greater than 20 sec.

              default: 0-

        states : typing.Optional[typing.Union[TripStateEnum, typing.Sequence[TripStateEnum]]]
            Allow to filter for Trips with defined states. Those states can be compound of : _Nominal,Unstarted, DataLacking, Unfinished_.

            Default: All states are allowed.

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
        Trips
            A list of Trip

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.trips.get_trips_by_vehicle(
            fid="fid",
            vid="vid",
        )
        """
        _response = self._raw_client.get_trips_by_vehicle(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            distance=distance,
            duration=duration,
            states=states,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_trip_by_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Trip:
        """
        This method returns the Trip that matches the Trip id (tid) a given Vehicle (id) has taken.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Trip
            Trip response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.trips.get_fleet_trip_by_vehicle(
            fid="fid",
            vid="vid",
            tid="tid",
        )
        """
        _response = self._raw_client.get_fleet_trip_by_vehicle(
            fid, vid, tid, profile=profile, request_options=request_options
        )
        return _response.data

    def get_trip_collisions_by_trip_and_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        page_token: typing.Optional[str] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collisions:
        """
        Returns the list of Collisions of a vehicle that occurred during a trip and bounded (optional) by a timestamp ranges and an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

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
        client.trips.get_trip_collisions_by_trip_and_vehicle(
            fid="fid",
            vid="vid",
            tid="tid",
        )
        """
        _response = self._raw_client.get_trip_collisions_by_trip_and_vehicle(
            fid,
            vid,
            tid,
            page_token=page_token,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_trip_alert_by_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alerts:
        """
        Returns the alert message list for a given vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

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

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
        client.trips.get_fleet_trip_alert_by_vehicle(
            fid="fid",
            vid="vid",
            tid="tid",
        )
        """
        _response = self._raw_client.get_fleet_trip_alert_by_vehicle(
            fid,
            vid,
            tid,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            profile=profile,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_trip_alert_by_vehicle_by_id(
        self,
        fid: str,
        vid: str,
        tid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alert:
        """
        Returns the alert message list for a given vehicle that occure during a trip.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

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
        client.trips.get_fleet_trip_alert_by_vehicle_by_id(
            fid="fid",
            vid="vid",
            tid="tid",
            aid="aid",
        )
        """
        _response = self._raw_client.get_fleet_trip_alert_by_vehicle_by_id(
            fid, vid, tid, aid, profile=profile, request_options=request_options
        )
        return _response.data

    def get_path_for_trip(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tolerance: typing.Optional[float] = None,
        profile: typing.Optional[DataProfile] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WayPoints:
        """
        Gives the Vehicle's wayPoints for a specified Trip.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

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

        tolerance : typing.Optional[float]
            Tolerance factor is expressed in length km unit and is used to simplify path by reducing the total number of points by is using Douglas-Peucker algorithm to find a similar curve with fewer points (find more info here: [Ramer_Douglas_Peucker_algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm#Algorithm) ).

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page for high frequency data upload. When not set, at most 60 results will be returned.  The range for this parameter is [1...2000]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WayPoints
            Path response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.trips.get_path_for_trip(
            fid="fid",
            vid="vid",
            tid="tid",
        )
        """
        _response = self._raw_client.get_path_for_trip(
            fid,
            vid,
            tid,
            index_range=index_range,
            timestamps=timestamps,
            tolerance=tolerance,
            profile=profile,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_telemetry_for_trip_by_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
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
        Returns the set of Telemetry values that occurred for a given vehicle (id) and a speific Trip (tid) during the timestamp ranges and bounded by an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

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
        client.trips.get_telemetry_for_trip_by_vehicle(
            fid="fid",
            vid="vid",
            tid="tid",
        )
        """
        _response = self._raw_client.get_telemetry_for_trip_by_vehicle(
            fid,
            vid,
            tid,
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


class AsyncTripsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTripsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTripsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTripsClient
        """
        return self._raw_client

    async def get_trips_by_vehicle(
        self,
        fid: str,
        vid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        distance: typing.Optional[Range] = None,
        duration: typing.Optional[Range] = None,
        states: typing.Optional[typing.Union[TripStateEnum, typing.Sequence[TripStateEnum]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Trips:
        """
        This method returns a list of all Trips that a given Vehicle has taken. This will NOT include Trips that have not yet been completed.

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

        distance : typing.Optional[Range]
            Trip distance  validity interval. It allows to  define the min or max duration of a trip.
            **Unit = Km** and format : float (only one digit after the decimal point is aceepted for the interval bounds).

            *Example:*

                      * 1-150: Trip with distance between 1 Km and 150 km .

                      * 0.1-: Trip with distance  greater than 100 m.

              default: 0-

        duration : typing.Optional[Range]
            Trip duration validity interval. It allows to  define the min or max duration of a trip. **Unit = sec**

            *Example:*

                      * 10-3600: Trip with duration between 10 sec and 1 hour.

                      * 20-: Trip with duration greater than 20 sec.

              default: 0-

        states : typing.Optional[typing.Union[TripStateEnum, typing.Sequence[TripStateEnum]]]
            Allow to filter for Trips with defined states. Those states can be compound of : _Nominal,Unstarted, DataLacking, Unfinished_.

            Default: All states are allowed.

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
        Trips
            A list of Trip

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.trips.get_trips_by_vehicle(
                fid="fid",
                vid="vid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_trips_by_vehicle(
            fid,
            vid,
            profile=profile,
            timestamps=timestamps,
            distance=distance,
            duration=duration,
            states=states,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_trip_by_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Trip:
        """
        This method returns the Trip that matches the Trip id (tid) a given Vehicle (id) has taken.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Trip
            Trip response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.trips.get_fleet_trip_by_vehicle(
                fid="fid",
                vid="vid",
                tid="tid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_trip_by_vehicle(
            fid, vid, tid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_trip_collisions_by_trip_and_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        page_token: typing.Optional[str] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collisions:
        """
        Returns the list of Collisions of a vehicle that occurred during a trip and bounded (optional) by a timestamp ranges and an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

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
            await client.trips.get_trip_collisions_by_trip_and_vehicle(
                fid="fid",
                vid="vid",
                tid="tid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_trip_collisions_by_trip_and_vehicle(
            fid,
            vid,
            tid,
            page_token=page_token,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_trip_alert_by_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alerts:
        """
        Returns the alert message list for a given vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

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

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
            await client.trips.get_fleet_trip_alert_by_vehicle(
                fid="fid",
                vid="vid",
                tid="tid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_trip_alert_by_vehicle(
            fid,
            vid,
            tid,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            profile=profile,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_trip_alert_by_vehicle_by_id(
        self,
        fid: str,
        vid: str,
        tid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alert:
        """
        Returns the alert message list for a given vehicle that occure during a trip.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

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
            await client.trips.get_fleet_trip_alert_by_vehicle_by_id(
                fid="fid",
                vid="vid",
                tid="tid",
                aid="aid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_trip_alert_by_vehicle_by_id(
            fid, vid, tid, aid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_path_for_trip(
        self,
        fid: str,
        vid: str,
        tid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tolerance: typing.Optional[float] = None,
        profile: typing.Optional[DataProfile] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WayPoints:
        """
        Gives the Vehicle's wayPoints for a specified Trip.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

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

        tolerance : typing.Optional[float]
            Tolerance factor is expressed in length km unit and is used to simplify path by reducing the total number of points by is using Douglas-Peucker algorithm to find a similar curve with fewer points (find more info here: [Ramer_Douglas_Peucker_algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm#Algorithm) ).

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page for high frequency data upload. When not set, at most 60 results will be returned.  The range for this parameter is [1...2000]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WayPoints
            Path response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.trips.get_path_for_trip(
                fid="fid",
                vid="vid",
                tid="tid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_path_for_trip(
            fid,
            vid,
            tid,
            index_range=index_range,
            timestamps=timestamps,
            tolerance=tolerance,
            profile=profile,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_telemetry_for_trip_by_vehicle(
        self,
        fid: str,
        vid: str,
        tid: str,
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
        Returns the set of Telemetry values that occurred for a given vehicle (id) and a speific Trip (tid) during the timestamp ranges and bounded by an index range.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        vid : str
            Resource is related to this Vehicle ID only.

        tid : str
            The ID {tid} of Trip

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
            await client.trips.get_telemetry_for_trip_by_vehicle(
                fid="fid",
                vid="vid",
                tid="tid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_telemetry_for_trip_by_vehicle(
            fid,
            vid,
            tid,
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
