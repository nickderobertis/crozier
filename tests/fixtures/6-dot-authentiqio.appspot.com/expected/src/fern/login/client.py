

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLoginClient, RawLoginClient
from .types.push_login_request_response import PushLoginRequestResponse


class LoginClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoginClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLoginClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoginClient
        """
        return self._raw_client

    def push_login_request(
        self, *, callback: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PushLoginRequestResponse:
        """
        push sign-in request
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        callback : str
            URI App will connect to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PushLoginRequestResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.login.push_login_request(
            callback="callback",
        )
        """
        _response = self._raw_client.push_login_request(callback=callback, request_options=request_options)
        return _response.data


class AsyncLoginClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoginClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLoginClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoginClient
        """
        return self._raw_client

    async def push_login_request(
        self, *, callback: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PushLoginRequestResponse:
        """
        push sign-in request
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        callback : str
            URI App will connect to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PushLoginRequestResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.login.push_login_request(
                callback="callback",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.push_login_request(callback=callback, request_options=request_options)
        return _response.data
