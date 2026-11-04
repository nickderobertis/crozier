

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.jwk_set_response import JwkSetResponse
from ..types.o_auth2metadata_response import OAuth2MetadataResponse
from .raw_client import AsyncRawOAuth2DiscoveryClient, RawOAuth2DiscoveryClient


class OAuth2DiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuth2DiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuth2DiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuth2DiscoveryClient
        """
        return self._raw_client

    def get_jwks(self, *, request_options: typing.Optional[RequestOptions] = None) -> JwkSetResponse:
        """
        Returns the broker's aggregated public signing keys in JWK Set format (RFC 7517).

        Clients use this single endpoint to verify any token the broker asks them to trust,
        regardless of operating mode. Only public key material is included — private keys
        are never exposed.

        **Mode-dependent content**:
        - `local` mode: returns only the broker's locally-generated signing keys.
        - `proxy` mode: republishes the upstream authorization server's public keys verbatim.
        - `hybrid` mode: returns the union of local signing keys and upstream keys in a
          single JWKS document. If any `kid` appears in both sets, the endpoint returns 500.

        **Availability**: Served in all three modes (`local`, `proxy`, `hybrid`). Returns
        503 if the upstream JWKS is unavailable (proxy/hybrid modes). Returns 500 if a
        duplicate `kid` is detected across local and upstream key sets (hybrid mode).

        **Caching**: Responses include `Cache-Control: public, max-age=300` to allow
        clients to cache the key set for 5 minutes. Clients should respect this header
        and implement key rotation by periodically refreshing the JWKS.

        **Key Rotation**: When signing keys are rotated, the new key appears in the
        JWKS immediately. Previous keys remain in the set until removed by an admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwkSetResponse
            JWK Set containing public signing keys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.o_auth2discovery.get_jwks()
        """
        _response = self._raw_client.get_jwks(request_options=request_options)
        return _response.data

    def get_o_auth2server_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OAuth2MetadataResponse:
        """
        Returns the broker's OAuth2 authorization server metadata as defined
        in RFC 8414. This enables dynamic client discovery of the broker's
        OAuth2 capabilities and endpoints.

        **Mode-specific behavior**:
        - `proxy` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which republishes upstream keys.
        - `local` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which serves locally-generated signing keys.
        - `hybrid` mode: `issuer` is the broker's public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint (union of local and upstream keys). The
          metadata reflects the union of capabilities for both proxy and local grant types.

        **Caching**: Responses include `Cache-Control: public, max-age=3600` to allow
        clients to cache metadata for 1 hour.

        **No Authentication**: This endpoint is publicly accessible as required by RFC 8414.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2MetadataResponse
            OAuth2 Authorization Server Metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.o_auth2discovery.get_o_auth2server_metadata()
        """
        _response = self._raw_client.get_o_auth2server_metadata(request_options=request_options)
        return _response.data


class AsyncOAuth2DiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuth2DiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuth2DiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuth2DiscoveryClient
        """
        return self._raw_client

    async def get_jwks(self, *, request_options: typing.Optional[RequestOptions] = None) -> JwkSetResponse:
        """
        Returns the broker's aggregated public signing keys in JWK Set format (RFC 7517).

        Clients use this single endpoint to verify any token the broker asks them to trust,
        regardless of operating mode. Only public key material is included — private keys
        are never exposed.

        **Mode-dependent content**:
        - `local` mode: returns only the broker's locally-generated signing keys.
        - `proxy` mode: republishes the upstream authorization server's public keys verbatim.
        - `hybrid` mode: returns the union of local signing keys and upstream keys in a
          single JWKS document. If any `kid` appears in both sets, the endpoint returns 500.

        **Availability**: Served in all three modes (`local`, `proxy`, `hybrid`). Returns
        503 if the upstream JWKS is unavailable (proxy/hybrid modes). Returns 500 if a
        duplicate `kid` is detected across local and upstream key sets (hybrid mode).

        **Caching**: Responses include `Cache-Control: public, max-age=300` to allow
        clients to cache the key set for 5 minutes. Clients should respect this header
        and implement key rotation by periodically refreshing the JWKS.

        **Key Rotation**: When signing keys are rotated, the new key appears in the
        JWKS immediately. Previous keys remain in the set until removed by an admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwkSetResponse
            JWK Set containing public signing keys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth2discovery.get_jwks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jwks(request_options=request_options)
        return _response.data

    async def get_o_auth2server_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OAuth2MetadataResponse:
        """
        Returns the broker's OAuth2 authorization server metadata as defined
        in RFC 8414. This enables dynamic client discovery of the broker's
        OAuth2 capabilities and endpoints.

        **Mode-specific behavior**:
        - `proxy` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which republishes upstream keys.
        - `local` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which serves locally-generated signing keys.
        - `hybrid` mode: `issuer` is the broker's public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint (union of local and upstream keys). The
          metadata reflects the union of capabilities for both proxy and local grant types.

        **Caching**: Responses include `Cache-Control: public, max-age=3600` to allow
        clients to cache metadata for 1 hour.

        **No Authentication**: This endpoint is publicly accessible as required by RFC 8414.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2MetadataResponse
            OAuth2 Authorization Server Metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth2discovery.get_o_auth2server_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_o_auth2server_metadata(request_options=request_options)
        return _response.data
