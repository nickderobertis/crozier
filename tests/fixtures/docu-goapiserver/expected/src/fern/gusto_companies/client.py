

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.employee_time_off import EmployeeTimeOff
from ..types.gusto_company import GustoCompany
from .raw_client import AsyncRawGustoCompaniesClient, RawGustoCompaniesClient


class GustoCompaniesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGustoCompaniesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGustoCompaniesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGustoCompaniesClient
        """
        return self._raw_client

    def get_gusto_companies_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GustoCompany]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the company catalog as an unpaginated array.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GustoCompany]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_companies.get_gusto_companies_v3(
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_gusto_companies_v3(company_id=company_id, request_options=request_options)
        return _response.data

    def get_gusto_companies_id_time_off_v3(
        self,
        id: str,
        *,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EmployeeTimeOff]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. First verifies that the Gusto company belongs to company_id, returning 404 if absent. Defaults date_to to today and date_from to three calendar months before date_to. date_to cannot precede date_from. Sorts by effective_time ascending, breaking ties by employee_id.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        employee_id : typing.Optional[str]
            Restrict to one employee UUID.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Both bounds are optional; see operation defaults.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Both bounds are optional; see operation defaults.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EmployeeTimeOff]
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_companies.get_gusto_companies_id_time_off_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            date_from=datetime.date.fromisoformat(
                "2026-01-01",
            ),
            date_to=datetime.date.fromisoformat(
                "2026-01-31",
            ),
        )
        """
        _response = self._raw_client.get_gusto_companies_id_time_off_v3(
            id,
            company_id=company_id,
            employee_id=employee_id,
            date_from=date_from,
            date_to=date_to,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    def get_gusto_companies_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GustoCompany:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The ID is the internal record UUID. Records outside the requested company return 404.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GustoCompany
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_companies.get_gusto_companies_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_gusto_companies_id_v3(
            id, company_id=company_id, request_options=request_options
        )
        return _response.data


class AsyncGustoCompaniesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGustoCompaniesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGustoCompaniesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGustoCompaniesClient
        """
        return self._raw_client

    async def get_gusto_companies_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GustoCompany]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the company catalog as an unpaginated array.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GustoCompany]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_companies.get_gusto_companies_v3(
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_companies_v3(
            company_id=company_id, request_options=request_options
        )
        return _response.data

    async def get_gusto_companies_id_time_off_v3(
        self,
        id: str,
        *,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EmployeeTimeOff]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. First verifies that the Gusto company belongs to company_id, returning 404 if absent. Defaults date_to to today and date_from to three calendar months before date_to. date_to cannot precede date_from. Sorts by effective_time ascending, breaking ties by employee_id.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        employee_id : typing.Optional[str]
            Restrict to one employee UUID.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Both bounds are optional; see operation defaults.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Both bounds are optional; see operation defaults.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EmployeeTimeOff]
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
            await client.gusto_companies.get_gusto_companies_id_time_off_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                date_from=datetime.date.fromisoformat(
                    "2026-01-01",
                ),
                date_to=datetime.date.fromisoformat(
                    "2026-01-31",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_companies_id_time_off_v3(
            id,
            company_id=company_id,
            employee_id=employee_id,
            date_from=date_from,
            date_to=date_to,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    async def get_gusto_companies_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GustoCompany:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The ID is the internal record UUID. Records outside the requested company return 404.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GustoCompany
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_companies.get_gusto_companies_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_companies_id_v3(
            id, company_id=company_id, request_options=request_options
        )
        return _response.data
