

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_credential_password_ip_listing import UserCredentialPasswordIpListing
from ..types.user_credential_password_ip_read import UserCredentialPasswordIpRead
from .raw_client import AsyncRawCredentialPasswordIpClient, RawCredentialPasswordIpClient


class CredentialPasswordIpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCredentialPasswordIpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCredentialPasswordIpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCredentialPasswordIpClient
        """
        return self._raw_client

    def list_all_credential_password_ip_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserCredentialPasswordIpListing]:
        """
        Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserCredentialPasswordIpListing]
            Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

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
        client.credential_password_ip.list_all_credential_password_ip_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_credential_password_ip_for_user(user_id, request_options=request_options)
        return _response.data

    def read_credential_password_ip_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserCredentialPasswordIpRead:
        """
        Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCredentialPasswordIpRead
            Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

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
        client.credential_password_ip.read_credential_password_ip_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_credential_password_ip_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncCredentialPasswordIpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCredentialPasswordIpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCredentialPasswordIpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCredentialPasswordIpClient
        """
        return self._raw_client

    async def list_all_credential_password_ip_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserCredentialPasswordIpListing]:
        """
        Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserCredentialPasswordIpListing]
            Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

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
            await client.credential_password_ip.list_all_credential_password_ip_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_credential_password_ip_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def read_credential_password_ip_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserCredentialPasswordIpRead:
        """
        Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCredentialPasswordIpRead
            Create a credential of a user for server authentication, or delete the credential of a user for server authentication.

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
            await client.credential_password_ip.read_credential_password_ip_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_credential_password_ip_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
