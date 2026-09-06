

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUserSessionClient, RawUserSessionClient


class UserSessionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserSessionClient
        """
        return self._raw_client

    def post_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidates the current session and clean up any remember-me authentication.

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
            api_key="YOUR_API_KEY",
        )
        client.user_session.post_logout()
        """
        _response = self._raw_client.post_logout(request_options=request_options)
        return _response.data

    def post_logout1(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidates the current session and clean up any remember-me authentication.

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
            api_key="YOUR_API_KEY",
        )
        client.user_session.post_logout1()
        """
        _response = self._raw_client.post_logout1(request_options=request_options)
        return _response.data

    def convert_header_session_to_cookie(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Forcefully return Set-Cookie header, even if the session is contained in the X-Auth-Token header.

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
            api_key="YOUR_API_KEY",
        )
        client.user_session.convert_header_session_to_cookie()
        """
        _response = self._raw_client.convert_header_session_to_cookie(request_options=request_options)
        return _response.data


class AsyncUserSessionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserSessionClient
        """
        return self._raw_client

    async def post_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidates the current session and clean up any remember-me authentication.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user_session.post_logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_logout(request_options=request_options)
        return _response.data

    async def post_logout1(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidates the current session and clean up any remember-me authentication.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user_session.post_logout1()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_logout1(request_options=request_options)
        return _response.data

    async def convert_header_session_to_cookie(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Forcefully return Set-Cookie header, even if the session is contained in the X-Auth-Token header.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user_session.convert_header_session_to_cookie()


        asyncio.run(main())
        """
        _response = await self._raw_client.convert_header_session_to_cookie(request_options=request_options)
        return _response.data
