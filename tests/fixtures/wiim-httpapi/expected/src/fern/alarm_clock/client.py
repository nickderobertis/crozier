

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAlarmClockClient, RawAlarmClockClient


class AlarmClockClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAlarmClockClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAlarmClockClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAlarmClockClient
        """
        return self._raw_client

    def set_time_sync(self, yyyymmddhhmmss: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alarm_clock.set_time_sync(
            yyyymmddhhmmss="YYYYMMDDHHMMSS",
        )
        """
        _response = self._raw_client.set_time_sync(yyyymmddhhmmss, request_options=request_options)
        return _response.data

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
    ) -> str:
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
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alarm_clock.set_alarm_clock(
            n=1,
            trig=1,
            op=1,
            time="time",
            day="day",
            url="url",
        )
        """
        _response = self._raw_client.set_alarm_clock(n, trig, op, time, day, url, request_options=request_options)
        return _response.data

    def get_alarm_clock(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alarm_clock.get_alarm_clock(
            n=1,
        )
        """
        _response = self._raw_client.get_alarm_clock(n, request_options=request_options)
        return _response.data

    def stop_alarm_clock(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=alarmStop

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alarm_clock.stop_alarm_clock()
        """
        _response = self._raw_client.stop_alarm_clock(request_options=request_options)
        return _response.data


class AsyncAlarmClockClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAlarmClockClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAlarmClockClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAlarmClockClient
        """
        return self._raw_client

    async def set_time_sync(
        self, yyyymmddhhmmss: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
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
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alarm_clock.set_time_sync(
                yyyymmddhhmmss="YYYYMMDDHHMMSS",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_time_sync(yyyymmddhhmmss, request_options=request_options)
        return _response.data

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
    ) -> str:
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
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alarm_clock.set_alarm_clock(
                n=1,
                trig=1,
                op=1,
                time="time",
                day="day",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_alarm_clock(n, trig, op, time, day, url, request_options=request_options)
        return _response.data

    async def get_alarm_clock(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alarm_clock.get_alarm_clock(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alarm_clock(n, request_options=request_options)
        return _response.data

    async def stop_alarm_clock(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=alarmStop

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alarm_clock.stop_alarm_clock()


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_alarm_clock(request_options=request_options)
        return _response.data
