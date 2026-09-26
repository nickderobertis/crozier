

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawServerClient, RawServerClient
from .types.get_version_response import GetVersionResponse


OMIT = typing.cast(typing.Any, ...)


class ServerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServerClient
        """
        return self._raw_client

    def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetVersionResponse:
        """
        Returns the current version of the API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVersionResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.server.get_version()
        """
        _response = self._raw_client.get_version(request_options=request_options)
        return _response.data

    def post_disconnect(
        self,
        *,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Disconnects the application from the Fergus API and revokes all tokens.

        Parameters
        ----------
        refresh_token : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.server.post_disconnect(
            refresh_token="refreshToken",
            client_id="clientId",
            client_secret="clientSecret",
        )
        """
        _response = self._raw_client.post_disconnect(
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data


class AsyncServerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServerClient
        """
        return self._raw_client

    async def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetVersionResponse:
        """
        Returns the current version of the API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVersionResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.server.get_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_version(request_options=request_options)
        return _response.data

    async def post_disconnect(
        self,
        *,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Disconnects the application from the Fergus API and revokes all tokens.

        Parameters
        ----------
        refresh_token : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.server.post_disconnect(
                refresh_token="refreshToken",
                client_id="clientId",
                client_secret="clientSecret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_disconnect(
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data
