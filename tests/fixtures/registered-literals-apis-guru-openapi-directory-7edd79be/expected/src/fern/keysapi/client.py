

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.current_key import CurrentKey
from ..types.expiry import Expiry
from ..types.key_view import KeyView
from .raw_client import AsyncRawKeysapiClient, RawKeysapiClient


class KeysapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKeysapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKeysapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKeysapiClient
        """
        return self._raw_client

    def current(
        self, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CurrentKey]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CurrentKey]


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.keysapi.current(
            serial="serial",
        )
        """
        _response = self._raw_client.current(serial, request_options=request_options)
        return _response.data

    def custom(self, serial: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]

        """
        with self._raw_client.custom(serial, request_options=request_options) as r:
            yield from r.data

    def expiry(
        self, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Expiry]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Expiry]


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.keysapi.expiry(
            serial="serial",
        )
        """
        _response = self._raw_client.expiry(serial, request_options=request_options)
        return _response.data

    def find(self, serial: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Optional[KeyView]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[KeyView]


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.keysapi.find(
            serial="serial",
        )
        """
        _response = self._raw_client.find(serial, request_options=request_options)
        return _response.data


class AsyncKeysapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKeysapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKeysapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKeysapiClient
        """
        return self._raw_client

    async def current(
        self, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CurrentKey]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CurrentKey]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.keysapi.current(
                serial="serial",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.current(serial, request_options=request_options)
        return _response.data

    async def custom(
        self, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]

        """
        async with self._raw_client.custom(serial, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def expiry(
        self, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Expiry]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Expiry]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.keysapi.expiry(
                serial="serial",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.expiry(serial, request_options=request_options)
        return _response.data

    async def find(
        self, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[KeyView]:
        """
        Parameters
        ----------
        serial : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[KeyView]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.keysapi.find(
                serial="serial",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find(serial, request_options=request_options)
        return _response.data
