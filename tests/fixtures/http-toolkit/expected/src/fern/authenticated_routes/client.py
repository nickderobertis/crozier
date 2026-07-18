

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuthenticatedRoutesClient, RawAuthenticatedRoutesClient


class AuthenticatedRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticatedRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticatedRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticatedRoutesClient
        """
        return self._raw_client

    def auth_basic_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by basic auth, see docs for the credentials

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authenticated_routes.auth_basic_auth()
        """
        _response = self._raw_client.auth_basic_auth(request_options=request_options)
        return _response.data

    def auth_basic_auth_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by basic auth, see docs for the credentials

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authenticated_routes.auth_basic_auth_post()
        """
        _response = self._raw_client.auth_basic_auth_post(request_options=request_options)
        return _response.data

    def auth_jwt_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by SHA256 JWT auth, see docs for obtaining the token

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authenticated_routes.auth_jwt_auth()
        """
        _response = self._raw_client.auth_jwt_auth(request_options=request_options)
        return _response.data

    def auth_jwt_auth_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by basic auth, see docs for the credentials

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authenticated_routes.auth_jwt_auth_post()
        """
        _response = self._raw_client.auth_jwt_auth_post(request_options=request_options)
        return _response.data


class AsyncAuthenticatedRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticatedRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticatedRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticatedRoutesClient
        """
        return self._raw_client

    async def auth_basic_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by basic auth, see docs for the credentials

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authenticated_routes.auth_basic_auth()


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_basic_auth(request_options=request_options)
        return _response.data

    async def auth_basic_auth_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by basic auth, see docs for the credentials

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authenticated_routes.auth_basic_auth_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_basic_auth_post(request_options=request_options)
        return _response.data

    async def auth_jwt_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by SHA256 JWT auth, see docs for obtaining the token

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authenticated_routes.auth_jwt_auth()


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_jwt_auth(request_options=request_options)
        return _response.data

    async def auth_jwt_auth_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Route is protected by basic auth, see docs for the credentials

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authenticated_routes.auth_jwt_auth_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_jwt_auth_post(request_options=request_options)
        return _response.data
