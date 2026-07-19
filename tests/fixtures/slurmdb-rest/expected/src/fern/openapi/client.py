

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOpenapiClient, RawOpenapiClient


class OpenapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOpenapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOpenapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOpenapiClient
        """
        return self._raw_client

    def retrieve_open_api_specification(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.openapi.retrieve_open_api_specification()
        """
        _response = self._raw_client.retrieve_open_api_specification(request_options=request_options)
        return _response.data


class AsyncOpenapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOpenapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOpenapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOpenapiClient
        """
        return self._raw_client

    async def retrieve_open_api_specification(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.openapi.retrieve_open_api_specification()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_open_api_specification(request_options=request_options)
        return _response.data
