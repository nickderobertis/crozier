

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEnrollmentsClient, RawEnrollmentsClient
from .types.get_enrollments_v3request_group_by import GetEnrollmentsV3RequestGroupBy
from .types.get_enrollments_v3request_view import GetEnrollmentsV3RequestView
from .types.get_enrollments_v3response import GetEnrollmentsV3Response


class EnrollmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnrollmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnrollmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnrollmentsClient
        """
        return self._raw_client

    def get_enrollments_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetEnrollmentsV3RequestView] = None,
        group_by: typing.Optional[GetEnrollmentsV3RequestGroupBy] = None,
        period_from: typing.Optional[str] = None,
        period_to: typing.Optional[str] = None,
        year_from: typing.Optional[str] = None,
        year_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEnrollmentsV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The response representation is selected in this order:

        | Selection | Response | Date selectors |
        | --- | --- | --- |
        | view=trend | EnrollmentTrend array | Optional period_from/period_to |
        | group_by=period (unless trend) | EnrollmentPeriodAnalytics array | year_from/year_to |
        | view=analytics, group_by=month | EnrollmentAnalytics array | period_from/period_to |
        | Default: view=basic, group_by=month | EnrollmentMonthly array | period_from/period_to |

        Monthly basic/analytics default to 2023-01 through the current month. Period analytics defaults to 2023 through the current year. Trend uses the available calculated periods when bounds are omitted. No pagination is implemented. Each representation returns its row count in X-Total-Count. For view=trend, omit both range bounds or provide both; endpoints must lie within the available horizon. Incomplete, invalid, inverted or out-of-horizon trend ranges fail in the data layer and currently return HTTP 500.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetEnrollmentsV3RequestView]
            Select the representation.

        group_by : typing.Optional[GetEnrollmentsV3RequestGroupBy]
            period implies period analytics unless view=trend.

        period_from : typing.Optional[str]
            First monthly period for monthly or trend views.

        period_to : typing.Optional[str]
            Last monthly period for monthly or trend views.

        year_from : typing.Optional[str]
            First year for group_by=period; defaults to 2023.

        year_to : typing.Optional[str]
            Last year for group_by=period; defaults to the current year.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEnrollmentsV3Response
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enrollments.get_enrollments_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_enrollments_v3(
            company_id=company_id,
            school_id=school_id,
            view=view,
            group_by=group_by,
            period_from=period_from,
            period_to=period_to,
            year_from=year_from,
            year_to=year_to,
            request_options=request_options,
        )
        return _response.data


class AsyncEnrollmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnrollmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnrollmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnrollmentsClient
        """
        return self._raw_client

    async def get_enrollments_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetEnrollmentsV3RequestView] = None,
        group_by: typing.Optional[GetEnrollmentsV3RequestGroupBy] = None,
        period_from: typing.Optional[str] = None,
        period_to: typing.Optional[str] = None,
        year_from: typing.Optional[str] = None,
        year_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEnrollmentsV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The response representation is selected in this order:

        | Selection | Response | Date selectors |
        | --- | --- | --- |
        | view=trend | EnrollmentTrend array | Optional period_from/period_to |
        | group_by=period (unless trend) | EnrollmentPeriodAnalytics array | year_from/year_to |
        | view=analytics, group_by=month | EnrollmentAnalytics array | period_from/period_to |
        | Default: view=basic, group_by=month | EnrollmentMonthly array | period_from/period_to |

        Monthly basic/analytics default to 2023-01 through the current month. Period analytics defaults to 2023 through the current year. Trend uses the available calculated periods when bounds are omitted. No pagination is implemented. Each representation returns its row count in X-Total-Count. For view=trend, omit both range bounds or provide both; endpoints must lie within the available horizon. Incomplete, invalid, inverted or out-of-horizon trend ranges fail in the data layer and currently return HTTP 500.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetEnrollmentsV3RequestView]
            Select the representation.

        group_by : typing.Optional[GetEnrollmentsV3RequestGroupBy]
            period implies period analytics unless view=trend.

        period_from : typing.Optional[str]
            First monthly period for monthly or trend views.

        period_to : typing.Optional[str]
            Last monthly period for monthly or trend views.

        year_from : typing.Optional[str]
            First year for group_by=period; defaults to 2023.

        year_to : typing.Optional[str]
            Last year for group_by=period; defaults to the current year.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEnrollmentsV3Response
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enrollments.get_enrollments_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enrollments_v3(
            company_id=company_id,
            school_id=school_id,
            view=view,
            group_by=group_by,
            period_from=period_from,
            period_to=period_to,
            year_from=year_from,
            year_to=year_to,
            request_options=request_options,
        )
        return _response.data
