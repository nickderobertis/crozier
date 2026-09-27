

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_lead_stages_item import BulkLeadStagesItem
from ..types.intended_start_date_update import IntendedStartDateUpdate
from ..types.lead_stage import LeadStage
from ..types.lead_stages import LeadStages
from ..types.update_intended_start_dates_response import UpdateIntendedStartDatesResponse
from ..types.update_lead_stages_request import UpdateLeadStagesRequest
from .raw_client import AsyncRawLeadsClient, RawLeadsClient
from .types.get_leads_id_v3request_fields_item import GetLeadsIdV3RequestFieldsItem
from .types.get_leads_id_v3response import GetLeadsIdV3Response
from .types.get_leads_v3request_fields_item import GetLeadsV3RequestFieldsItem
from .types.get_leads_v3request_status import GetLeadsV3RequestStatus
from .types.get_leads_v3request_view import GetLeadsV3RequestView
from .types.get_leads_v3response import GetLeadsV3Response


OMIT = typing.cast(typing.Any, ...)


class LeadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLeadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLeadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLeadsClient
        """
        return self._raw_client

    def get_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetLeadsV3RequestView] = None,
        fields: typing.Optional[
            typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]
        ] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        query: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[GetLeadsV3RequestStatus] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        age_min: typing.Optional[float] = None,
        age_max: typing.Optional[float] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLeadsV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns paginated lead rows, or paginated LeadStages objects when view=stages.

        Normal lookup precedence is ids, then query, then the filtered school collection. ids is limited to 200 UUIDs and missing IDs are omitted. query performs a name search with optional max_results. status, date_from/date_to and age_min/age_max are validated before these branches but only filter the normal school collection; ids and query bypass those filters. Negative ages are accepted for expected children. The age interval defaults to -12 through 180 months. date_to cannot precede date_from, and age_max cannot be smaller than age_min.

        view=stages requires the school in the session assignments and accepts only company_id, school_id, view, page and per_page. Any other parameter in this view returns 400.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetLeadsV3RequestView]
            Omit for lead rows; stages includes per-stage timestamps.

        fields : typing.Optional[typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Normal lead representation only; names are case-sensitive. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Read at most 200 lead UUIDs; takes precedence over query. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        query : typing.Optional[str]
            Name search; used only when ids is omitted.

        max_results : typing.Optional[int]
            Maximum name-search results; 0 keeps the backend default.

        status : typing.Optional[GetLeadsV3RequestStatus]
            Procare lead status; exact case required. Applies only to normal school collection.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        age_min : typing.Optional[float]
            Minimum child age in months; normal school collection only.

        age_max : typing.Optional[float]
            Maximum child age in months; normal school collection only.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLeadsV3Response
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leads.get_leads_v3(
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
        _response = self._raw_client.get_leads_v3(
            company_id=company_id,
            school_id=school_id,
            view=view,
            fields=fields,
            ids=ids,
            query=query,
            max_results=max_results,
            status=status,
            date_from=date_from,
            date_to=date_to,
            age_min=age_min,
            age_max=age_max,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    def patch_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        request: typing.Sequence[BulkLeadStagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LeadStages]:
        """
        Requires school_id assigned to the session. The body is an array of 1 to 200 items, each with lead_id and at least one non-null stage. All items are validated before writes. Missing leads are omitted from the response. Repeated lead IDs are allowed; each appears once in the response in first-occurrence order with its final stages. The batch is not atomic: a database failure returns 500 and stops processing after any earlier writes.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : typing.Sequence[BulkLeadStagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LeadStages]
            Successful response.

        Examples
        --------
        from fern import (
            BulkLeadStagesItem,
            FernApi,
            UpdateLeadStagesRequestStageTourCompleted,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leads.patch_leads_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
            request=[
                BulkLeadStagesItem(
                    lead_id="44444444-4444-4444-8444-444444444444",
                    stages=UpdateLeadStagesRequestStageTourCompleted(
                        stage_tour_completed=True,
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.patch_leads_v3(
            company_id=company_id, school_id=school_id, request=request, request_options=request_options
        )
        return _response.data

    def get_leads_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLeadsIdV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. fields selects properties from the lead projection; unknown fields return 400. Returns 404 when the scoped lead does not exist.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLeadsIdV3Response
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leads.get_leads_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_leads_id_v3(
            id, company_id=company_id, school_id=school_id, fields=fields, request_options=request_options
        )
        return _response.data

    def get_leads_id_stages_v3(
        self, id: str, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LeadStage]:
        """
        Requires school_id assigned to the session. Each stage includes its own state and timestamp. The company lead-stages setting selects the underlying stage source for both reading and writing; it is not a read-only permission.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LeadStage]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leads.get_leads_id_stages_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_leads_id_stages_v3(
            id, company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data

    def patch_leads_id_stages_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateLeadStagesRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LeadStage]:
        """
        Requires school_id assigned to the session and at least one non-null boolean stage. Unknown properties return 400. Stages are written in the documented schema order. Each stage is a separate write: a later failure returns 404/500 and earlier stages may remain applied; an error response does not include a partial stage list. On success the current stages are read back.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateLeadStagesRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LeadStage]
            Successful response.

        Examples
        --------
        from fern import FernApi, UpdateLeadStagesRequestStageTourCompleted

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leads.patch_leads_id_stages_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
            request=UpdateLeadStagesRequestStageTourCompleted(
                stage_tour_completed=True,
            ),
        )
        """
        _response = self._raw_client.patch_leads_id_stages_v3(
            id, company_id=company_id, school_id=school_id, request=request, request_options=request_options
        )
        return _response.data

    def patch_leads_intended_start_date_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        updates: typing.Sequence[IntendedStartDateUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateIntendedStartDatesResponse:
        """
        Requires school_id assigned to the session. At most 200 lead IDs are accepted across all update groups, and duplicates anywhere in the request return 400. Dates must be future YYYY-MM-DD values or TBD. Leads with a CRM/Procare expected start date are not overwritten and are reported in lead_ids_not_updated. Missing lead IDs and leads without raw records are omitted. Per-lead write failures are reported with HTTP 200 in lead_ids_not_updated; a group lookup failure returns 500 after any earlier groups may have been applied.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        updates : typing.Sequence[IntendedStartDateUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateIntendedStartDatesResponse
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi, IntendedStartDateUpdate

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.leads.patch_leads_intended_start_date_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
            updates=[
                IntendedStartDateUpdate(
                    lead_ids=["44444444-4444-4444-8444-444444444444"],
                    intended_start_date=datetime.date.fromisoformat(
                        "2030-09-01",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.patch_leads_intended_start_date_v3(
            company_id=company_id, school_id=school_id, updates=updates, request_options=request_options
        )
        return _response.data


class AsyncLeadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLeadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLeadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLeadsClient
        """
        return self._raw_client

    async def get_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetLeadsV3RequestView] = None,
        fields: typing.Optional[
            typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]
        ] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        query: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[GetLeadsV3RequestStatus] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        age_min: typing.Optional[float] = None,
        age_max: typing.Optional[float] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLeadsV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns paginated lead rows, or paginated LeadStages objects when view=stages.

        Normal lookup precedence is ids, then query, then the filtered school collection. ids is limited to 200 UUIDs and missing IDs are omitted. query performs a name search with optional max_results. status, date_from/date_to and age_min/age_max are validated before these branches but only filter the normal school collection; ids and query bypass those filters. Negative ages are accepted for expected children. The age interval defaults to -12 through 180 months. date_to cannot precede date_from, and age_max cannot be smaller than age_min.

        view=stages requires the school in the session assignments and accepts only company_id, school_id, view, page and per_page. Any other parameter in this view returns 400.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetLeadsV3RequestView]
            Omit for lead rows; stages includes per-stage timestamps.

        fields : typing.Optional[typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Normal lead representation only; names are case-sensitive. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Read at most 200 lead UUIDs; takes precedence over query. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        query : typing.Optional[str]
            Name search; used only when ids is omitted.

        max_results : typing.Optional[int]
            Maximum name-search results; 0 keeps the backend default.

        status : typing.Optional[GetLeadsV3RequestStatus]
            Procare lead status; exact case required. Applies only to normal school collection.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional created-date window for the normal school collection.

        age_min : typing.Optional[float]
            Minimum child age in months; normal school collection only.

        age_max : typing.Optional[float]
            Maximum child age in months; normal school collection only.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLeadsV3Response
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
            await client.leads.get_leads_v3(
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
        _response = await self._raw_client.get_leads_v3(
            company_id=company_id,
            school_id=school_id,
            view=view,
            fields=fields,
            ids=ids,
            query=query,
            max_results=max_results,
            status=status,
            date_from=date_from,
            date_to=date_to,
            age_min=age_min,
            age_max=age_max,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    async def patch_leads_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        request: typing.Sequence[BulkLeadStagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LeadStages]:
        """
        Requires school_id assigned to the session. The body is an array of 1 to 200 items, each with lead_id and at least one non-null stage. All items are validated before writes. Missing leads are omitted from the response. Repeated lead IDs are allowed; each appears once in the response in first-occurrence order with its final stages. The batch is not atomic: a database failure returns 500 and stops processing after any earlier writes.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : typing.Sequence[BulkLeadStagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LeadStages]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BulkLeadStagesItem,
            UpdateLeadStagesRequestStageTourCompleted,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.leads.patch_leads_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
                request=[
                    BulkLeadStagesItem(
                        lead_id="44444444-4444-4444-8444-444444444444",
                        stages=UpdateLeadStagesRequestStageTourCompleted(
                            stage_tour_completed=True,
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_leads_v3(
            company_id=company_id, school_id=school_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_leads_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLeadsIdV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. fields selects properties from the lead projection; unknown fields return 400. Returns 404 when the scoped lead does not exist.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLeadsIdV3Response
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.leads.get_leads_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_leads_id_v3(
            id, company_id=company_id, school_id=school_id, fields=fields, request_options=request_options
        )
        return _response.data

    async def get_leads_id_stages_v3(
        self, id: str, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LeadStage]:
        """
        Requires school_id assigned to the session. Each stage includes its own state and timestamp. The company lead-stages setting selects the underlying stage source for both reading and writing; it is not a read-only permission.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LeadStage]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.leads.get_leads_id_stages_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_leads_id_stages_v3(
            id, company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data

    async def patch_leads_id_stages_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateLeadStagesRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LeadStage]:
        """
        Requires school_id assigned to the session and at least one non-null boolean stage. Unknown properties return 400. Stages are written in the documented schema order. Each stage is a separate write: a later failure returns 404/500 and earlier stages may remain applied; an error response does not include a partial stage list. On success the current stages are read back.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateLeadStagesRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LeadStage]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateLeadStagesRequestStageTourCompleted

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.leads.patch_leads_id_stages_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
                request=UpdateLeadStagesRequestStageTourCompleted(
                    stage_tour_completed=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_leads_id_stages_v3(
            id, company_id=company_id, school_id=school_id, request=request, request_options=request_options
        )
        return _response.data

    async def patch_leads_intended_start_date_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        updates: typing.Sequence[IntendedStartDateUpdate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateIntendedStartDatesResponse:
        """
        Requires school_id assigned to the session. At most 200 lead IDs are accepted across all update groups, and duplicates anywhere in the request return 400. Dates must be future YYYY-MM-DD values or TBD. Leads with a CRM/Procare expected start date are not overwritten and are reported in lead_ids_not_updated. Missing lead IDs and leads without raw records are omitted. Per-lead write failures are reported with HTTP 200 in lead_ids_not_updated; a group lookup failure returns 500 after any earlier groups may have been applied.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        updates : typing.Sequence[IntendedStartDateUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateIntendedStartDatesResponse
            Successful response.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, IntendedStartDateUpdate

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.leads.patch_leads_intended_start_date_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
                updates=[
                    IntendedStartDateUpdate(
                        lead_ids=["44444444-4444-4444-8444-444444444444"],
                        intended_start_date=datetime.date.fromisoformat(
                            "2030-09-01",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_leads_intended_start_date_v3(
            company_id=company_id, school_id=school_id, updates=updates, request_options=request_options
        )
        return _response.data
