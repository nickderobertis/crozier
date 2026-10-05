

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.layer import Layer
from .raw_client import AsyncRawLayersClient, RawLayersClient


OMIT = typing.cast(typing.Any, ...)


class LayersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLayersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLayersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLayersClient
        """
        return self._raw_client

    def create_layer(
        self,
        *,
        title: str,
        opacity: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Layer:
        """
        Parameters
        ----------
        title : str

        opacity : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Layer
            The created layer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            "v2",
        )
        client.layers.create_layer(
            title="title",
        )
        """
        _response = self._raw_client.create_layer(title=title, opacity=opacity, request_options=request_options)
        return _response.data

    def get_layer(self, layer_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Layer:
        """
        Parameters
        ----------
        layer_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Layer
            One layer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            "v2",
        )
        client.layers.get_layer(
            layer_id="layer_id",
        )
        """
        _response = self._raw_client.get_layer(layer_id, request_options=request_options)
        return _response.data


class AsyncLayersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLayersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLayersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLayersClient
        """
        return self._raw_client

    async def create_layer(
        self,
        *,
        title: str,
        opacity: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Layer:
        """
        Parameters
        ----------
        title : str

        opacity : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Layer
            The created layer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            "v2",
        )


        async def main() -> None:
            await client.layers.create_layer(
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_layer(title=title, opacity=opacity, request_options=request_options)
        return _response.data

    async def get_layer(self, layer_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Layer:
        """
        Parameters
        ----------
        layer_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Layer
            One layer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            "v2",
        )


        async def main() -> None:
            await client.layers.get_layer(
                layer_id="layer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_layer(layer_id, request_options=request_options)
        return _response.data
