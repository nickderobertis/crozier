

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payroll import Payroll
from ..types.payroll_total import PayrollTotal
from .raw_client import AsyncRawGustoPayrollsClient, RawGustoPayrollsClient


class GustoPayrollsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGustoPayrollsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGustoPayrollsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGustoPayrollsClient
        """
        return self._raw_client

    def get_gusto_payrolls_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[Payroll]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. Omitting selectors reads the available payroll records for the school.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[Payroll]]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_payrolls.get_gusto_payrolls_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_gusto_payrolls_v3(
            company_id=company_id,
            school_id=school_id,
            period=period,
            period_from=period_from,
            period_to=period_to,
            request_options=request_options,
        )
        return _response.data

    def get_gusto_payrolls_totals_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[PayrollTotal]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. When selectors are omitted the totals return the most recent nine periods. Any period selector removes that cap.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[PayrollTotal]]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_payrolls.get_gusto_payrolls_totals_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_gusto_payrolls_totals_v3(
            company_id=company_id,
            school_id=school_id,
            period=period,
            period_from=period_from,
            period_to=period_to,
            request_options=request_options,
        )
        return _response.data


class AsyncGustoPayrollsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGustoPayrollsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGustoPayrollsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGustoPayrollsClient
        """
        return self._raw_client

    async def get_gusto_payrolls_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[Payroll]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. Omitting selectors reads the available payroll records for the school.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[Payroll]]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_payrolls.get_gusto_payrolls_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_payrolls_v3(
            company_id=company_id,
            school_id=school_id,
            period=period,
            period_from=period_from,
            period_to=period_to,
            request_options=request_options,
        )
        return _response.data

    async def get_gusto_payrolls_totals_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[PayrollTotal]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. When selectors are omitted the totals return the most recent nine periods. Any period selector removes that cap.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[PayrollTotal]]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_payrolls.get_gusto_payrolls_totals_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_payrolls_totals_v3(
            company_id=company_id,
            school_id=school_id,
            period=period,
            period_from=period_from,
            period_to=period_to,
            request_options=request_options,
        )
        return _response.data
