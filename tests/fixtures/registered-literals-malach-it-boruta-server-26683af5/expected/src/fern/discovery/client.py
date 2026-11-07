

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorization_server_metadata import AuthorizationServerMetadata
from ..types.credential_issuer_metadata import CredentialIssuerMetadata
from .raw_client import AsyncRawDiscoveryClient, RawDiscoveryClient


class DiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDiscoveryClient
        """
        return self._raw_client

    def get_o_auth_authorization_server_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationServerMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationServerMetadata
            Authorization server metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery.get_o_auth_authorization_server_metadata()
        """
        _response = self._raw_client.get_o_auth_authorization_server_metadata(request_options=request_options)
        return _response.data

    def get_open_id_provider_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationServerMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationServerMetadata
            Authorization server metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery.get_open_id_provider_metadata()
        """
        _response = self._raw_client.get_open_id_provider_metadata(request_options=request_options)
        return _response.data

    def get_open_id_credential_issuer_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialIssuerMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialIssuerMetadata
            Credential issuer metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery.get_open_id_credential_issuer_metadata()
        """
        _response = self._raw_client.get_open_id_credential_issuer_metadata(request_options=request_options)
        return _response.data


class AsyncDiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDiscoveryClient
        """
        return self._raw_client

    async def get_o_auth_authorization_server_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationServerMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationServerMetadata
            Authorization server metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.get_o_auth_authorization_server_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_o_auth_authorization_server_metadata(request_options=request_options)
        return _response.data

    async def get_open_id_provider_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizationServerMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizationServerMetadata
            Authorization server metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.get_open_id_provider_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_open_id_provider_metadata(request_options=request_options)
        return _response.data

    async def get_open_id_credential_issuer_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialIssuerMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialIssuerMetadata
            Credential issuer metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.get_open_id_credential_issuer_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_open_id_credential_issuer_metadata(request_options=request_options)
        return _response.data
