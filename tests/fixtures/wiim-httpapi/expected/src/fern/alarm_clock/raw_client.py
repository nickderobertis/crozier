

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawAlarmClockClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_time_sync(
        self, yyyymmddhhmmss: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        If the device has no internet access, you need to sync its time with:


        http://10.10.10.254/httpapi.asp?command=timeSync:YYYYMMDDHHMMSS


        YYYY is year (such as 2015), MM is month (01~12), DD is day (01~31), HH
        is hour (00~23),

        MM is minute (00~59), SS is second (00~59)


        In UTC

        Parameters
        ----------
        yyyymmddhhmmss : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"timeSync:{encode_path_param(yyyymmddhhmmss)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_alarm_clock(
        self,
        n: int,
        trig: int,
        op: int,
        time: str,
        day: str,
        url: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=setAlarmClock:n:trig:op:time[:day][:url]


        n: 0~2, currently support max 3 alarm


        trig: the alarm trigger:

        0 cancel the alarm, for example: setAlarmClock:n:0

        1 once, day should be YYYYMMDD

        2 every day

        3 every week, day should be 2 bytes ("00"~"06"), means from Sunday to
        Saturday.

        4 every week, day should be 2 bytes, the bit 0 to bit 6 means the
        effect, for example,

        "7F" means every day in week, "01" means only Sunday

        5 every month, day should be 2 bytes ("01"~"31")


        op: the action

        0 shell execute

        1 playback or ring

        2 stop playback

        time: should be HHMMSS, in UTC


        day:

        if trigger is 0 or 2, no need to set.

        if trigger is 1, should be YYYYMMDD ( %04d%02d%02d)

        if trigger is 3, day should be 2 bytes ("00"~"06"), means from Sunday to
        Saturday.

        if trigger is 4, day should be 2 bytes, the bit 0 to bit 6 means the
        effect, for example,

        "7F" means every day in week, "01" means only Sunday

        if trigger is 5, day should be 2 bytes ("01"~"31")


        url: the shell path or playback url, should less than 256 bytes

        Parameters
        ----------
        n : int
            The alarm clock number

            currently support max 3 alarm

        trig : int
            The alarm trigger


            0 cancel the alarm, for example: setAlarmClock:n:0

            1 once, day should be YYYYMMDD

            2 every day

            3 every week, day should be 2 bytes (00"~"06"), means from Sunday to
            Saturday.

            4 every week, day should be 2 bytes, the bit 0 to bit 6 means the
            effect, for example,

            "7F" means every day in week, "01" means only Sunday

            5 every month, day should be 2 bytes ("01"~"31")

        op : int
            The action

            0 shell execute
            1 playback or ring
            2 stop playback

        time : str
            should be HHMMSS, in UTC

        day : str
            if trigger is 0 or 2, no need to set.


            if trigger is 1, should be YYYYMMDD ( %04d%02d%02d)


            if trigger is 3, day should be 2 bytes ("00"~"06"), means from
            Sunday to Saturday.


            if trigger is 4, day should be 2 bytes, the bit 0 to bit 6 means the
            effect, for example,

            "7F" means every day in week, "01" means only Sunday


            if trigger is 5, day should be 2 bytes ("01"~"31")

        url : str
            The shell path or playback url, should less than 256 bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"setAlarmClock:{encode_path_param(n)}:{encode_path_param(trig)}:{encode_path_param(op)}:{encode_path_param(time)}:{encode_path_param(day)}:{encode_path_param(url)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_alarm_clock(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=getAlarmClock:n

        n: 0~2, currently support max 3 alarm
        {"enable":"1",
        "trigger":"%d",
        "operation":"%d",
        "date"::"%02d:%02d:%02d", //if not a "every day" alarm, no this
        "week_day":"%d", //if not a "every week" alarm, no this
        "day":"%02d", //if not a "every month" alarm, no this
        "time":"%02d:02d:%02d",
        "path":"%s""}

        Parameters
        ----------
        n : int
            The alarm clock number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"getAlarmClock:{encode_path_param(n)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def stop_alarm_clock(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=alarmStop

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "alarmStop",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAlarmClockClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_time_sync(
        self, yyyymmddhhmmss: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        If the device has no internet access, you need to sync its time with:


        http://10.10.10.254/httpapi.asp?command=timeSync:YYYYMMDDHHMMSS


        YYYY is year (such as 2015), MM is month (01~12), DD is day (01~31), HH
        is hour (00~23),

        MM is minute (00~59), SS is second (00~59)


        In UTC

        Parameters
        ----------
        yyyymmddhhmmss : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"timeSync:{encode_path_param(yyyymmddhhmmss)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_alarm_clock(
        self,
        n: int,
        trig: int,
        op: int,
        time: str,
        day: str,
        url: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=setAlarmClock:n:trig:op:time[:day][:url]


        n: 0~2, currently support max 3 alarm


        trig: the alarm trigger:

        0 cancel the alarm, for example: setAlarmClock:n:0

        1 once, day should be YYYYMMDD

        2 every day

        3 every week, day should be 2 bytes ("00"~"06"), means from Sunday to
        Saturday.

        4 every week, day should be 2 bytes, the bit 0 to bit 6 means the
        effect, for example,

        "7F" means every day in week, "01" means only Sunday

        5 every month, day should be 2 bytes ("01"~"31")


        op: the action

        0 shell execute

        1 playback or ring

        2 stop playback

        time: should be HHMMSS, in UTC


        day:

        if trigger is 0 or 2, no need to set.

        if trigger is 1, should be YYYYMMDD ( %04d%02d%02d)

        if trigger is 3, day should be 2 bytes ("00"~"06"), means from Sunday to
        Saturday.

        if trigger is 4, day should be 2 bytes, the bit 0 to bit 6 means the
        effect, for example,

        "7F" means every day in week, "01" means only Sunday

        if trigger is 5, day should be 2 bytes ("01"~"31")


        url: the shell path or playback url, should less than 256 bytes

        Parameters
        ----------
        n : int
            The alarm clock number

            currently support max 3 alarm

        trig : int
            The alarm trigger


            0 cancel the alarm, for example: setAlarmClock:n:0

            1 once, day should be YYYYMMDD

            2 every day

            3 every week, day should be 2 bytes (00"~"06"), means from Sunday to
            Saturday.

            4 every week, day should be 2 bytes, the bit 0 to bit 6 means the
            effect, for example,

            "7F" means every day in week, "01" means only Sunday

            5 every month, day should be 2 bytes ("01"~"31")

        op : int
            The action

            0 shell execute
            1 playback or ring
            2 stop playback

        time : str
            should be HHMMSS, in UTC

        day : str
            if trigger is 0 or 2, no need to set.


            if trigger is 1, should be YYYYMMDD ( %04d%02d%02d)


            if trigger is 3, day should be 2 bytes ("00"~"06"), means from
            Sunday to Saturday.


            if trigger is 4, day should be 2 bytes, the bit 0 to bit 6 means the
            effect, for example,

            "7F" means every day in week, "01" means only Sunday


            if trigger is 5, day should be 2 bytes ("01"~"31")

        url : str
            The shell path or playback url, should less than 256 bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"setAlarmClock:{encode_path_param(n)}:{encode_path_param(trig)}:{encode_path_param(op)}:{encode_path_param(time)}:{encode_path_param(day)}:{encode_path_param(url)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_alarm_clock(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=getAlarmClock:n

        n: 0~2, currently support max 3 alarm
        {"enable":"1",
        "trigger":"%d",
        "operation":"%d",
        "date"::"%02d:%02d:%02d", //if not a "every day" alarm, no this
        "week_day":"%d", //if not a "every week" alarm, no this
        "day":"%02d", //if not a "every month" alarm, no this
        "time":"%02d:02d:%02d",
        "path":"%s""}

        Parameters
        ----------
        n : int
            The alarm clock number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"getAlarmClock:{encode_path_param(n)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def stop_alarm_clock(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=alarmStop

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "alarmStop",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
