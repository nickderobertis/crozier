

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.enrollment_tracker import EnrollmentTracker
from .raw_client import AsyncRawEnrollmentTrackerClient, RawEnrollmentTrackerClient


class EnrollmentTrackerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnrollmentTrackerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnrollmentTrackerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnrollmentTrackerClient
        """
        return self._raw_client

    def get_enrollment_tracker_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[str] = None,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnrollmentTracker:
        """
        Requires school_id assigned to the session. Returns the school tracker grid and computed enrollment information, optionally narrowed by room_id and monthly period. Returns 404 if the tracker is absent.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        room_id : typing.Optional[str]
            Optional room UUID.

        period : typing.Optional[str]
            Optional monthly period in YYYY-MM.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnrollmentTracker
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enrollment_tracker.get_enrollment_tracker_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_enrollment_tracker_v3(
            company_id=company_id, school_id=school_id, room_id=room_id, period=period, request_options=request_options
        )
        return _response.data


class AsyncEnrollmentTrackerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnrollmentTrackerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnrollmentTrackerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnrollmentTrackerClient
        """
        return self._raw_client

    async def get_enrollment_tracker_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[str] = None,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnrollmentTracker:
        """
        Requires school_id assigned to the session. Returns the school tracker grid and computed enrollment information, optionally narrowed by room_id and monthly period. Returns 404 if the tracker is absent.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        room_id : typing.Optional[str]
            Optional room UUID.

        period : typing.Optional[str]
            Optional monthly period in YYYY-MM.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnrollmentTracker
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enrollment_tracker.get_enrollment_tracker_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enrollment_tracker_v3(
            company_id=company_id, school_id=school_id, room_id=room_id, period=period, request_options=request_options
        )
        return _response.data
