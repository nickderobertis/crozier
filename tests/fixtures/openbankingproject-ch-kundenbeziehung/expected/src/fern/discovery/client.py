

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.fapi_configuration import FapiConfiguration
from ..types.jwk_set import JwkSet
from ..types.oidc_discovery import OidcDiscovery
from ..types.swiss_banking_metadata import SwissBankingMetadata
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

    def openid_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> OidcDiscovery:
        """
        OpenID Connect Discovery 1.0 compliant discovery document with FAPI 2.0 metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcDiscovery
            OpenID Connect configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery.openid_configuration()
        """
        _response = self._raw_client.openid_configuration(request_options=request_options)
        return _response.data

    def fapi_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> FapiConfiguration:
        """
        FAPI 2.0 specific configuration metadata for Swiss financial services.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FapiConfiguration
            FAPI configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery.fapi_configuration()
        """
        _response = self._raw_client.fapi_configuration(request_options=request_options)
        return _response.data

    def jwks(self, *, request_options: typing.Optional[RequestOptions] = None) -> JwkSet:
        """
        Public keys for JWT signature verification (RFC 7517).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwkSet
            JSON Web Key Set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery.jwks()
        """
        _response = self._raw_client.jwks(request_options=request_options)
        return _response.data

    def swiss_banking_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SwissBankingMetadata:
        """
        Swiss Open Banking specific metadata including supported use cases and standards.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SwissBankingMetadata
            Swiss banking metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery.swiss_banking_metadata()
        """
        _response = self._raw_client.swiss_banking_metadata(request_options=request_options)
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

    async def openid_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> OidcDiscovery:
        """
        OpenID Connect Discovery 1.0 compliant discovery document with FAPI 2.0 metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcDiscovery
            OpenID Connect configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.openid_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.openid_configuration(request_options=request_options)
        return _response.data

    async def fapi_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> FapiConfiguration:
        """
        FAPI 2.0 specific configuration metadata for Swiss financial services.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FapiConfiguration
            FAPI configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.fapi_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.fapi_configuration(request_options=request_options)
        return _response.data

    async def jwks(self, *, request_options: typing.Optional[RequestOptions] = None) -> JwkSet:
        """
        Public keys for JWT signature verification (RFC 7517).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwkSet
            JSON Web Key Set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.jwks()


        asyncio.run(main())
        """
        _response = await self._raw_client.jwks(request_options=request_options)
        return _response.data

    async def swiss_banking_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SwissBankingMetadata:
        """
        Swiss Open Banking specific metadata including supported use cases and standards.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SwissBankingMetadata
            Swiss banking metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.swiss_banking_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.swiss_banking_metadata(request_options=request_options)
        return _response.data
