

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alert import Alert
from ..types.alerts import Alerts
from ..types.collision import Collision
from ..types.collisions import Collisions
from ..types.data_profile import DataProfile
from ..types.fleet import Fleet
from ..types.fleets import Fleets
from ..types.index_range import IndexRange
from ..types.maintenance_list import MaintenanceList
from ..types.range import Range
from ..types.status_list import StatusList
from ..types.trip_state_enum import TripStateEnum
from ..types.trips import Trips
from .raw_client import AsyncRawFleetClient, RawFleetClient


class FleetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFleetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFleetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFleetClient
        """
        return self._raw_client

    def get_fleets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Fleets:
        """
        Returns all Fleets owned by a partner.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleets
            Fleet list response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fleet.get_fleets()
        """
        _response = self._raw_client.get_fleets(
            page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    def get_fleet(self, fid: str, *, request_options: typing.Optional[RequestOptions] = None) -> Fleet:
        """
        Returns the Fleet's information.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Fleet response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fleet.get_fleet(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet(fid, request_options=request_options)
        return _response.data

    def get_fleet_status_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusList:
        """
        Returns the latest vehicles status for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
        StatusList
            A list of Status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fleet.get_fleet_status_list(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet_status_list(
            fid,
            profile=profile,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_mantenance_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MaintenanceList:
        """
        Returns the latest vehicles maintenance list for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
        MaintenanceList
            A list of vehicle maintenance

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fleet.get_fleet_mantenance_list(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet_mantenance_list(
            fid,
            profile=profile,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_alert_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alerts:
        """
        Returns the vehicles alerts list for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
        client.fleet.get_fleet_alert_list(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet_alert_list(
            fid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_alert_by_id(
        self,
        fid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alert:
        """
        Returns information about a specific alert message for a given fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
        client.fleet.get_fleet_alert_by_id(
            fid="fid",
            aid="aid",
        )
        """
        _response = self._raw_client.get_fleet_alert_by_id(fid, aid, profile=profile, request_options=request_options)
        return _response.data

    def get_fleet_trips(
        self,
        fid: str,
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
        This method returns a list of all Trips. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
        client.fleet.get_fleet_trips(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet_trips(
            fid,
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

    def get_fleet_trip_collisions(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        page_token: typing.Optional[str] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collisions:
        """
        Returns the list of Collisions that occured on vehicles' fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
        client.fleet.get_fleet_trip_collisions(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet_trip_collisions(
            fid,
            profile=profile,
            page_token=page_token,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def get_collisions_by_id(
        self,
        fid: str,
        cid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collision:
        """
        Returns the Collision that matches the fleet id and the Collision cid.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
        client.fleet.get_collisions_by_id(
            fid="fid",
            cid="cid",
        )
        """
        _response = self._raw_client.get_collisions_by_id(fid, cid, profile=profile, request_options=request_options)
        return _response.data


class AsyncFleetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFleetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFleetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFleetClient
        """
        return self._raw_client

    async def get_fleets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Fleets:
        """
        Returns all Fleets owned by a partner.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleets
            Fleet list response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fleet.get_fleets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleets(
            page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def get_fleet(self, fid: str, *, request_options: typing.Optional[RequestOptions] = None) -> Fleet:
        """
        Returns the Fleet's information.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Fleet response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fleet.get_fleet(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet(fid, request_options=request_options)
        return _response.data

    async def get_fleet_status_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusList:
        """
        Returns the latest vehicles status for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
        StatusList
            A list of Status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fleet.get_fleet_status_list(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_status_list(
            fid,
            profile=profile,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_mantenance_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MaintenanceList:
        """
        Returns the latest vehicles maintenance list for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
        MaintenanceList
            A list of vehicle maintenance

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fleet.get_fleet_mantenance_list(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_mantenance_list(
            fid,
            profile=profile,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_alert_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alerts:
        """
        Returns the vehicles alerts list for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
            await client.fleet.get_fleet_alert_list(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_alert_list(
            fid,
            profile=profile,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_alert_by_id(
        self,
        fid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Alert:
        """
        Returns information about a specific alert message for a given fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
            await client.fleet.get_fleet_alert_by_id(
                fid="fid",
                aid="aid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_alert_by_id(
            fid, aid, profile=profile, request_options=request_options
        )
        return _response.data

    async def get_fleet_trips(
        self,
        fid: str,
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
        This method returns a list of all Trips. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
            await client.fleet.get_fleet_trips(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_trips(
            fid,
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

    async def get_fleet_trip_collisions(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        page_token: typing.Optional[str] = None,
        timestamps: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collisions:
        """
        Returns the list of Collisions that occured on vehicles' fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        profile : typing.Optional[DataProfile]
            Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

             * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level.

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
            await client.fleet.get_fleet_trip_collisions(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_trip_collisions(
            fid,
            profile=profile,
            page_token=page_token,
            timestamps=timestamps,
            index_range=index_range,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def get_collisions_by_id(
        self,
        fid: str,
        cid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collision:
        """
        Returns the Collision that matches the fleet id and the Collision cid.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

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
            await client.fleet.get_collisions_by_id(
                fid="fid",
                cid="cid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collisions_by_id(
            fid, cid, profile=profile, request_options=request_options
        )
        return _response.data
