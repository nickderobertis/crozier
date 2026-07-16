

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_customer_segments_response import ListCustomerSegmentsResponse
from ..types.retrieve_customer_segment_response import RetrieveCustomerSegmentResponse
from .raw_client import AsyncRawCustomerSegmentsClient, RawCustomerSegmentsClient


class CustomerSegmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomerSegmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomerSegmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomerSegmentsClient
        """
        return self._raw_client

    def list_customer_segments(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomerSegmentsResponse:
        """
        Retrieves the list of customer segments of a business.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by previous calls to `ListCustomerSegments`.
            This cursor is used to retrieve the next set of query results.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomerSegmentsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customer_segments.list_customer_segments()
        """
        _response = self._raw_client.list_customer_segments(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    def retrieve_customer_segment(
        self, segment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCustomerSegmentResponse:
        """
        Retrieves a specific customer segment as identified by the `segment_id` value.

        Parameters
        ----------
        segment_id : str
            The Square-issued ID of the customer segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCustomerSegmentResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customer_segments.retrieve_customer_segment(
            segment_id="segment_id",
        )
        """
        _response = self._raw_client.retrieve_customer_segment(segment_id, request_options=request_options)
        return _response.data


class AsyncCustomerSegmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomerSegmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomerSegmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomerSegmentsClient
        """
        return self._raw_client

    async def list_customer_segments(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomerSegmentsResponse:
        """
        Retrieves the list of customer segments of a business.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by previous calls to `ListCustomerSegments`.
            This cursor is used to retrieve the next set of query results.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomerSegmentsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_segments.list_customer_segments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customer_segments(
            cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def retrieve_customer_segment(
        self, segment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCustomerSegmentResponse:
        """
        Retrieves a specific customer segment as identified by the `segment_id` value.

        Parameters
        ----------
        segment_id : str
            The Square-issued ID of the customer segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCustomerSegmentResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_segments.retrieve_customer_segment(
                segment_id="segment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_customer_segment(segment_id, request_options=request_options)
        return _response.data
