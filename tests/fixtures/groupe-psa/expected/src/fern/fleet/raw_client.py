

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
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
from pydantic import ValidationError


class RawFleetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_fleets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Fleets]:
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
        HttpResponse[Fleets]
            Fleet list response
        """
        _response = self._client_wrapper.httpx_client.request(
            "fleets",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fleets,
                    parse_obj_as(
                        type_=Fleets,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_fleet(self, fid: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Fleet]:
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
        HttpResponse[Fleet]
            Fleet response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_fleet_status_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StatusList]:
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
        HttpResponse[StatusList]
            A list of Status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/status",
            method="GET",
            params={
                "profile": profile,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatusList,
                    parse_obj_as(
                        type_=StatusList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_fleet_mantenance_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MaintenanceList]:
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
        HttpResponse[MaintenanceList]
            A list of vehicle maintenance
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/maintenances",
            method="GET",
            params={
                "profile": profile,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MaintenanceList,
                    parse_obj_as(
                        type_=MaintenanceList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Alerts]:
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
        HttpResponse[Alerts]
            A list of alert
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/alerts",
            method="GET",
            params={
                "profile": profile,
                "timestamps": timestamps,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Alerts,
                    parse_obj_as(
                        type_=Alerts,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_fleet_alert_by_id(
        self,
        fid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Alert]:
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
        HttpResponse[Alert]
            Alert response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/alerts/{encode_path_param(aid)}",
            method="GET",
            params={
                "profile": profile,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Alert,
                    parse_obj_as(
                        type_=Alert,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Trips]:
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
        HttpResponse[Trips]
            A list of Trip
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/trips",
            method="GET",
            params={
                "profile": profile,
                "timestamps": timestamps,
                "distance": distance,
                "duration": duration,
                "states": states,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Trips,
                    parse_obj_as(
                        type_=Trips,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Collisions]:
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
        HttpResponse[Collisions]
            A list of Collision
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/collisions",
            method="GET",
            params={
                "profile": profile,
                "pageToken": page_token,
                "timestamps": timestamps,
                "indexRange": index_range,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collisions,
                    parse_obj_as(
                        type_=Collisions,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_collisions_by_id(
        self,
        fid: str,
        cid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Collision]:
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
        HttpResponse[Collision]
            Collision response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/collisions/{encode_path_param(cid)}",
            method="GET",
            params={
                "profile": profile,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collision,
                    parse_obj_as(
                        type_=Collision,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFleetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_fleets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Fleets]:
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
        AsyncHttpResponse[Fleets]
            Fleet list response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "fleets",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fleets,
                    parse_obj_as(
                        type_=Fleets,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_fleet(
        self, fid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Fleet]:
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
        AsyncHttpResponse[Fleet]
            Fleet response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_fleet_status_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StatusList]:
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
        AsyncHttpResponse[StatusList]
            A list of Status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/status",
            method="GET",
            params={
                "profile": profile,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatusList,
                    parse_obj_as(
                        type_=StatusList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_fleet_mantenance_list(
        self,
        fid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MaintenanceList]:
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
        AsyncHttpResponse[MaintenanceList]
            A list of vehicle maintenance
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/maintenances",
            method="GET",
            params={
                "profile": profile,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MaintenanceList,
                    parse_obj_as(
                        type_=MaintenanceList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Alerts]:
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
        AsyncHttpResponse[Alerts]
            A list of alert
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/alerts",
            method="GET",
            params={
                "profile": profile,
                "timestamps": timestamps,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Alerts,
                    parse_obj_as(
                        type_=Alerts,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_fleet_alert_by_id(
        self,
        fid: str,
        aid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Alert]:
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
        AsyncHttpResponse[Alert]
            Alert response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/alerts/{encode_path_param(aid)}",
            method="GET",
            params={
                "profile": profile,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Alert,
                    parse_obj_as(
                        type_=Alert,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Trips]:
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
        AsyncHttpResponse[Trips]
            A list of Trip
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/trips",
            method="GET",
            params={
                "profile": profile,
                "timestamps": timestamps,
                "distance": distance,
                "duration": duration,
                "states": states,
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Trips,
                    parse_obj_as(
                        type_=Trips,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Collisions]:
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
        AsyncHttpResponse[Collisions]
            A list of Collision
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/collisions",
            method="GET",
            params={
                "profile": profile,
                "pageToken": page_token,
                "timestamps": timestamps,
                "indexRange": index_range,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collisions,
                    parse_obj_as(
                        type_=Collisions,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_collisions_by_id(
        self,
        fid: str,
        cid: str,
        *,
        profile: typing.Optional[DataProfile] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Collision]:
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
        AsyncHttpResponse[Collision]
            Collision response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/collisions/{encode_path_param(cid)}",
            method="GET",
            params={
                "profile": profile,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collision,
                    parse_obj_as(
                        type_=Collision,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
