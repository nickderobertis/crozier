

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.firing_note import FiringNote
from ..types.seal_request import SealRequest
from .raw_client import AsyncRawFiringsClient, RawFiringsClient


OMIT = typing.cast(typing.Any, ...)


class FiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFiringsClient
        """
        return self._raw_client

    def plan_firing(
        self, *, request: typing.Optional[FiringNote] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : typing.Optional[FiringNote]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The planned firing.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.plan_firing()
        """
        _response = self._raw_client.plan_firing(request=request, request_options=request_options)
        return _response.data

    def record_firing(
        self, *, request: typing.Optional[FiringNote] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FiringNote]:
        """
        Parameters
        ----------
        request : typing.Optional[FiringNote]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FiringNote]
            The recorded firing.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.record_firing(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.record_firing(request=request, request_options=request_options)
        return _response.data

    def seal_firing(
        self, *, request: SealRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : SealRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The sealed firing.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.seal_firing(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.seal_firing(request=request, request_options=request_options)
        return _response.data


class AsyncFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFiringsClient
        """
        return self._raw_client

    async def plan_firing(
        self, *, request: typing.Optional[FiringNote] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : typing.Optional[FiringNote]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The planned firing.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.plan_firing()


        asyncio.run(main())
        """
        _response = await self._raw_client.plan_firing(request=request, request_options=request_options)
        return _response.data

    async def record_firing(
        self, *, request: typing.Optional[FiringNote] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FiringNote]:
        """
        Parameters
        ----------
        request : typing.Optional[FiringNote]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FiringNote]
            The recorded firing.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.record_firing(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_firing(request=request, request_options=request_options)
        return _response.data

    async def seal_firing(
        self, *, request: SealRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : SealRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The sealed firing.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.seal_firing(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.seal_firing(request=request, request_options=request_options)
        return _response.data
