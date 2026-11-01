

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLampsClient, RawLampsClient


OMIT = typing.cast(typing.Any, ...)


class LampsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLampsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLampsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLampsClient
        """
        return self._raw_client

    def log_check(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.lamps.log_check(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.log_check(request=request, request_options=request_options)
        return _response.data

    def log_trim(
        self, *, note: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.lamps.log_trim()
        """
        _response = self._raw_client.log_trim(note=note, request_options=request_options)
        return _response.data


class AsyncLampsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLampsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLampsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLampsClient
        """
        return self._raw_client

    async def log_check(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            await client.lamps.log_check(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.log_check(request=request, request_options=request_options)
        return _response.data

    async def log_trim(
        self, *, note: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        note : typing.Optional[str]

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
            await client.lamps.log_trim()


        asyncio.run(main())
        """
        _response = await self._raw_client.log_trim(note=note, request_options=request_options)
        return _response.data
