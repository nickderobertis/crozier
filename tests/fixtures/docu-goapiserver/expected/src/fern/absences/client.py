

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.absence import Absence
from .raw_client import AsyncRawAbsencesClient, RawAbsencesClient
from .types.get_absences_v3request_sort_by import GetAbsencesV3RequestSortBy


class AbsencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAbsencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAbsencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAbsencesClient
        """
        return self._raw_client

    def get_absences_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        student_id: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        sort_by: typing.Optional[GetAbsencesV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Absence]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide school_id or student_id; student_id takes precedence when both are supplied (both IDs are still validated). Provide date_from, optionally date_to (defaults to today), OR a positive last_n_days. last_n_days cannot be combined with either date bound. Default order is date descending.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        student_id : typing.Optional[str]
            Required when school_id is omitted; takes precedence over school_id.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        last_n_days : typing.Optional[int]
            Rolling date window; mutually exclusive with explicit dates.

        sort_by : typing.Optional[GetAbsencesV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Absence]
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.absences.get_absences_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
            date_from=datetime.date.fromisoformat(
                "2026-01-01",
            ),
            date_to=datetime.date.fromisoformat(
                "2026-01-31",
            ),
        )
        """
        _response = self._raw_client.get_absences_v3(
            company_id=company_id,
            school_id=school_id,
            student_id=student_id,
            date_from=date_from,
            date_to=date_to,
            last_n_days=last_n_days,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data


class AsyncAbsencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAbsencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAbsencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAbsencesClient
        """
        return self._raw_client

    async def get_absences_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        student_id: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        sort_by: typing.Optional[GetAbsencesV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Absence]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide school_id or student_id; student_id takes precedence when both are supplied (both IDs are still validated). Provide date_from, optionally date_to (defaults to today), OR a positive last_n_days. last_n_days cannot be combined with either date bound. Default order is date descending.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        student_id : typing.Optional[str]
            Required when school_id is omitted; takes precedence over school_id.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        last_n_days : typing.Optional[int]
            Rolling date window; mutually exclusive with explicit dates.

        sort_by : typing.Optional[GetAbsencesV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Absence]
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
            await client.absences.get_absences_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
                date_from=datetime.date.fromisoformat(
                    "2026-01-01",
                ),
                date_to=datetime.date.fromisoformat(
                    "2026-01-31",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_absences_v3(
            company_id=company_id,
            school_id=school_id,
            student_id=student_id,
            date_from=date_from,
            date_to=date_to,
            last_n_days=last_n_days,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data
