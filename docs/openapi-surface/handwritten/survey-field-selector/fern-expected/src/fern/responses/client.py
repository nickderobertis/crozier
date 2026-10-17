

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawResponsesClient, RawResponsesClient
from .types.list_responses_request_select_item import ListResponsesRequestSelectItem


class ResponsesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawResponsesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawResponsesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawResponsesClient
        """
        return self._raw_client

    def list_responses(
        self,
        *,
        select: typing.Optional[
            typing.Union[ListResponsesRequestSelectItem, typing.Sequence[ListResponsesRequestSelectItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        select : typing.Optional[typing.Union[ListResponsesRequestSelectItem, typing.Sequence[ListResponsesRequestSelectItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.responses.list_responses()
        """
        _response = self._raw_client.list_responses(select=select, request_options=request_options)
        return _response.data


class AsyncResponsesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawResponsesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawResponsesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawResponsesClient
        """
        return self._raw_client

    async def list_responses(
        self,
        *,
        select: typing.Optional[
            typing.Union[ListResponsesRequestSelectItem, typing.Sequence[ListResponsesRequestSelectItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        select : typing.Optional[typing.Union[ListResponsesRequestSelectItem, typing.Sequence[ListResponsesRequestSelectItem]]]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.responses.list_responses()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_responses(select=select, request_options=request_options)
        return _response.data
