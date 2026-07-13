

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.oauth_callback_url_create import OauthCallbackUrlCreate
from ..types.oauth_callback_url_delete import OauthCallbackUrlDelete
from ..types.oauth_callback_url_listing import OauthCallbackUrlListing
from ..types.oauth_callback_url_read import OauthCallbackUrlRead
from ..types.oauth_callback_url_update import OauthCallbackUrlUpdate
from .raw_client import AsyncRawCallbackUrlClient, RawCallbackUrlClient


OMIT = typing.cast(typing.Any, ...)


class CallbackUrlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCallbackUrlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCallbackUrlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCallbackUrlClient
        """
        return self._raw_client

    def list_all_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OauthCallbackUrlListing]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OauthCallbackUrlListing]
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.callback_url.list_all_callback_url_for_user_oauth_client(
            user_id=1,
            oauth_client_id=1,
        )
        """
        _response = self._raw_client.list_all_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, request_options=request_options
        )
        return _response.data

    def create_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OauthCallbackUrlCreate:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlCreate
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.callback_url.create_callback_url_for_user_oauth_client(
            user_id=1,
            oauth_client_id=1,
            url="url",
        )
        """
        _response = self._raw_client.create_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, url=url, request_options=request_options
        )
        return _response.data

    def read_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthCallbackUrlRead:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlRead
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.callback_url.read_callback_url_for_user_oauth_client(
            user_id=1,
            oauth_client_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, item_id, request_options=request_options
        )
        return _response.data

    def update_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthCallbackUrlUpdate:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlUpdate
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.callback_url.update_callback_url_for_user_oauth_client(
            user_id=1,
            oauth_client_id=1,
            item_id=1,
            url="url",
        )
        """
        _response = self._raw_client.update_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, item_id, url=url, request_options=request_options
        )
        return _response.data

    def delete_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthCallbackUrlDelete:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlDelete
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.callback_url.delete_callback_url_for_user_oauth_client(
            user_id=1,
            oauth_client_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncCallbackUrlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCallbackUrlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCallbackUrlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCallbackUrlClient
        """
        return self._raw_client

    async def list_all_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OauthCallbackUrlListing]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OauthCallbackUrlListing]
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.callback_url.list_all_callback_url_for_user_oauth_client(
                user_id=1,
                oauth_client_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, request_options=request_options
        )
        return _response.data

    async def create_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OauthCallbackUrlCreate:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlCreate
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.callback_url.create_callback_url_for_user_oauth_client(
                user_id=1,
                oauth_client_id=1,
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, url=url, request_options=request_options
        )
        return _response.data

    async def read_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthCallbackUrlRead:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlRead
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.callback_url.read_callback_url_for_user_oauth_client(
                user_id=1,
                oauth_client_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthCallbackUrlUpdate:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlUpdate
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.callback_url.update_callback_url_for_user_oauth_client(
                user_id=1,
                oauth_client_id=1,
                item_id=1,
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, item_id, url=url, request_options=request_options
        )
        return _response.data

    async def delete_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthCallbackUrlDelete:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthCallbackUrlDelete
            Used for managing OAuth Client Callback URLs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.callback_url.delete_callback_url_for_user_oauth_client(
                user_id=1,
                oauth_client_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_callback_url_for_user_oauth_client(
            user_id, oauth_client_id, item_id, request_options=request_options
        )
        return _response.data
