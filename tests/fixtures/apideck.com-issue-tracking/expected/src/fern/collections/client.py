

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collections_sort import CollectionsSort
from ..types.get_collection_response import GetCollectionResponse
from ..types.get_collections_response import GetCollectionsResponse
from .raw_client import AsyncRawCollectionsClient, RawCollectionsClient


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[CollectionsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionsResponse:
        """
        List Collections

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[CollectionsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionsResponse
            List Collections

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.collections.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, sort=sort, fields=fields, request_options=request_options
        )
        return _response.data

    def one(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionResponse:
        """
        Get Collection

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionResponse
            Get a Collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.collections.one(
            collection_id="apideck-io",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(collection_id, raw=raw, fields=fields, request_options=request_options)
        return _response.data


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[CollectionsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionsResponse:
        """
        List Collections

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[CollectionsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionsResponse
            List Collections

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, sort=sort, fields=fields, request_options=request_options
        )
        return _response.data

    async def one(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionResponse:
        """
        Get Collection

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionResponse
            Get a Collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.one(
                collection_id="apideck-io",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(collection_id, raw=raw, fields=fields, request_options=request_options)
        return _response.data
