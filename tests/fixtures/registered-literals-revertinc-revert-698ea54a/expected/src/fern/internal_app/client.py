

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.internal_recent_app_api_calls_response import InternalRecentAppApiCallsResponse
from .raw_client import AsyncRawInternalAppClient, RawInternalAppClient


class InternalAppClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalAppClient
        """
        return self._raw_client

    def internal_app_get_recent_api_calls_for_app(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalRecentAppApiCallsResponse:
        """
        Recent api calls for App

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalRecentAppApiCallsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_app.internal_app_get_recent_api_calls_for_app(
            app_id="appId",
        )
        """
        _response = self._raw_client.internal_app_get_recent_api_calls_for_app(app_id, request_options=request_options)
        return _response.data


class AsyncInternalAppClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalAppClient
        """
        return self._raw_client

    async def internal_app_get_recent_api_calls_for_app(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalRecentAppApiCallsResponse:
        """
        Recent api calls for App

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalRecentAppApiCallsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_app.internal_app_get_recent_api_calls_for_app(
                app_id="appId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_app_get_recent_api_calls_for_app(
            app_id, request_options=request_options
        )
        return _response.data
