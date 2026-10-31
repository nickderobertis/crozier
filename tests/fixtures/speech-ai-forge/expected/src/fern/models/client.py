

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.base_response import BaseResponse
from .raw_client import AsyncRawModelsClient, RawModelsClient


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModelsClient
        """
        return self._raw_client

    def reload_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.models.reload_models()
        """
        _response = self._raw_client.reload_models(request_options=request_options)
        return _response.data

    def unload_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.models.unload_models()
        """
        _response = self._raw_client.unload_models(request_options=request_options)
        return _response.data


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModelsClient
        """
        return self._raw_client

    async def reload_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.models.reload_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.reload_models(request_options=request_options)
        return _response.data

    async def unload_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.models.unload_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.unload_models(request_options=request_options)
        return _response.data
