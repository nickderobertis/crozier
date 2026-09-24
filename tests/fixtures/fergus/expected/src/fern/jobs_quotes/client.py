

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accept_quote_response import AcceptQuoteResponse
from ..types.get_quote_by_id_quote_response import GetQuoteByIdQuoteResponse
from ..types.get_standalone_quotes_response import GetStandaloneQuotesResponse
from ..types.quote_totals_response import QuoteTotalsResponse
from .raw_client import AsyncRawJobsQuotesClient, RawJobsQuotesClient
from .types.get_jobs_quotes_request_filter_status import GetJobsQuotesRequestFilterStatus
from .types.get_jobs_quotes_request_sort_field import GetJobsQuotesRequestSortField
from .types.get_jobs_quotes_request_sort_order import GetJobsQuotesRequestSortOrder


OMIT = typing.cast(typing.Any, ...)


class JobsQuotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsQuotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsQuotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsQuotesClient
        """
        return self._raw_client

    def get_jobs_quotes(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_status: typing.Optional[GetJobsQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsQuotesRequestSortField] = None,
        created_after: typing.Optional[dt.datetime] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStandaloneQuotesResponse:
        """
        Returns a list of all quotes from across all jobs, sorted by created date and last modified date.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_status : typing.Optional[GetJobsQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsQuotesRequestSortField]

        created_after : typing.Optional[dt.datetime]
            Get quote created after certain time. Overrides sortField and sortOrder

        modified_after : typing.Optional[dt.datetime]
            Get quote modified after certain time. Overrides sortField and sortOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStandaloneQuotesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.get_jobs_quotes()
        """
        _response = self._raw_client.get_jobs_quotes(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_status=filter_status,
            sort_field=sort_field,
            created_after=created_after,
            modified_after=modified_after,
            request_options=request_options,
        )
        return _response.data

    def get_jobs_quotes_quote_id(
        self, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetQuoteByIdQuoteResponse:
        """
        Returns a specific quote by ID from across all jobs.

        Parameters
        ----------
        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuoteByIdQuoteResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.get_jobs_quotes_quote_id(
            quote_id=1.1,
        )
        """
        _response = self._raw_client.get_jobs_quotes_quote_id(quote_id, request_options=request_options)
        return _response.data

    def get_jobs_quotes_guid_guid(
        self,
        guid: str,
        *,
        include_combined_item_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetQuoteByIdQuoteResponse:
        """
        Returns a specific quote by GUID with full details.

        Parameters
        ----------
        guid : str

        include_combined_item_parents : typing.Optional[bool]
            Include the parents of combined line item in the `lineItems` list (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuoteByIdQuoteResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.get_jobs_quotes_guid_guid(
            guid="guid",
        )
        """
        _response = self._raw_client.get_jobs_quotes_guid_guid(
            guid, include_combined_item_parents=include_combined_item_parents, request_options=request_options
        )
        return _response.data

    def post_jobs_quotes_quote_id_publish(
        self,
        quote_id: str,
        *,
        published_at: typing.Optional[dt.datetime] = OMIT,
        published_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Publishes a quote.

        Parameters
        ----------
        quote_id : str

        published_at : typing.Optional[dt.datetime]

        published_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.post_jobs_quotes_quote_id_publish(
            quote_id="quoteId",
        )
        """
        _response = self._raw_client.post_jobs_quotes_quote_id_publish(
            quote_id, published_at=published_at, published_by=published_by, request_options=request_options
        )
        return _response.data

    def post_jobs_quotes_quote_id_mark_as_sent(
        self,
        quote_id: str,
        *,
        is_sent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Marks a quote as sent.

        Parameters
        ----------
        quote_id : str

        is_sent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.post_jobs_quotes_quote_id_mark_as_sent(
            quote_id="quoteId",
        )
        """
        _response = self._raw_client.post_jobs_quotes_quote_id_mark_as_sent(
            quote_id, is_sent=is_sent, request_options=request_options
        )
        return _response.data

    def post_jobs_quotes_quote_id_accept(
        self,
        quote_id: str,
        *,
        accepted_by: str,
        accepted_at: typing.Optional[dt.datetime] = OMIT,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[AcceptQuoteResponse]:
        """
        Accepts a quote.

        Parameters
        ----------
        quote_id : str

        accepted_by : str
            The name or employee GUID of the person accepting the quote

        accepted_at : typing.Optional[dt.datetime]

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            The IDs of the sections that the customer has accepted. Required if the quote has optional or multi-select sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AcceptQuoteResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.post_jobs_quotes_quote_id_accept(
            quote_id="quoteId",
            accepted_by="acceptedBy",
        )
        """
        _response = self._raw_client.post_jobs_quotes_quote_id_accept(
            quote_id,
            accepted_by=accepted_by,
            accepted_at=accepted_at,
            selected_section_ids=selected_section_ids,
            request_options=request_options,
        )
        return _response.data

    def post_jobs_quotes_quote_id_decline(
        self,
        quote_id: str,
        *,
        declined_at: typing.Optional[dt.datetime] = OMIT,
        reason_notes: typing.Optional[str] = OMIT,
        rejected_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Declines a quote.

        Parameters
        ----------
        quote_id : str

        declined_at : typing.Optional[dt.datetime]

        reason_notes : typing.Optional[str]

        rejected_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.post_jobs_quotes_quote_id_decline(
            quote_id="quoteId",
        )
        """
        _response = self._raw_client.post_jobs_quotes_quote_id_decline(
            quote_id,
            declined_at=declined_at,
            reason_notes=reason_notes,
            rejected_by=rejected_by,
            request_options=request_options,
        )
        return _response.data

    def post_jobs_quotes_quote_id_void(
        self,
        quote_id: str,
        *,
        voided_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Voids a quote.

        Parameters
        ----------
        quote_id : str

        voided_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.post_jobs_quotes_quote_id_void(
            quote_id="quoteId",
        )
        """
        _response = self._raw_client.post_jobs_quotes_quote_id_void(
            quote_id, voided_at=voided_at, request_options=request_options
        )
        return _response.data

    def post_jobs_quotes_quote_id_totals(
        self,
        quote_id: float,
        *,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuoteTotalsResponse:
        """
        Get totals for a quote. Fixed sections are always included. Optionally provide optional/multiselect section IDs to include in the totals.

        Parameters
        ----------
        quote_id : float

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            [] — returns totals for fixed sections only. [1, 2, 3] — returns totals for fixed sections + the provided optional/multiselect section IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuoteTotalsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_quotes.post_jobs_quotes_quote_id_totals(
            quote_id=1.1,
        )
        """
        _response = self._raw_client.post_jobs_quotes_quote_id_totals(
            quote_id, selected_section_ids=selected_section_ids, request_options=request_options
        )
        return _response.data


class AsyncJobsQuotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsQuotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsQuotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsQuotesClient
        """
        return self._raw_client

    async def get_jobs_quotes(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_status: typing.Optional[GetJobsQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsQuotesRequestSortField] = None,
        created_after: typing.Optional[dt.datetime] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStandaloneQuotesResponse:
        """
        Returns a list of all quotes from across all jobs, sorted by created date and last modified date.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_status : typing.Optional[GetJobsQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsQuotesRequestSortField]

        created_after : typing.Optional[dt.datetime]
            Get quote created after certain time. Overrides sortField and sortOrder

        modified_after : typing.Optional[dt.datetime]
            Get quote modified after certain time. Overrides sortField and sortOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStandaloneQuotesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.get_jobs_quotes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_quotes(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_status=filter_status,
            sort_field=sort_field,
            created_after=created_after,
            modified_after=modified_after,
            request_options=request_options,
        )
        return _response.data

    async def get_jobs_quotes_quote_id(
        self, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetQuoteByIdQuoteResponse:
        """
        Returns a specific quote by ID from across all jobs.

        Parameters
        ----------
        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuoteByIdQuoteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.get_jobs_quotes_quote_id(
                quote_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_quotes_quote_id(quote_id, request_options=request_options)
        return _response.data

    async def get_jobs_quotes_guid_guid(
        self,
        guid: str,
        *,
        include_combined_item_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetQuoteByIdQuoteResponse:
        """
        Returns a specific quote by GUID with full details.

        Parameters
        ----------
        guid : str

        include_combined_item_parents : typing.Optional[bool]
            Include the parents of combined line item in the `lineItems` list (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuoteByIdQuoteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.get_jobs_quotes_guid_guid(
                guid="guid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_quotes_guid_guid(
            guid, include_combined_item_parents=include_combined_item_parents, request_options=request_options
        )
        return _response.data

    async def post_jobs_quotes_quote_id_publish(
        self,
        quote_id: str,
        *,
        published_at: typing.Optional[dt.datetime] = OMIT,
        published_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Publishes a quote.

        Parameters
        ----------
        quote_id : str

        published_at : typing.Optional[dt.datetime]

        published_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.post_jobs_quotes_quote_id_publish(
                quote_id="quoteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_quotes_quote_id_publish(
            quote_id, published_at=published_at, published_by=published_by, request_options=request_options
        )
        return _response.data

    async def post_jobs_quotes_quote_id_mark_as_sent(
        self,
        quote_id: str,
        *,
        is_sent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Marks a quote as sent.

        Parameters
        ----------
        quote_id : str

        is_sent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.post_jobs_quotes_quote_id_mark_as_sent(
                quote_id="quoteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_quotes_quote_id_mark_as_sent(
            quote_id, is_sent=is_sent, request_options=request_options
        )
        return _response.data

    async def post_jobs_quotes_quote_id_accept(
        self,
        quote_id: str,
        *,
        accepted_by: str,
        accepted_at: typing.Optional[dt.datetime] = OMIT,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[AcceptQuoteResponse]:
        """
        Accepts a quote.

        Parameters
        ----------
        quote_id : str

        accepted_by : str
            The name or employee GUID of the person accepting the quote

        accepted_at : typing.Optional[dt.datetime]

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            The IDs of the sections that the customer has accepted. Required if the quote has optional or multi-select sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AcceptQuoteResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.post_jobs_quotes_quote_id_accept(
                quote_id="quoteId",
                accepted_by="acceptedBy",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_quotes_quote_id_accept(
            quote_id,
            accepted_by=accepted_by,
            accepted_at=accepted_at,
            selected_section_ids=selected_section_ids,
            request_options=request_options,
        )
        return _response.data

    async def post_jobs_quotes_quote_id_decline(
        self,
        quote_id: str,
        *,
        declined_at: typing.Optional[dt.datetime] = OMIT,
        reason_notes: typing.Optional[str] = OMIT,
        rejected_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Declines a quote.

        Parameters
        ----------
        quote_id : str

        declined_at : typing.Optional[dt.datetime]

        reason_notes : typing.Optional[str]

        rejected_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.post_jobs_quotes_quote_id_decline(
                quote_id="quoteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_quotes_quote_id_decline(
            quote_id,
            declined_at=declined_at,
            reason_notes=reason_notes,
            rejected_by=rejected_by,
            request_options=request_options,
        )
        return _response.data

    async def post_jobs_quotes_quote_id_void(
        self,
        quote_id: str,
        *,
        voided_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Voids a quote.

        Parameters
        ----------
        quote_id : str

        voided_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.post_jobs_quotes_quote_id_void(
                quote_id="quoteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_quotes_quote_id_void(
            quote_id, voided_at=voided_at, request_options=request_options
        )
        return _response.data

    async def post_jobs_quotes_quote_id_totals(
        self,
        quote_id: float,
        *,
        selected_section_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuoteTotalsResponse:
        """
        Get totals for a quote. Fixed sections are always included. Optionally provide optional/multiselect section IDs to include in the totals.

        Parameters
        ----------
        quote_id : float

        selected_section_ids : typing.Optional[typing.Sequence[int]]
            [] — returns totals for fixed sections only. [1, 2, 3] — returns totals for fixed sections + the provided optional/multiselect section IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuoteTotalsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_quotes.post_jobs_quotes_quote_id_totals(
                quote_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_quotes_quote_id_totals(
            quote_id, selected_section_ids=selected_section_ids, request_options=request_options
        )
        return _response.data
