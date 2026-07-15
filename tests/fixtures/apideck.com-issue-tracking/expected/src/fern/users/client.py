

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_collection_user_response import GetCollectionUserResponse
from ..types.get_collection_users_response import GetCollectionUsersResponse
from .raw_client import AsyncRawUsersClient, RawUsersClient


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def collection_users_all(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionUsersResponse:
        """
        List Users

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionUsersResponse
            Users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.users.collection_users_all(
            collection_id="apideck-io",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.collection_users_all(
            collection_id, raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    def collection_users_one(
        self,
        collection_id: str,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionUserResponse:
        """
        Get user

        Parameters
        ----------
        collection_id : str
            The collection ID

        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionUserResponse
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.users.collection_users_one(
            collection_id="apideck-io",
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.collection_users_one(
            collection_id, id, raw=raw, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def collection_users_all(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionUsersResponse:
        """
        List Users

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionUsersResponse
            Users

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
            await client.users.collection_users_all(
                collection_id="apideck-io",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_users_all(
            collection_id, raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    async def collection_users_one(
        self,
        collection_id: str,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionUserResponse:
        """
        Get user

        Parameters
        ----------
        collection_id : str
            The collection ID

        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionUserResponse
            User

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
            await client.users.collection_users_one(
                collection_id="apideck-io",
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_users_one(
            collection_id, id, raw=raw, fields=fields, request_options=request_options
        )
        return _response.data
