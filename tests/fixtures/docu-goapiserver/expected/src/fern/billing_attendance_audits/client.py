

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.billing_attendance_audit import BillingAttendanceAudit
from .raw_client import AsyncRawBillingAttendanceAuditsClient, RawBillingAttendanceAuditsClient


class BillingAttendanceAuditsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillingAttendanceAuditsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillingAttendanceAuditsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillingAttendanceAuditsClient
        """
        return self._raw_client

    def get_billing_attendance_audits_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        last_n_days: int,
        unpaid_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BillingAttendanceAudit]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns attendance checked against billing, including unpaid_day. The backend supports a rolling window only: last_n_days is required. Each result is an attendance row flattened from its student record.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        last_n_days : int
            Required positive rolling-window length in days.

        unpaid_only : typing.Optional[bool]
            Restrict to unpaid attendance. Accepts true/1 and false/0, case-insensitive.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingAttendanceAudit]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_attendance_audits.get_billing_attendance_audits_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
            last_n_days=1,
        )
        """
        _response = self._raw_client.get_billing_attendance_audits_v3(
            company_id=company_id,
            school_id=school_id,
            last_n_days=last_n_days,
            unpaid_only=unpaid_only,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data


class AsyncBillingAttendanceAuditsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillingAttendanceAuditsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillingAttendanceAuditsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillingAttendanceAuditsClient
        """
        return self._raw_client

    async def get_billing_attendance_audits_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        last_n_days: int,
        unpaid_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BillingAttendanceAudit]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns attendance checked against billing, including unpaid_day. The backend supports a rolling window only: last_n_days is required. Each result is an attendance row flattened from its student record.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        last_n_days : int
            Required positive rolling-window length in days.

        unpaid_only : typing.Optional[bool]
            Restrict to unpaid attendance. Accepts true/1 and false/0, case-insensitive.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingAttendanceAudit]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_attendance_audits.get_billing_attendance_audits_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
                last_n_days=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_billing_attendance_audits_v3(
            company_id=company_id,
            school_id=school_id,
            last_n_days=last_n_days,
            unpaid_only=unpaid_only,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data
