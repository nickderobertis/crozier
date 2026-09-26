

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment import Payment
from .raw_client import AsyncRawPaymentsClient, RawPaymentsClient
from .types.get_payments_id_v3request_fields_item import GetPaymentsIdV3RequestFieldsItem
from .types.get_payments_v3request_fields_item import GetPaymentsV3RequestFieldsItem
from .types.get_payments_v3request_group_by import GetPaymentsV3RequestGroupBy
from .types.get_payments_v3request_metrics_item import GetPaymentsV3RequestMetricsItem
from .types.get_payments_v3response import GetPaymentsV3Response


class PaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentsClient
        """
        return self._raw_client

    def get_payments_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_id: typing.Optional[str] = None,
        family_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_name: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        state: typing.Optional[str] = None,
        is_posted: typing.Optional[bool] = None,
        successful_only: typing.Optional[bool] = None,
        payment_mode: typing.Optional[str] = None,
        payment_method_sub_kind: typing.Optional[str] = None,
        min_amount: typing.Optional[float] = None,
        max_amount: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[str] = None,
        group_by: typing.Optional[GetPaymentsV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentsV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Without group_by, returns sparse payment rows. With group_by and metrics, returns nested PaymentAggregate rows. school_id and school_ids are both applied when provided (their intersection); omitted school filters read the company scope. Row queries support family_id/family_ids; these IDs do not filter the aggregate representation. fields and pagination apply only to rows. Aggregate responses use limit, X-Total-Count and X-Truncated, without Link.

        An explicit date range requires both bounds and date_to >= date_from. These date checks occur in the data layer; failures currently produce HTTP 500 rather than 400. last_n_days and explicit bounds can both restrict the result. Item and collection school filters are independent of the session school assignments.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_id : typing.Optional[str]
            Row view only: optional family UUID. When family_ids is also supplied, the reader first restricts to this family; family_ids cannot widen that scope.

        family_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional family UUIDs; row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_name : typing.Optional[str]
            Case-insensitive family-name substring filter.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        last_n_days : typing.Optional[int]
            Rolling lookback on payment created_at (not transaction_date). Positive values add this filter; zero/negative values do not. May be combined with a transaction-date range.

        state : typing.Optional[str]
            Case-insensitive payment state filter.

        is_posted : typing.Optional[bool]
            Filter by posted state; omit for both states. Accepts true/1 and false/0, case-insensitive.

        successful_only : typing.Optional[bool]
            Include payments that are posted or whose normalized state is success, succeeded, completed, paid, posted, processed, settled or state_success. Only true/1 enables the filter; other values disable it.

        payment_mode : typing.Optional[str]
            Case-insensitive payment mode filter.

        payment_method_sub_kind : typing.Optional[str]
            Case-insensitive payment method subtype filter.

        min_amount : typing.Optional[float]
            Inclusive minimum payment amount.

        max_amount : typing.Optional[float]
            Inclusive maximum payment amount.

        fields : typing.Optional[typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: transaction_date, amount, total_amount, created_at or family_name with _asc/_desc (default transaction_date_desc). Aggregates: group or any supported metric with _asc/_desc. Unrecognized sort keys fall back to the backend default. Aggregate default: count_desc.

        group_by : typing.Optional[GetPaymentsV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]]
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
        GetPaymentsV3Response
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.payments.get_payments_v3(
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
        _response = self._raw_client.get_payments_v3(
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            family_id=family_id,
            family_ids=family_ids,
            family_name=family_name,
            date_from=date_from,
            date_to=date_to,
            last_n_days=last_n_days,
            state=state,
            is_posted=is_posted,
            successful_only=successful_only,
            payment_mode=payment_mode,
            payment_method_sub_kind=payment_method_sub_kind,
            min_amount=min_amount,
            max_amount=max_amount,
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

    def get_payments_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payment:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Only school_id/school_ids and fields affect the item lookup. The shared filter parser still validates supplied family IDs, last_n_days, is_posted and amount bounds, but collection filters do not narrow the item. Returns 404 when no payment matches its ID and school scope.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        fields : typing.Optional[typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.payments.get_payments_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_payments_id_v3(
            id,
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            fields=fields,
            request_options=request_options,
        )
        return _response.data


class AsyncPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentsClient
        """
        return self._raw_client

    async def get_payments_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_id: typing.Optional[str] = None,
        family_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_name: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        state: typing.Optional[str] = None,
        is_posted: typing.Optional[bool] = None,
        successful_only: typing.Optional[bool] = None,
        payment_mode: typing.Optional[str] = None,
        payment_method_sub_kind: typing.Optional[str] = None,
        min_amount: typing.Optional[float] = None,
        max_amount: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[str] = None,
        group_by: typing.Optional[GetPaymentsV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentsV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Without group_by, returns sparse payment rows. With group_by and metrics, returns nested PaymentAggregate rows. school_id and school_ids are both applied when provided (their intersection); omitted school filters read the company scope. Row queries support family_id/family_ids; these IDs do not filter the aggregate representation. fields and pagination apply only to rows. Aggregate responses use limit, X-Total-Count and X-Truncated, without Link.

        An explicit date range requires both bounds and date_to >= date_from. These date checks occur in the data layer; failures currently produce HTTP 500 rather than 400. last_n_days and explicit bounds can both restrict the result. Item and collection school filters are independent of the session school assignments.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_id : typing.Optional[str]
            Row view only: optional family UUID. When family_ids is also supplied, the reader first restricts to this family; family_ids cannot widen that scope.

        family_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional family UUIDs; row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_name : typing.Optional[str]
            Case-insensitive family-name substring filter.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        last_n_days : typing.Optional[int]
            Rolling lookback on payment created_at (not transaction_date). Positive values add this filter; zero/negative values do not. May be combined with a transaction-date range.

        state : typing.Optional[str]
            Case-insensitive payment state filter.

        is_posted : typing.Optional[bool]
            Filter by posted state; omit for both states. Accepts true/1 and false/0, case-insensitive.

        successful_only : typing.Optional[bool]
            Include payments that are posted or whose normalized state is success, succeeded, completed, paid, posted, processed, settled or state_success. Only true/1 enables the filter; other values disable it.

        payment_mode : typing.Optional[str]
            Case-insensitive payment mode filter.

        payment_method_sub_kind : typing.Optional[str]
            Case-insensitive payment method subtype filter.

        min_amount : typing.Optional[float]
            Inclusive minimum payment amount.

        max_amount : typing.Optional[float]
            Inclusive maximum payment amount.

        fields : typing.Optional[typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: transaction_date, amount, total_amount, created_at or family_name with _asc/_desc (default transaction_date_desc). Aggregates: group or any supported metric with _asc/_desc. Unrecognized sort keys fall back to the backend default. Aggregate default: count_desc.

        group_by : typing.Optional[GetPaymentsV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]]
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
        GetPaymentsV3Response
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
            await client.payments.get_payments_v3(
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
        _response = await self._raw_client.get_payments_v3(
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            family_id=family_id,
            family_ids=family_ids,
            family_name=family_name,
            date_from=date_from,
            date_to=date_to,
            last_n_days=last_n_days,
            state=state,
            is_posted=is_posted,
            successful_only=successful_only,
            payment_mode=payment_mode,
            payment_method_sub_kind=payment_method_sub_kind,
            min_amount=min_amount,
            max_amount=max_amount,
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

    async def get_payments_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payment:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Only school_id/school_ids and fields affect the item lookup. The shared filter parser still validates supplied family IDs, last_n_days, is_posted and amount bounds, but collection filters do not narrow the item. Returns 404 when no payment matches its ID and school scope.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        fields : typing.Optional[typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payments.get_payments_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payments_id_v3(
            id,
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            fields=fields,
            request_options=request_options,
        )
        return _response.data
