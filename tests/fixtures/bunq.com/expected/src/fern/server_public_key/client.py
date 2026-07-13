

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.installation_server_public_key_listing import InstallationServerPublicKeyListing
from .raw_client import AsyncRawServerPublicKeyClient, RawServerPublicKeyClient


class ServerPublicKeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServerPublicKeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServerPublicKeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServerPublicKeyClient
        """
        return self._raw_client

    def list_all_server_public_key_for_installation(
        self, installation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstallationServerPublicKeyListing]:
        """
        Show the ServerPublicKey for this Installation.

        Parameters
        ----------
        installation_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstallationServerPublicKeyListing]
            Using /installation/_/server-public-key you can request the ServerPublicKey again. This is done by referring to the id of the Installation.

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
        client.server_public_key.list_all_server_public_key_for_installation(
            installation_id=1,
        )
        """
        _response = self._raw_client.list_all_server_public_key_for_installation(
            installation_id, request_options=request_options
        )
        return _response.data


class AsyncServerPublicKeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServerPublicKeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServerPublicKeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServerPublicKeyClient
        """
        return self._raw_client

    async def list_all_server_public_key_for_installation(
        self, installation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstallationServerPublicKeyListing]:
        """
        Show the ServerPublicKey for this Installation.

        Parameters
        ----------
        installation_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstallationServerPublicKeyListing]
            Using /installation/_/server-public-key you can request the ServerPublicKey again. This is done by referring to the id of the Installation.

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
            await client.server_public_key.list_all_server_public_key_for_installation(
                installation_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_server_public_key_for_installation(
            installation_id, request_options=request_options
        )
        return _response.data
