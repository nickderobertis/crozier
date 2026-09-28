

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.new_start_student import NewStartStudent
from .raw_client import AsyncRawNewStartTrackerClient, RawNewStartTrackerClient
from .types.get_new_start_tracker_v3request_ems_student_status import GetNewStartTrackerV3RequestEmsStudentStatus
from .types.get_new_start_tracker_v3request_sort_by import GetNewStartTrackerV3RequestSortBy


class NewStartTrackerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNewStartTrackerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNewStartTrackerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNewStartTrackerClient
        """
        return self._raw_client

    def get_new_start_tracker_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        ems_student_status: typing.Optional[GetNewStartTrackerV3RequestEmsStudentStatus] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetNewStartTrackerV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NewStartStudent]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Start-date invoicing, service windows, and pro-rate information per student.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        ems_student_status : typing.Optional[GetNewStartTrackerV3RequestEmsStudentStatus]
            Optional onboarding status, matched case-insensitively.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetNewStartTrackerV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NewStartStudent]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.new_start_tracker.get_new_start_tracker_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_new_start_tracker_v3(
            company_id=company_id,
            school_id=school_id,
            ems_student_status=ems_student_status,
            has_alerts=has_alerts,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    def get_new_start_tracker_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> NewStartStudent:
        """
        The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewStartStudent
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.new_start_tracker.get_new_start_tracker_student_id_v3(
            student_id="student_id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_new_start_tracker_student_id_v3(
            student_id, company_id=company_id, request_options=request_options
        )
        return _response.data


class AsyncNewStartTrackerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNewStartTrackerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNewStartTrackerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNewStartTrackerClient
        """
        return self._raw_client

    async def get_new_start_tracker_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        ems_student_status: typing.Optional[GetNewStartTrackerV3RequestEmsStudentStatus] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetNewStartTrackerV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[NewStartStudent]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Start-date invoicing, service windows, and pro-rate information per student.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        ems_student_status : typing.Optional[GetNewStartTrackerV3RequestEmsStudentStatus]
            Optional onboarding status, matched case-insensitively.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetNewStartTrackerV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NewStartStudent]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.new_start_tracker.get_new_start_tracker_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_new_start_tracker_v3(
            company_id=company_id,
            school_id=school_id,
            ems_student_status=ems_student_status,
            has_alerts=has_alerts,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    async def get_new_start_tracker_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> NewStartStudent:
        """
        The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NewStartStudent
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.new_start_tracker.get_new_start_tracker_student_id_v3(
                student_id="student_id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_new_start_tracker_student_id_v3(
            student_id, company_id=company_id, request_options=request_options
        )
        return _response.data
