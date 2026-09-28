

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.waitlist import Waitlist
from .raw_client import AsyncRawWaitlistClient, RawWaitlistClient
from .types.get_waitlist_v3request_sort_by import GetWaitlistV3RequestSortBy


OMIT = typing.cast(typing.Any, ...)


class WaitlistClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWaitlistClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWaitlistClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWaitlistClient
        """
        return self._raw_client

    def get_waitlist_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        query: typing.Optional[str] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetWaitlistV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Waitlist]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Waitlist entries with room eligibility derived from the preferred start date.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        query : typing.Optional[str]
            Search text passed to the waitlist student lookup.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetWaitlistV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Waitlist]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.waitlist.get_waitlist_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_waitlist_v3(
            company_id=company_id,
            school_id=school_id,
            query=query,
            has_alerts=has_alerts,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    def get_waitlist_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Waitlist:
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
        Waitlist
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.waitlist.get_waitlist_student_id_v3(
            student_id="student_id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_waitlist_student_id_v3(
            student_id, company_id=company_id, request_options=request_options
        )
        return _response.data

    def patch_waitlist_student_id_v3(
        self,
        student_id: str,
        *,
        company_id: str,
        preferred_start_date: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Waitlist:
        """
        The student must exist in Waitlist onboarding status and belong to a school assigned to the session. preferred_start_date must be later than today. Recomputes and returns the waitlist entry and room eligibility. Clearing this date is not supported. The update may have executed if the subsequent read returns 500.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        preferred_start_date : dt.date
            Required future date. Today, past dates, empty strings and null are rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Waitlist
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.waitlist.patch_waitlist_student_id_v3(
            student_id="student_id",
            company_id="11111111-1111-4111-8111-111111111111",
            preferred_start_date=datetime.date.fromisoformat(
                "2030-09-01",
            ),
        )
        """
        _response = self._raw_client.patch_waitlist_student_id_v3(
            student_id,
            company_id=company_id,
            preferred_start_date=preferred_start_date,
            request_options=request_options,
        )
        return _response.data


class AsyncWaitlistClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWaitlistClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWaitlistClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWaitlistClient
        """
        return self._raw_client

    async def get_waitlist_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        query: typing.Optional[str] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetWaitlistV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Waitlist]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Waitlist entries with room eligibility derived from the preferred start date.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        query : typing.Optional[str]
            Search text passed to the waitlist student lookup.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetWaitlistV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Waitlist]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.waitlist.get_waitlist_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_waitlist_v3(
            company_id=company_id,
            school_id=school_id,
            query=query,
            has_alerts=has_alerts,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    async def get_waitlist_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Waitlist:
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
        Waitlist
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.waitlist.get_waitlist_student_id_v3(
                student_id="student_id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_waitlist_student_id_v3(
            student_id, company_id=company_id, request_options=request_options
        )
        return _response.data

    async def patch_waitlist_student_id_v3(
        self,
        student_id: str,
        *,
        company_id: str,
        preferred_start_date: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Waitlist:
        """
        The student must exist in Waitlist onboarding status and belong to a school assigned to the session. preferred_start_date must be later than today. Recomputes and returns the waitlist entry and room eligibility. Clearing this date is not supported. The update may have executed if the subsequent read returns 500.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        preferred_start_date : dt.date
            Required future date. Today, past dates, empty strings and null are rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Waitlist
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
            await client.waitlist.patch_waitlist_student_id_v3(
                student_id="student_id",
                company_id="11111111-1111-4111-8111-111111111111",
                preferred_start_date=datetime.date.fromisoformat(
                    "2030-09-01",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_waitlist_student_id_v3(
            student_id,
            company_id=company_id,
            preferred_start_date=preferred_start_date,
            request_options=request_options,
        )
        return _response.data
