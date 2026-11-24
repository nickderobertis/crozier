

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.nullable_color import NullableColor
from ..types.shade import Shade
from .raw_client import AsyncRawSimpleEncodingClient, RawSimpleEncodingClient
from .types.encode_value_request_x_inline_nullable_enum import EncodeValueRequestXInlineNullableEnum


class SimpleEncodingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSimpleEncodingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSimpleEncodingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSimpleEncodingClient
        """
        return self._raw_client

    def encode_value(
        self,
        *,
        nullable_enum: typing.Optional[NullableColor] = None,
        inline_nullable_enum: typing.Optional[EncodeValueRequestXInlineNullableEnum] = None,
        wrapped_nullable_enum: typing.Optional[Shade] = None,
        plain_enum: typing.Optional[Shade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        nullable_enum : typing.Optional[NullableColor]

        inline_nullable_enum : typing.Optional[EncodeValueRequestXInlineNullableEnum]

        wrapped_nullable_enum : typing.Optional[Shade]

        plain_enum : typing.Optional[Shade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.simple_encoding.encode_value()
        """
        _response = self._raw_client.encode_value(
            nullable_enum=nullable_enum,
            inline_nullable_enum=inline_nullable_enum,
            wrapped_nullable_enum=wrapped_nullable_enum,
            plain_enum=plain_enum,
            request_options=request_options,
        )
        return _response.data

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi()
        client.simple_encoding.ping()
        """
        _response = self._raw_client.ping(request_options=request_options)
        return _response.data


class AsyncSimpleEncodingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSimpleEncodingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSimpleEncodingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSimpleEncodingClient
        """
        return self._raw_client

    async def encode_value(
        self,
        *,
        nullable_enum: typing.Optional[NullableColor] = None,
        inline_nullable_enum: typing.Optional[EncodeValueRequestXInlineNullableEnum] = None,
        wrapped_nullable_enum: typing.Optional[Shade] = None,
        plain_enum: typing.Optional[Shade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        nullable_enum : typing.Optional[NullableColor]

        inline_nullable_enum : typing.Optional[EncodeValueRequestXInlineNullableEnum]

        wrapped_nullable_enum : typing.Optional[Shade]

        plain_enum : typing.Optional[Shade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.simple_encoding.encode_value()


        asyncio.run(main())
        """
        _response = await self._raw_client.encode_value(
            nullable_enum=nullable_enum,
            inline_nullable_enum=inline_nullable_enum,
            wrapped_nullable_enum=wrapped_nullable_enum,
            plain_enum=plain_enum,
            request_options=request_options,
        )
        return _response.data

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi()


        async def main() -> None:
            await client.simple_encoding.ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping(request_options=request_options)
        return _response.data
