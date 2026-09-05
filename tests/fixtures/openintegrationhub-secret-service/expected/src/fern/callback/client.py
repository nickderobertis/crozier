

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCallbackClient, RawCallbackClient


class CallbackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCallbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCallbackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCallbackClient
        """
        return self._raw_client

    def platform_auth_flow(
        self,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Should be called by service only

        Parameters
        ----------
        code : typing.Optional[str]
            Authorization code to obtain access token from provider

        state : typing.Optional[str]
            Base64Url encoded, contains auth flow id and meta data

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
        client.callback.platform_auth_flow()
        """
        _response = self._raw_client.platform_auth_flow(code=code, state=state, request_options=request_options)
        return _response.data


class AsyncCallbackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCallbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCallbackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCallbackClient
        """
        return self._raw_client

    async def platform_auth_flow(
        self,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Should be called by service only

        Parameters
        ----------
        code : typing.Optional[str]
            Authorization code to obtain access token from provider

        state : typing.Optional[str]
            Base64Url encoded, contains auth flow id and meta data

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
            await client.callback.platform_auth_flow()


        asyncio.run(main())
        """
        _response = await self._raw_client.platform_auth_flow(code=code, state=state, request_options=request_options)
        return _response.data
