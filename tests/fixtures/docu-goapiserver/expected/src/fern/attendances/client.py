

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAttendancesClient, RawAttendancesClient
from .types.get_attendances_v3request_fields_item import GetAttendancesV3RequestFieldsItem
from .types.get_attendances_v3request_group_by import GetAttendancesV3RequestGroupBy
from .types.get_attendances_v3request_metrics_item import GetAttendancesV3RequestMetricsItem
from .types.get_attendances_v3request_sort_by import GetAttendancesV3RequestSortBy
from .types.get_attendances_v3response import GetAttendancesV3Response


class AttendancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttendancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttendancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttendancesClient
        """
        return self._raw_client

    def get_attendances_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        min_hours: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[GetAttendancesV3RequestSortBy] = None,
        group_by: typing.Optional[GetAttendancesV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAttendancesV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide date_from AND date_to, or a positive last_n_days; mixing them returns 400. Defaults min_hours to 2; records below that threshold are excluded. room_id/room_ids and student_id/student_ids are merged. Row responses are sparse Attendance objects and support fields and pagination; sort_by on rows returns 400. group_by plus metrics selects nested AttendanceAggregate rows with a limit instead of pagination. Room/student filter counts, when positive, are returned in headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        room_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional room UUIDs; combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with student_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional student UUIDs; combined with student_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        last_n_days : typing.Optional[int]
            Positive rolling-window length; cannot be combined with either explicit date bound.

        min_hours : typing.Optional[float]
            Minimum hours attended per record. Use zero to include records below the historical two-hour threshold.

        fields : typing.Optional[typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: student_id, date, room_id, room_name, hours_attended. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[GetAttendancesV3RequestSortBy]
            Aggregate view only; sending sort_by without group_by returns 400. Default group_asc.

        group_by : typing.Optional[GetAttendancesV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Row view only.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Row view only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAttendancesV3Response
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attendances.get_attendances_v3(
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
        _response = self._raw_client.get_attendances_v3(
            company_id=company_id,
            school_id=school_id,
            room_id=room_id,
            room_ids=room_ids,
            student_id=student_id,
            student_ids=student_ids,
            date_from=date_from,
            date_to=date_to,
            last_n_days=last_n_days,
            min_hours=min_hours,
            fields=fields,
            sort_by=sort_by,
            group_by=group_by,
            metrics=metrics,
            limit=limit,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data


class AsyncAttendancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttendancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttendancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttendancesClient
        """
        return self._raw_client

    async def get_attendances_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        min_hours: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[GetAttendancesV3RequestSortBy] = None,
        group_by: typing.Optional[GetAttendancesV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAttendancesV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide date_from AND date_to, or a positive last_n_days; mixing them returns 400. Defaults min_hours to 2; records below that threshold are excluded. room_id/room_ids and student_id/student_ids are merged. Row responses are sparse Attendance objects and support fields and pagination; sort_by on rows returns 400. group_by plus metrics selects nested AttendanceAggregate rows with a limit instead of pagination. Room/student filter counts, when positive, are returned in headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        room_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional room UUIDs; combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with student_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional student UUIDs; combined with student_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        last_n_days : typing.Optional[int]
            Positive rolling-window length; cannot be combined with either explicit date bound.

        min_hours : typing.Optional[float]
            Minimum hours attended per record. Use zero to include records below the historical two-hour threshold.

        fields : typing.Optional[typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: student_id, date, room_id, room_name, hours_attended. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[GetAttendancesV3RequestSortBy]
            Aggregate view only; sending sort_by without group_by returns 400. Default group_asc.

        group_by : typing.Optional[GetAttendancesV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Row view only.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Row view only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAttendancesV3Response
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
            await client.attendances.get_attendances_v3(
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
        _response = await self._raw_client.get_attendances_v3(
            company_id=company_id,
            school_id=school_id,
            room_id=room_id,
            room_ids=room_ids,
            student_id=student_id,
            student_ids=student_ids,
            date_from=date_from,
            date_to=date_to,
            last_n_days=last_n_days,
            min_hours=min_hours,
            fields=fields,
            sort_by=sort_by,
            group_by=group_by,
            metrics=metrics,
            limit=limit,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data
