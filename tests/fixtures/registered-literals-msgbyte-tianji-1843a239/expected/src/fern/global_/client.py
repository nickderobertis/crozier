

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGlobalClient, RawGlobalClient
from .types.global_config_response import GlobalConfigResponse


class GlobalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlobalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlobalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlobalClient
        """
        return self._raw_client

    def config(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalConfigResponse:
        """
        Get Tianji system global config

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalConfigResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.global_.config()
        """
        _response = self._raw_client.config(request_options=request_options)
        return _response.data


class AsyncGlobalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlobalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlobalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlobalClient
        """
        return self._raw_client

    async def config(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalConfigResponse:
        """
        Get Tianji system global config

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalConfigResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.global_.config()


        asyncio.run(main())
        """
        _response = await self._raw_client.config(request_options=request_options)
        return _response.data
