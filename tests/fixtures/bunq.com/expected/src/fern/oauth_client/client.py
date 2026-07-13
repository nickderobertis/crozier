

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.oauth_client_create import OauthClientCreate
from ..types.oauth_client_listing import OauthClientListing
from ..types.oauth_client_read import OauthClientRead
from ..types.oauth_client_update import OauthClientUpdate
from .raw_client import AsyncRawOauthClientClient, RawOauthClientClient


OMIT = typing.cast(typing.Any, ...)


class OauthClientClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOauthClientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOauthClientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOauthClientClient
        """
        return self._raw_client

    def list_all_oauth_client_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OauthClientListing]:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OauthClientListing]
            Used for managing OAuth Clients.

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
        client.oauth_client.list_all_oauth_client_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_oauth_client_for_user(user_id, request_options=request_options)
        return _response.data

    def create_oauth_client_for_user(
        self,
        user_id: int,
        *,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthClientCreate:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        status : typing.Optional[str]
            The status of the Oauth Client, can be ACTIVE or CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthClientCreate
            Used for managing OAuth Clients.

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
        client.oauth_client.create_oauth_client_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.create_oauth_client_for_user(
            user_id, status=status, request_options=request_options
        )
        return _response.data

    def read_oauth_client_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OauthClientRead:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthClientRead
            Used for managing OAuth Clients.

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
        client.oauth_client.read_oauth_client_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_oauth_client_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    def update_oauth_client_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthClientUpdate:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        item_id : int


        status : typing.Optional[str]
            The status of the Oauth Client, can be ACTIVE or CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthClientUpdate
            Used for managing OAuth Clients.

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
        client.oauth_client.update_oauth_client_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_oauth_client_for_user(
            user_id, item_id, status=status, request_options=request_options
        )
        return _response.data


class AsyncOauthClientClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOauthClientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOauthClientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOauthClientClient
        """
        return self._raw_client

    async def list_all_oauth_client_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OauthClientListing]:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OauthClientListing]
            Used for managing OAuth Clients.

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
            await client.oauth_client.list_all_oauth_client_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_oauth_client_for_user(user_id, request_options=request_options)
        return _response.data

    async def create_oauth_client_for_user(
        self,
        user_id: int,
        *,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthClientCreate:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        status : typing.Optional[str]
            The status of the Oauth Client, can be ACTIVE or CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthClientCreate
            Used for managing OAuth Clients.

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
            await client.oauth_client.create_oauth_client_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_oauth_client_for_user(
            user_id, status=status, request_options=request_options
        )
        return _response.data

    async def read_oauth_client_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OauthClientRead:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthClientRead
            Used for managing OAuth Clients.

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
            await client.oauth_client.read_oauth_client_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_oauth_client_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    async def update_oauth_client_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OauthClientUpdate:
        """
        Used for managing OAuth Clients.

        Parameters
        ----------
        user_id : int


        item_id : int


        status : typing.Optional[str]
            The status of the Oauth Client, can be ACTIVE or CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OauthClientUpdate
            Used for managing OAuth Clients.

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
            await client.oauth_client.update_oauth_client_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_oauth_client_for_user(
            user_id, item_id, status=status, request_options=request_options
        )
        return _response.data
