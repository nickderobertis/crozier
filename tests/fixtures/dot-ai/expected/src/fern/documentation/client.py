

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.openapi_get_response import OpenapiGetResponse
from .raw_client import AsyncRawDocumentationClient, RawDocumentationClient


class DocumentationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDocumentationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDocumentationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDocumentationClient
        """
        return self._raw_client

    def get_the_open_api30specification_for_this_api(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OpenapiGetResponse:
        """
        Get the OpenAPI 3.0 specification for this API

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenapiGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.documentation.get_the_open_api30specification_for_this_api()
        """
        _response = self._raw_client.get_the_open_api30specification_for_this_api(request_options=request_options)
        return _response.data


class AsyncDocumentationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDocumentationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDocumentationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDocumentationClient
        """
        return self._raw_client

    async def get_the_open_api30specification_for_this_api(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OpenapiGetResponse:
        """
        Get the OpenAPI 3.0 specification for this API

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenapiGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.documentation.get_the_open_api30specification_for_this_api()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_open_api30specification_for_this_api(request_options=request_options)
        return _response.data
