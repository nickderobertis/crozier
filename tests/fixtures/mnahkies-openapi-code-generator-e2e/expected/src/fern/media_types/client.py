

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.product_order import ProductOrder
from ..types.product_order_address import ProductOrderAddress
from .raw_client import AsyncRawMediaTypesClient, RawMediaTypesClient


OMIT = typing.cast(typing.Any, ...)


class MediaTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMediaTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMediaTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMediaTypesClient
        """
        return self._raw_client

    def post_media_types_text(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Rendered as HTML

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.media_types.post_media_types_text()
        """
        _response = self._raw_client.post_media_types_text(request_options=request_options)
        return _response.data

    def post_media_types_x_www_form_urlencoded(
        self,
        *,
        sku: typing.Optional[str] = OMIT,
        quantity: typing.Optional[float] = OMIT,
        address: typing.Optional[ProductOrderAddress] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProductOrder:
        """
        Parameters
        ----------
        sku : typing.Optional[str]

        quantity : typing.Optional[float]

        address : typing.Optional[ProductOrderAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProductOrder
            Echoed back as JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.media_types.post_media_types_x_www_form_urlencoded()
        """
        _response = self._raw_client.post_media_types_x_www_form_urlencoded(
            sku=sku, quantity=quantity, address=address, request_options=request_options
        )
        return _response.data

    def post_media_types_octet_stream(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            ok
        """
        with self._raw_client.post_media_types_octet_stream(request=request, request_options=request_options) as r:
            yield from r.data


class AsyncMediaTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMediaTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMediaTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMediaTypesClient
        """
        return self._raw_client

    async def post_media_types_text(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Rendered as HTML

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.media_types.post_media_types_text()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_media_types_text(request_options=request_options)
        return _response.data

    async def post_media_types_x_www_form_urlencoded(
        self,
        *,
        sku: typing.Optional[str] = OMIT,
        quantity: typing.Optional[float] = OMIT,
        address: typing.Optional[ProductOrderAddress] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProductOrder:
        """
        Parameters
        ----------
        sku : typing.Optional[str]

        quantity : typing.Optional[float]

        address : typing.Optional[ProductOrderAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProductOrder
            Echoed back as JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.media_types.post_media_types_x_www_form_urlencoded()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_media_types_x_www_form_urlencoded(
            sku=sku, quantity=quantity, address=address, request_options=request_options
        )
        return _response.data

    async def post_media_types_octet_stream(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            ok
        """
        async with self._raw_client.post_media_types_octet_stream(
            request=request, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
