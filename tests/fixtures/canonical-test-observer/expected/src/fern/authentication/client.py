

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuthenticationClient, RawAuthenticationClient


class AuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticationClient
        """
        return self._raw_client

    def saml_login(
        self, *, return_to: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        return_to : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authentication.saml_login()
        """
        _response = self._raw_client.saml_login(return_to=return_to, request_options=request_options)
        return _response.data

    def saml_logout(
        self, *, return_to: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        return_to : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authentication.saml_logout()
        """
        _response = self._raw_client.saml_logout(return_to=return_to, request_options=request_options)
        return _response.data

    def saml_login_callback(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authentication.saml_login_callback()
        """
        _response = self._raw_client.saml_login_callback(request_options=request_options)
        return _response.data

    def saml_logout_callback(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.authentication.saml_logout_callback()
        """
        _response = self._raw_client.saml_logout_callback(request_options=request_options)
        return _response.data


class AsyncAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticationClient
        """
        return self._raw_client

    async def saml_login(
        self, *, return_to: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        return_to : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authentication.saml_login()


        asyncio.run(main())
        """
        _response = await self._raw_client.saml_login(return_to=return_to, request_options=request_options)
        return _response.data

    async def saml_logout(
        self, *, return_to: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        return_to : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authentication.saml_logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.saml_logout(return_to=return_to, request_options=request_options)
        return _response.data

    async def saml_login_callback(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authentication.saml_login_callback()


        asyncio.run(main())
        """
        _response = await self._raw_client.saml_login_callback(request_options=request_options)
        return _response.data

    async def saml_logout_callback(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.authentication.saml_logout_callback()


        asyncio.run(main())
        """
        _response = await self._raw_client.saml_logout_callback(request_options=request_options)
        return _response.data
