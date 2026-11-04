

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.auth_provider import AuthProvider
from ..types.listed_auth_provider import ListedAuthProvider
from .raw_client import AsyncRawAuthProviderV1Alpha1ConsoleClient, RawAuthProviderV1Alpha1ConsoleClient


class AuthProviderV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthProviderV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthProviderV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthProviderV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_auth_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListedAuthProvider]:
        """
        Lists all auth providers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListedAuthProvider]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_provider_v1alpha1console.list_auth_providers()
        """
        _response = self._raw_client.list_auth_providers(request_options=request_options)
        return _response.data

    def disable_auth_provider(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthProvider:
        """
        Disables an auth provider

        Parameters
        ----------
        name : str
            metadata.name of the auth provider to disable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthProvider
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_provider_v1alpha1console.disable_auth_provider(
            name="name",
        )
        """
        _response = self._raw_client.disable_auth_provider(name, request_options=request_options)
        return _response.data

    def enable_auth_provider(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthProvider:
        """
        Enables an auth provider

        Parameters
        ----------
        name : str
            metadata.name of the auth provider to enable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthProvider
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_provider_v1alpha1console.enable_auth_provider(
            name="name",
        )
        """
        _response = self._raw_client.enable_auth_provider(name, request_options=request_options)
        return _response.data


class AsyncAuthProviderV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthProviderV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthProviderV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthProviderV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_auth_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListedAuthProvider]:
        """
        Lists all auth providers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListedAuthProvider]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_provider_v1alpha1console.list_auth_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_auth_providers(request_options=request_options)
        return _response.data

    async def disable_auth_provider(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthProvider:
        """
        Disables an auth provider

        Parameters
        ----------
        name : str
            metadata.name of the auth provider to disable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthProvider
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_provider_v1alpha1console.disable_auth_provider(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_auth_provider(name, request_options=request_options)
        return _response.data

    async def enable_auth_provider(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthProvider:
        """
        Enables an auth provider

        Parameters
        ----------
        name : str
            metadata.name of the auth provider to enable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthProvider
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_provider_v1alpha1console.enable_auth_provider(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_auth_provider(name, request_options=request_options)
        return _response.data
