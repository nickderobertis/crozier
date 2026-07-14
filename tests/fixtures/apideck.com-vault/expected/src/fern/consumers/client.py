

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.consumer_connection import ConsumerConnection
from ..types.consumer_id import ConsumerId
from ..types.consumer_metadata import ConsumerMetadata
from ..types.consumer_request_counts_in_date_range_response import ConsumerRequestCountsInDateRangeResponse
from ..types.create_consumer_response import CreateConsumerResponse
from ..types.delete_consumer_response import DeleteConsumerResponse
from ..types.get_consumer_response import GetConsumerResponse
from ..types.get_consumers_response import GetConsumersResponse
from ..types.request_count_allocation import RequestCountAllocation
from ..types.update_consumer_response import UpdateConsumerResponse
from .raw_client import AsyncRawConsumersClient, RawConsumersClient


OMIT = typing.cast(typing.Any, ...)


class ConsumersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConsumersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConsumersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConsumersClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConsumersResponse:
        """
        This endpoint includes all application consumers, along with an aggregated count of requests made.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConsumersResponse
            Consumers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.consumers.all_()
        """
        _response = self._raw_client.all_(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    def add(
        self,
        *,
        consumer_id: ConsumerId,
        aggregated_request_count: typing.Optional[float] = OMIT,
        application_id: typing.Optional[str] = OMIT,
        connections: typing.Optional[typing.Sequence[ConsumerConnection]] = OMIT,
        created: typing.Optional[str] = OMIT,
        metadata: typing.Optional[ConsumerMetadata] = OMIT,
        modified: typing.Optional[str] = OMIT,
        request_count_updated: typing.Optional[str] = OMIT,
        request_counts: typing.Optional[RequestCountAllocation] = OMIT,
        services: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConsumerResponse:
        """
        Create a consumer

        Parameters
        ----------
        consumer_id : ConsumerId

        aggregated_request_count : typing.Optional[float]

        application_id : typing.Optional[str]
            ID of your Apideck Application

        connections : typing.Optional[typing.Sequence[ConsumerConnection]]

        created : typing.Optional[str]

        metadata : typing.Optional[ConsumerMetadata]

        modified : typing.Optional[str]

        request_count_updated : typing.Optional[str]

        request_counts : typing.Optional[RequestCountAllocation]

        services : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConsumerResponse
            Consumer created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.consumers.add(
            consumer_id="test_consumer_id",
        )
        """
        _response = self._raw_client.add(
            consumer_id=consumer_id,
            aggregated_request_count=aggregated_request_count,
            application_id=application_id,
            connections=connections,
            created=created,
            metadata=metadata,
            modified=modified,
            request_count_updated=request_count_updated,
            request_counts=request_counts,
            services=services,
            request_options=request_options,
        )
        return _response.data

    def one(self, consumer_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetConsumerResponse:
        """
        Consumer detail including their aggregated counts with the connections they have authorized.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConsumerResponse
            Consumer

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.consumers.one(
            consumer_id="test_user_id",
        )
        """
        _response = self._raw_client.one(consumer_id, request_options=request_options)
        return _response.data

    def delete(
        self, consumer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteConsumerResponse:
        """
        Delete consumer and all their connections, including credentials.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteConsumerResponse
            Consumer deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.consumers.delete(
            consumer_id="test_user_id",
        )
        """
        _response = self._raw_client.delete(consumer_id, request_options=request_options)
        return _response.data

    def update(
        self,
        consumer_id: str,
        *,
        metadata: typing.Optional[ConsumerMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateConsumerResponse:
        """
        Update consumer metadata such as name and email.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        metadata : typing.Optional[ConsumerMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateConsumerResponse
            Consumer updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.consumers.update(
            consumer_id="test_user_id",
        )
        """
        _response = self._raw_client.update(consumer_id, metadata=metadata, request_options=request_options)
        return _response.data

    def consumer_request_counts_all(
        self,
        consumer_id: str,
        *,
        start_datetime: str,
        end_datetime: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsumerRequestCountsInDateRangeResponse:
        """
        Get consumer request counts within a given datetime range.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        start_datetime : str
            Scopes results to requests that happened after datetime

        end_datetime : str
            Scopes results to requests that happened before datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsumerRequestCountsInDateRangeResponse
            Consumers Request Counts within Date Range

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.consumers.consumer_request_counts_all(
            consumer_id="test_user_id",
            start_datetime="2021-05-01T12:00:00.000Z",
            end_datetime="2021-05-30T12:00:00.000Z",
        )
        """
        _response = self._raw_client.consumer_request_counts_all(
            consumer_id, start_datetime=start_datetime, end_datetime=end_datetime, request_options=request_options
        )
        return _response.data


class AsyncConsumersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConsumersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConsumersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConsumersClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConsumersResponse:
        """
        This endpoint includes all application consumers, along with an aggregated count of requests made.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConsumersResponse
            Consumers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumers.all_()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    async def add(
        self,
        *,
        consumer_id: ConsumerId,
        aggregated_request_count: typing.Optional[float] = OMIT,
        application_id: typing.Optional[str] = OMIT,
        connections: typing.Optional[typing.Sequence[ConsumerConnection]] = OMIT,
        created: typing.Optional[str] = OMIT,
        metadata: typing.Optional[ConsumerMetadata] = OMIT,
        modified: typing.Optional[str] = OMIT,
        request_count_updated: typing.Optional[str] = OMIT,
        request_counts: typing.Optional[RequestCountAllocation] = OMIT,
        services: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConsumerResponse:
        """
        Create a consumer

        Parameters
        ----------
        consumer_id : ConsumerId

        aggregated_request_count : typing.Optional[float]

        application_id : typing.Optional[str]
            ID of your Apideck Application

        connections : typing.Optional[typing.Sequence[ConsumerConnection]]

        created : typing.Optional[str]

        metadata : typing.Optional[ConsumerMetadata]

        modified : typing.Optional[str]

        request_count_updated : typing.Optional[str]

        request_counts : typing.Optional[RequestCountAllocation]

        services : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConsumerResponse
            Consumer created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumers.add(
                consumer_id="test_consumer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            consumer_id=consumer_id,
            aggregated_request_count=aggregated_request_count,
            application_id=application_id,
            connections=connections,
            created=created,
            metadata=metadata,
            modified=modified,
            request_count_updated=request_count_updated,
            request_counts=request_counts,
            services=services,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self, consumer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConsumerResponse:
        """
        Consumer detail including their aggregated counts with the connections they have authorized.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConsumerResponse
            Consumer

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumers.one(
                consumer_id="test_user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(consumer_id, request_options=request_options)
        return _response.data

    async def delete(
        self, consumer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteConsumerResponse:
        """
        Delete consumer and all their connections, including credentials.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteConsumerResponse
            Consumer deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumers.delete(
                consumer_id="test_user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(consumer_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        consumer_id: str,
        *,
        metadata: typing.Optional[ConsumerMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateConsumerResponse:
        """
        Update consumer metadata such as name and email.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        metadata : typing.Optional[ConsumerMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateConsumerResponse
            Consumer updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumers.update(
                consumer_id="test_user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(consumer_id, metadata=metadata, request_options=request_options)
        return _response.data

    async def consumer_request_counts_all(
        self,
        consumer_id: str,
        *,
        start_datetime: str,
        end_datetime: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsumerRequestCountsInDateRangeResponse:
        """
        Get consumer request counts within a given datetime range.

        Parameters
        ----------
        consumer_id : str
            ID of the consumer to return

        start_datetime : str
            Scopes results to requests that happened after datetime

        end_datetime : str
            Scopes results to requests that happened before datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsumerRequestCountsInDateRangeResponse
            Consumers Request Counts within Date Range

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumers.consumer_request_counts_all(
                consumer_id="test_user_id",
                start_datetime="2021-05-01T12:00:00.000Z",
                end_datetime="2021-05-30T12:00:00.000Z",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.consumer_request_counts_all(
            consumer_id, start_datetime=start_datetime, end_datetime=end_datetime, request_options=request_options
        )
        return _response.data
