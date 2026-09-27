

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPreRegistrationFalloutClient, RawPreRegistrationFalloutClient
from .types.get_pre_registration_fallout_v3request_sort_by import GetPreRegistrationFalloutV3RequestSortBy
from .types.get_pre_registration_fallout_v3request_view import GetPreRegistrationFalloutV3RequestView
from .types.get_pre_registration_fallout_v3response import GetPreRegistrationFalloutV3Response


class PreRegistrationFalloutClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPreRegistrationFalloutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPreRegistrationFalloutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPreRegistrationFalloutClient
        """
        return self._raw_client

    def get_pre_registration_fallout_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        view: typing.Optional[GetPreRegistrationFalloutV3RequestView] = None,
        year: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        withdrew_only: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetPreRegistrationFalloutV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPreRegistrationFalloutV3Response:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Omitting view returns a PreRegistrationFalloutReport object containing years, school_summaries and total_summary. view=students returns a paginated array of PreRegistrationFalloutStudent.

        The report accepts only company_id, school_id and view. The students view additionally accepts year, query, withdrew_only, sort_by, page and per_page. Any other parameter, including a students-only parameter on the report view, returns 400. year defaults to the current year; all includes every supported year. Supported years run from 2024 to the current year. Pagination headers are emitted only for view=students.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        view : typing.Optional[GetPreRegistrationFalloutV3RequestView]
            Omit for the full report; students selects paginated detail.

        year : typing.Optional[str]
            Students view only: a year from 2024 through the current year, or all (case-insensitive). Defaults to the current year.

        query : typing.Optional[str]
            Students view only: student search text.

        withdrew_only : typing.Optional[bool]
            Students view only: restrict to withdrawals in the same year. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetPreRegistrationFalloutV3RequestSortBy]
            Students view only: sort column with _asc/_desc.

        page : typing.Optional[int]
            One-based page number. Applies only to view=students.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500. Applies only to view=students.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPreRegistrationFalloutV3Response
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pre_registration_fallout.get_pre_registration_fallout_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_pre_registration_fallout_v3(
            company_id=company_id,
            school_id=school_id,
            view=view,
            year=year,
            query=query,
            withdrew_only=withdrew_only,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data


class AsyncPreRegistrationFalloutClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPreRegistrationFalloutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPreRegistrationFalloutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPreRegistrationFalloutClient
        """
        return self._raw_client

    async def get_pre_registration_fallout_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        view: typing.Optional[GetPreRegistrationFalloutV3RequestView] = None,
        year: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        withdrew_only: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetPreRegistrationFalloutV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPreRegistrationFalloutV3Response:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Omitting view returns a PreRegistrationFalloutReport object containing years, school_summaries and total_summary. view=students returns a paginated array of PreRegistrationFalloutStudent.

        The report accepts only company_id, school_id and view. The students view additionally accepts year, query, withdrew_only, sort_by, page and per_page. Any other parameter, including a students-only parameter on the report view, returns 400. year defaults to the current year; all includes every supported year. Supported years run from 2024 to the current year. Pagination headers are emitted only for view=students.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        view : typing.Optional[GetPreRegistrationFalloutV3RequestView]
            Omit for the full report; students selects paginated detail.

        year : typing.Optional[str]
            Students view only: a year from 2024 through the current year, or all (case-insensitive). Defaults to the current year.

        query : typing.Optional[str]
            Students view only: student search text.

        withdrew_only : typing.Optional[bool]
            Students view only: restrict to withdrawals in the same year. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetPreRegistrationFalloutV3RequestSortBy]
            Students view only: sort column with _asc/_desc.

        page : typing.Optional[int]
            One-based page number. Applies only to view=students.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500. Applies only to view=students.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPreRegistrationFalloutV3Response
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pre_registration_fallout.get_pre_registration_fallout_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pre_registration_fallout_v3(
            company_id=company_id,
            school_id=school_id,
            view=view,
            year=year,
            query=query,
            withdrew_only=withdrew_only,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data
