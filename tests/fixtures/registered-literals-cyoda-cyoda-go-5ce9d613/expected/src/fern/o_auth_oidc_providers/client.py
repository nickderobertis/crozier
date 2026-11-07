

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.oidc_provider_response_dto import OidcProviderResponseDto
from .raw_client import AsyncRawOAuthOidcProvidersClient, RawOAuthOidcProvidersClient


OMIT = typing.cast(typing.Any, ...)


class OAuthOidcProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuthOidcProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuthOidcProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuthOidcProvidersClient
        """
        return self._raw_client

    def list_oidc_providers(
        self, *, active_only: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OidcProviderResponseDto]:
        """
        Retrieves a list of all registered OIDC providers, including both active and inactive providers.

        Parameters
        ----------
        active_only : typing.Optional[str]
            If true, returns only active providers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OidcProviderResponseDto]
            List of OIDC providers retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_oidc_providers.list_oidc_providers()
        """
        _response = self._raw_client.list_oidc_providers(active_only=active_only, request_options=request_options)
        return _response.data

    def register_oidc_provider(
        self,
        *,
        well_known_config_uri: str,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OidcProviderResponseDto:
        """
        Registers a new external OIDC provider for JWT validation. The provider's public keys will be
        discovered from the well-known configuration endpoint and used to validate JWT tokens.

        Parameters
        ----------
        well_known_config_uri : str
            URI to the OIDC provider's well-known configuration endpoint

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcProviderResponseDto
            OIDC provider registered successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_oidc_providers.register_oidc_provider(
            well_known_config_uri="https://oidc-domain.local/.well-known/openid-configuration",
        )
        """
        _response = self._raw_client.register_oidc_provider(
            well_known_config_uri=well_known_config_uri, issuers=issuers, request_options=request_options
        )
        return _response.data

    def reload_oidc_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Reloads all active OIDC provider configurations from the database and synchronizes
        cached keys with the remote JWKS endpoints.

        Key synchronization: For each provider, this operation fetches the current keys from
        the remote JWKS endpoint and invalidates any locally cached keys that no longer exist
        in the remote JWKS. This is useful for security when OIDC providers have rotated or
        revoked keys.

        This operation is useful when you want to ensure all nodes have the latest OIDC provider
        configurations and that any revoked keys are no longer trusted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_oidc_providers.reload_oidc_providers()
        """
        _response = self._raw_client.reload_oidc_providers(request_options=request_options)
        return _response.data

    def delete_oidc_provider(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an OIDC provider and all its associated JWK keys.
        The provider will first be invalidated (if not already) and then removed from storage.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_oidc_providers.delete_oidc_provider(
            id="id",
        )
        """
        _response = self._raw_client.delete_oidc_provider(id, request_options=request_options)
        return _response.data

    def update_oidc_provider(
        self,
        id: str,
        *,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OidcProviderResponseDto:
        """
        Updates configuration for an OIDC provider.

        Note: Updating the issuers list immediately deletes all cached keys for this provider.
        This ensures that JWTs from issuers that are no longer trusted cannot be validated using
        previously cached keys. The keys will be re-fetched from the remote JWKS endpoint with the
        new issuer configuration when they are next needed for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcProviderResponseDto
            OIDC provider issuers updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_oidc_providers.update_oidc_provider(
            id="id",
        )
        """
        _response = self._raw_client.update_oidc_provider(id, issuers=issuers, request_options=request_options)
        return _response.data

    def invalidate_oidc_provider(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidates an OIDC provider, marking it as inactive and invalidating all loaded public keys
        associated with this provider. The provider configuration is retained but will no longer be
        used for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to invalidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_oidc_providers.invalidate_oidc_provider(
            id="id",
        )
        """
        _response = self._raw_client.invalidate_oidc_provider(id, request_options=request_options)
        return _response.data

    def reactivate_oidc_provider(
        self,
        id: str,
        *,
        reactivate_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OidcProviderResponseDto:
        """
        Reactivates a previously invalidated OIDC provider. The provider will be marked as active
        and can be used for JWT validation again.
        This operation is idempotent - if the provider is already active, it returns the current state.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to reactivate

        reactivate_keys : typing.Optional[bool]
            If true, also reactivates all related JWK keys that were invalidated with this provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcProviderResponseDto
            OIDC provider reactivated successfully or already active

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_oidc_providers.reactivate_oidc_provider(
            id="id",
        )
        """
        _response = self._raw_client.reactivate_oidc_provider(
            id, reactivate_keys=reactivate_keys, request_options=request_options
        )
        return _response.data


class AsyncOAuthOidcProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuthOidcProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuthOidcProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuthOidcProvidersClient
        """
        return self._raw_client

    async def list_oidc_providers(
        self, *, active_only: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OidcProviderResponseDto]:
        """
        Retrieves a list of all registered OIDC providers, including both active and inactive providers.

        Parameters
        ----------
        active_only : typing.Optional[str]
            If true, returns only active providers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OidcProviderResponseDto]
            List of OIDC providers retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_oidc_providers.list_oidc_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_oidc_providers(active_only=active_only, request_options=request_options)
        return _response.data

    async def register_oidc_provider(
        self,
        *,
        well_known_config_uri: str,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OidcProviderResponseDto:
        """
        Registers a new external OIDC provider for JWT validation. The provider's public keys will be
        discovered from the well-known configuration endpoint and used to validate JWT tokens.

        Parameters
        ----------
        well_known_config_uri : str
            URI to the OIDC provider's well-known configuration endpoint

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcProviderResponseDto
            OIDC provider registered successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_oidc_providers.register_oidc_provider(
                well_known_config_uri="https://oidc-domain.local/.well-known/openid-configuration",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_oidc_provider(
            well_known_config_uri=well_known_config_uri, issuers=issuers, request_options=request_options
        )
        return _response.data

    async def reload_oidc_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Reloads all active OIDC provider configurations from the database and synchronizes
        cached keys with the remote JWKS endpoints.

        Key synchronization: For each provider, this operation fetches the current keys from
        the remote JWKS endpoint and invalidates any locally cached keys that no longer exist
        in the remote JWKS. This is useful for security when OIDC providers have rotated or
        revoked keys.

        This operation is useful when you want to ensure all nodes have the latest OIDC provider
        configurations and that any revoked keys are no longer trusted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_oidc_providers.reload_oidc_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.reload_oidc_providers(request_options=request_options)
        return _response.data

    async def delete_oidc_provider(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an OIDC provider and all its associated JWK keys.
        The provider will first be invalidated (if not already) and then removed from storage.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_oidc_providers.delete_oidc_provider(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_oidc_provider(id, request_options=request_options)
        return _response.data

    async def update_oidc_provider(
        self,
        id: str,
        *,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OidcProviderResponseDto:
        """
        Updates configuration for an OIDC provider.

        Note: Updating the issuers list immediately deletes all cached keys for this provider.
        This ensures that JWTs from issuers that are no longer trusted cannot be validated using
        previously cached keys. The keys will be re-fetched from the remote JWKS endpoint with the
        new issuer configuration when they are next needed for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcProviderResponseDto
            OIDC provider issuers updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_oidc_providers.update_oidc_provider(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_oidc_provider(id, issuers=issuers, request_options=request_options)
        return _response.data

    async def invalidate_oidc_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Invalidates an OIDC provider, marking it as inactive and invalidating all loaded public keys
        associated with this provider. The provider configuration is retained but will no longer be
        used for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to invalidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_oidc_providers.invalidate_oidc_provider(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_oidc_provider(id, request_options=request_options)
        return _response.data

    async def reactivate_oidc_provider(
        self,
        id: str,
        *,
        reactivate_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OidcProviderResponseDto:
        """
        Reactivates a previously invalidated OIDC provider. The provider will be marked as active
        and can be used for JWT validation again.
        This operation is idempotent - if the provider is already active, it returns the current state.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to reactivate

        reactivate_keys : typing.Optional[bool]
            If true, also reactivates all related JWK keys that were invalidated with this provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OidcProviderResponseDto
            OIDC provider reactivated successfully or already active

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_oidc_providers.reactivate_oidc_provider(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reactivate_oidc_provider(
            id, reactivate_keys=reactivate_keys, request_options=request_options
        )
        return _response.data
