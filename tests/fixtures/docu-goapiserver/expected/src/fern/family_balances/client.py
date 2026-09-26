

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.family_balance import FamilyBalance
from ..types.family_ledger import FamilyLedger
from .raw_client import AsyncRawFamilyBalancesClient, RawFamilyBalancesClient
from .types.get_family_balances_id_v3request_fields_item import GetFamilyBalancesIdV3RequestFieldsItem
from .types.get_family_balances_v3request_fields_item import GetFamilyBalancesV3RequestFieldsItem
from .types.get_family_balances_v3request_group_by import GetFamilyBalancesV3RequestGroupBy
from .types.get_family_balances_v3request_metrics_item import GetFamilyBalancesV3RequestMetricsItem
from .types.get_family_balances_v3request_view import GetFamilyBalancesV3RequestView
from .types.get_family_balances_v3response import GetFamilyBalancesV3Response


class FamilyBalancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFamilyBalancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFamilyBalancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFamilyBalancesClient
        """
        return self._raw_client

    def get_family_balances_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_name: typing.Optional[str] = None,
        balance_min: typing.Optional[float] = None,
        balance_max: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetFamilyBalancesV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[str] = None,
        view: typing.Optional[GetFamilyBalancesV3RequestView] = None,
        last_n_days: typing.Optional[int] = None,
        group_by: typing.Optional[GetFamilyBalancesV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetFamilyBalancesV3RequestMetricsItem, typing.Sequence[GetFamilyBalancesV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFamilyBalancesV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Default: sparse balance rows, one per family, with optional fields. group_by plus metrics selects nested FamilyBalanceAggregate rows; family_ids does not filter aggregates. school_id and school_ids are both applied when provided (their intersection).

        view=transactions takes precedence and returns FamilyLedger objects (family_id, student_ids, transactions). This view requires school_id assigned to the session. It ignores balance filters, fields, school_ids and grouping after the shared filter parser validates supplied filter values. last_n_days defaults to 30 and is clamped to 0..365. Pagination applies to families, not to transactions inside each family.

        Balance rows use per_page capped at 200; transaction-family pages use 500. Aggregates use limit and X-Truncated without Link.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional family UUIDs; balance row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_name : typing.Optional[str]
            Case-insensitive family-name substring filter; balance rows and aggregates.

        balance_min : typing.Optional[float]
            Inclusive minimum balance; balance rows and aggregates.

        balance_max : typing.Optional[float]
            Inclusive maximum balance; balance rows and aggregates.

        fields : typing.Optional[typing.Union[GetFamilyBalancesV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: family_id, family_name, balance, transaction_date. Balance row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: balance, family_name or transaction_date with _asc/_desc. Aggregates: group or a supported metric with _asc/_desc. Unsupported keys use the backend default. Defaults: balance_desc for rows, count_desc for aggregates.

        view : typing.Optional[GetFamilyBalancesV3RequestView]
            Read per-family transaction ledgers; takes precedence over grouping.

        last_n_days : typing.Optional[int]
            Transactions only: defaults to 30 and clamps to 0 through 365.

        group_by : typing.Optional[GetFamilyBalancesV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetFamilyBalancesV3RequestMetricsItem, typing.Sequence[GetFamilyBalancesV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Balance rows clamp at 200; view=transactions instead clamps at 500.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Balance rows clamp at 200; view=transactions instead clamps at 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFamilyBalancesV3Response
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.family_balances.get_family_balances_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_family_balances_v3(
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            family_ids=family_ids,
            family_name=family_name,
            balance_min=balance_min,
            balance_max=balance_max,
            fields=fields,
            sort_by=sort_by,
            view=view,
            last_n_days=last_n_days,
            group_by=group_by,
            metrics=metrics,
            limit=limit,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    def get_family_balances_id_transactions_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        last_n_days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FamilyLedger]:
        """
        Requires school_id assigned to the session. Returns an unpaginated array of per-family ledger objects, each containing student_ids and transactions; it is not a flat transaction array. The path ID is the family UUID. No matches produce an empty array rather than 404. last_n_days defaults to 30 and is clamped to 0..365.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        last_n_days : typing.Optional[int]
            Lookback in days; default 30, clamped to 0..365.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FamilyLedger]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.family_balances.get_family_balances_id_transactions_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_family_balances_id_transactions_v3(
            id, company_id=company_id, school_id=school_id, last_n_days=last_n_days, request_options=request_options
        )
        return _response.data

    def get_family_balances_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[
            typing.Union[
                GetFamilyBalancesIdV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesIdV3RequestFieldsItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FamilyBalance:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The path ID is the family UUID. school_id/school_ids narrow the lookup and fields selects the response properties. Other collection filters do not apply, although the shared parser still validates supplied family_ids and balance bounds. No matching family balance returns 404.

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

        fields : typing.Optional[typing.Union[GetFamilyBalancesIdV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: family_id, family_name, balance, transaction_date.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FamilyBalance
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.family_balances.get_family_balances_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_family_balances_id_v3(
            id,
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            fields=fields,
            request_options=request_options,
        )
        return _response.data


class AsyncFamilyBalancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFamilyBalancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFamilyBalancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFamilyBalancesClient
        """
        return self._raw_client

    async def get_family_balances_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_name: typing.Optional[str] = None,
        balance_min: typing.Optional[float] = None,
        balance_max: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetFamilyBalancesV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[str] = None,
        view: typing.Optional[GetFamilyBalancesV3RequestView] = None,
        last_n_days: typing.Optional[int] = None,
        group_by: typing.Optional[GetFamilyBalancesV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetFamilyBalancesV3RequestMetricsItem, typing.Sequence[GetFamilyBalancesV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFamilyBalancesV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Default: sparse balance rows, one per family, with optional fields. group_by plus metrics selects nested FamilyBalanceAggregate rows; family_ids does not filter aggregates. school_id and school_ids are both applied when provided (their intersection).

        view=transactions takes precedence and returns FamilyLedger objects (family_id, student_ids, transactions). This view requires school_id assigned to the session. It ignores balance filters, fields, school_ids and grouping after the shared filter parser validates supplied filter values. last_n_days defaults to 30 and is clamped to 0..365. Pagination applies to families, not to transactions inside each family.

        Balance rows use per_page capped at 200; transaction-family pages use 500. Aggregates use limit and X-Truncated without Link.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional family UUIDs; balance row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_name : typing.Optional[str]
            Case-insensitive family-name substring filter; balance rows and aggregates.

        balance_min : typing.Optional[float]
            Inclusive minimum balance; balance rows and aggregates.

        balance_max : typing.Optional[float]
            Inclusive maximum balance; balance rows and aggregates.

        fields : typing.Optional[typing.Union[GetFamilyBalancesV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: family_id, family_name, balance, transaction_date. Balance row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: balance, family_name or transaction_date with _asc/_desc. Aggregates: group or a supported metric with _asc/_desc. Unsupported keys use the backend default. Defaults: balance_desc for rows, count_desc for aggregates.

        view : typing.Optional[GetFamilyBalancesV3RequestView]
            Read per-family transaction ledgers; takes precedence over grouping.

        last_n_days : typing.Optional[int]
            Transactions only: defaults to 30 and clamps to 0 through 365.

        group_by : typing.Optional[GetFamilyBalancesV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetFamilyBalancesV3RequestMetricsItem, typing.Sequence[GetFamilyBalancesV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Balance rows clamp at 200; view=transactions instead clamps at 500.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Balance rows clamp at 200; view=transactions instead clamps at 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFamilyBalancesV3Response
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.family_balances.get_family_balances_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_family_balances_v3(
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            family_ids=family_ids,
            family_name=family_name,
            balance_min=balance_min,
            balance_max=balance_max,
            fields=fields,
            sort_by=sort_by,
            view=view,
            last_n_days=last_n_days,
            group_by=group_by,
            metrics=metrics,
            limit=limit,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    async def get_family_balances_id_transactions_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        last_n_days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FamilyLedger]:
        """
        Requires school_id assigned to the session. Returns an unpaginated array of per-family ledger objects, each containing student_ids and transactions; it is not a flat transaction array. The path ID is the family UUID. No matches produce an empty array rather than 404. last_n_days defaults to 30 and is clamped to 0..365.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        last_n_days : typing.Optional[int]
            Lookback in days; default 30, clamped to 0..365.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FamilyLedger]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.family_balances.get_family_balances_id_transactions_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_family_balances_id_transactions_v3(
            id, company_id=company_id, school_id=school_id, last_n_days=last_n_days, request_options=request_options
        )
        return _response.data

    async def get_family_balances_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[
            typing.Union[
                GetFamilyBalancesIdV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesIdV3RequestFieldsItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FamilyBalance:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The path ID is the family UUID. school_id/school_ids narrow the lookup and fields selects the response properties. Other collection filters do not apply, although the shared parser still validates supplied family_ids and balance bounds. No matching family balance returns 404.

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

        fields : typing.Optional[typing.Union[GetFamilyBalancesIdV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: family_id, family_name, balance, transaction_date.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FamilyBalance
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.family_balances.get_family_balances_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_family_balances_id_v3(
            id,
            company_id=company_id,
            school_id=school_id,
            school_ids=school_ids,
            fields=fields,
            request_options=request_options,
        )
        return _response.data
