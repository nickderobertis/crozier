

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.node import Node
from .raw_client import AsyncRawPredClient, RawPredClient


OMIT = typing.cast(typing.Any, ...)


class PredClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPredClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPredClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPredClient
        """
        return self._raw_client

    def put_pred(self, *, request: Node, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : Node

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, Node_And

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pred.put_pred(
            request=Node_And(
                children=[],
            ),
        )
        """
        _response = self._raw_client.put_pred(request=request, request_options=request_options)
        return _response.data


class AsyncPredClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPredClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPredClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPredClient
        """
        return self._raw_client

    async def put_pred(self, *, request: Node, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : Node

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Node_And

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pred.put_pred(
                request=Node_And(
                    children=[],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_pred(request=request, request_options=request_options)
        return _response.data
