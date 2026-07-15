

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_shared_link_response import CreateSharedLinkResponse
from ..types.created_at import CreatedAt
from ..types.delete_shared_link_response import DeleteSharedLinkResponse
from ..types.expires_at import ExpiresAt
from ..types.get_shared_link_response import GetSharedLinkResponse
from ..types.get_shared_links_response import GetSharedLinksResponse
from ..types.shared_link_scope import SharedLinkScope
from ..types.shared_link_target import SharedLinkTarget
from ..types.update_shared_link_response import UpdateSharedLinkResponse
from ..types.updated_at import UpdatedAt
from .raw_client import AsyncRawSharedLinksClient, RawSharedLinksClient


OMIT = typing.cast(typing.Any, ...)


class SharedLinksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSharedLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSharedLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSharedLinksClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSharedLinksResponse:
        """
        List SharedLinks

        Parameters
        ----------
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
        GetSharedLinksResponse
            Shared Links

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.shared_links.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSharedLinkResponse:
        """
        Create Shared Link

        Parameters
        ----------
        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSharedLinkResponse
            Shared Links

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.shared_links.add(
            target_id="target_id",
        )
        """
        _response = self._raw_client.add(
            target_id=target_id,
            raw=raw,
            created_at=created_at,
            download_url=download_url,
            expires_at=expires_at,
            password=password,
            password_protected=password_protected,
            scope=scope,
            target=target,
            updated_at=updated_at,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSharedLinkResponse:
        """
        Get Shared Link

        Parameters
        ----------
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
        GetSharedLinkResponse
            Shared Link

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.shared_links.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSharedLinkResponse:
        """
        Delete Shared Link

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSharedLinkResponse
            Shared Links

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.shared_links.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id: str,
        *,
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSharedLinkResponse:
        """
        Update Shared Link

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSharedLinkResponse
            Shared Links

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.shared_links.update(
            id="id",
            target_id="target_id",
        )
        """
        _response = self._raw_client.update(
            id,
            target_id=target_id,
            raw=raw,
            created_at=created_at,
            download_url=download_url,
            expires_at=expires_at,
            password=password,
            password_protected=password_protected,
            scope=scope,
            target=target,
            updated_at=updated_at,
            url=url,
            request_options=request_options,
        )
        return _response.data


class AsyncSharedLinksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSharedLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSharedLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSharedLinksClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSharedLinksResponse:
        """
        List SharedLinks

        Parameters
        ----------
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
        GetSharedLinksResponse
            Shared Links

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
            await client.shared_links.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSharedLinkResponse:
        """
        Create Shared Link

        Parameters
        ----------
        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSharedLinkResponse
            Shared Links

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
            await client.shared_links.add(
                target_id="target_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            target_id=target_id,
            raw=raw,
            created_at=created_at,
            download_url=download_url,
            expires_at=expires_at,
            password=password,
            password_protected=password_protected,
            scope=scope,
            target=target,
            updated_at=updated_at,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSharedLinkResponse:
        """
        Get Shared Link

        Parameters
        ----------
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
        GetSharedLinkResponse
            Shared Link

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
            await client.shared_links.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSharedLinkResponse:
        """
        Delete Shared Link

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSharedLinkResponse
            Shared Links

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
            await client.shared_links.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id: str,
        *,
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSharedLinkResponse:
        """
        Update Shared Link

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSharedLinkResponse
            Shared Links

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
            await client.shared_links.update(
                id="id",
                target_id="target_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id,
            target_id=target_id,
            raw=raw,
            created_at=created_at,
            download_url=download_url,
            expires_at=expires_at,
            password=password,
            password_protected=password_protected,
            scope=scope,
            target=target,
            updated_at=updated_at,
            url=url,
            request_options=request_options,
        )
        return _response.data
