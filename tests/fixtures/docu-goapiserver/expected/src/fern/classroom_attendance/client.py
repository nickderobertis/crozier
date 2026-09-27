

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.classroom_attendance import ClassroomAttendance
from .raw_client import AsyncRawClassroomAttendanceClient, RawClassroomAttendanceClient


class ClassroomAttendanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClassroomAttendanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClassroomAttendanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClassroomAttendanceClient
        """
        return self._raw_client

    def get_classroom_attendance_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        date: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassroomAttendance:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Daily classroom counters and student states, with their synchronization timestamp. date defaults to the current server date. Returns 404 if no snapshot exists.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        date : typing.Optional[dt.date]
            Snapshot calendar date; defaults to today.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassroomAttendance
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.classroom_attendance.get_classroom_attendance_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
            date=datetime.date.fromisoformat(
                "2026-01-15",
            ),
        )
        """
        _response = self._raw_client.get_classroom_attendance_v3(
            company_id=company_id, school_id=school_id, date=date, request_options=request_options
        )
        return _response.data


class AsyncClassroomAttendanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClassroomAttendanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClassroomAttendanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClassroomAttendanceClient
        """
        return self._raw_client

    async def get_classroom_attendance_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        date: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassroomAttendance:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Daily classroom counters and student states, with their synchronization timestamp. date defaults to the current server date. Returns 404 if no snapshot exists.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        date : typing.Optional[dt.date]
            Snapshot calendar date; defaults to today.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassroomAttendance
            Successful response.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.classroom_attendance.get_classroom_attendance_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
                date=datetime.date.fromisoformat(
                    "2026-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_classroom_attendance_v3(
            company_id=company_id, school_id=school_id, date=date, request_options=request_options
        )
        return _response.data
