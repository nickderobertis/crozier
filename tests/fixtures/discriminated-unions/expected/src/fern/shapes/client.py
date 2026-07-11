

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.shape import Shape
from .raw_client import AsyncRawShapesClient, RawShapesClient


OMIT = typing.cast(typing.Any, ...)


class ShapesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShapesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShapesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShapesClient
        """
        return self._raw_client

    def createshape(self, *, request: Shape, request_options: typing.Optional[RequestOptions] = None) -> Shape:
        """
        Parameters
        ----------
        request : Shape

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Shape


        Examples
        --------
        from fern import FernApi, Shape_Circle

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.shapes.createshape(
            request=Shape_Circle(
                radius=1.1,
            ),
        )
        """
        _response = self._raw_client.createshape(request=request, request_options=request_options)
        return _response.data


class AsyncShapesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShapesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShapesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShapesClient
        """
        return self._raw_client

    async def createshape(self, *, request: Shape, request_options: typing.Optional[RequestOptions] = None) -> Shape:
        """
        Parameters
        ----------
        request : Shape

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Shape


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Shape_Circle

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shapes.createshape(
                request=Shape_Circle(
                    radius=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createshape(request=request, request_options=request_options)
        return _response.data
