

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

    def get_v1schema_openapi(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the OpenAPI schema.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The OpenAPI schema.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.openapi.get_v1schema_openapi()
        """
        _response = self._raw_client.get_v1schema_openapi(request_options=request_options)
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

    async def get_v1schema_openapi(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the OpenAPI schema.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The OpenAPI schema.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.openapi.get_v1schema_openapi()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1schema_openapi(request_options=request_options)
        return _response.data
